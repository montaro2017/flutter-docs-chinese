package main

import (
	"encoding/json"
	"fmt"
	"html"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"sort"
	"strings"
	"sync"
)

type inventory struct { Pages []string `json:"pages"` }
type item struct { text string; page string; raw string }
type result struct { index int; items []item }
type tally struct { n int; first item; order int }

var (
	listRE = regexp.MustCompile(`(?is)<li\b[^>]*>.*?</li>`)
	inlineRE = regexp.MustCompile(`(?is)<(?:a|code|pre)\b[^>]*>.*?</(?:a|code|pre)>`)
	tagRE = regexp.MustCompile(`<[^>]+>`)
	wordRE = regexp.MustCompile(`[A-Za-z]+`)
)

func hasChinese(s string) bool {
	for _, r := range s { if r >= 0x3400 && r <= 0x9fff { return true } }
	return false
}

func scan(root, rel string, index int) result {
	b, err := os.ReadFile(filepath.Join(root, filepath.FromSlash(rel)))
	if err != nil { return result{index:index} }
	content := string(b)
	matches := listRE.FindAllString(content, -1)
	items := make([]item, 0, len(matches)/4)
	for _, raw := range matches {
		x := inlineRE.ReplaceAllString(raw, "¤")
		x = tagRE.ReplaceAllString(x, " ")
		x = strings.Join(strings.Fields(html.UnescapeString(x)), " ")
		if hasChinese(x) || len(wordRE.FindAllStringIndex(x, -1)) < 4 { continue }
		items = append(items, item{text:x,page:rel,raw:raw})
	}
	return result{index:index,items:items}
}

func main() {
	inventoryPath := ".translation/reachable-pages.json"
	if len(os.Args)>1 { inventoryPath=os.Args[1] }
	b, err := os.ReadFile(inventoryPath); if err != nil { fmt.Fprintln(os.Stderr,err); os.Exit(1) }
	var inv inventory; if err=json.Unmarshal(b,&inv); err!=nil { fmt.Fprintln(os.Stderr,err); os.Exit(1) }
	root := "flutter.docs.cn"
	if len(os.Args)>2 { root=os.Args[2] }
	workers := runtime.NumCPU(); if workers>16 { workers=16 }; if workers<1 { workers=1 }
	jobs:=make(chan int,workers*2); results:=make(chan result,workers*2)
	var wg sync.WaitGroup
	for w:=0;w<workers;w++ { wg.Add(1); go func(){ defer wg.Done(); for i:=range jobs { rel:=inv.Pages[i]; if !strings.HasPrefix(rel,"flutter/")||!strings.HasSuffix(rel,".html") { continue }; results<-scan(root,rel,i) } }() }
	go func(){ for i,rel:=range inv.Pages { if strings.HasPrefix(rel,"flutter/")&&strings.HasSuffix(rel,".html") { jobs<-i } }; close(jobs); wg.Wait(); close(results) }()
	ordered:=make([]result,len(inv.Pages)); for r:=range results { ordered[r.index]=r }
	counts:=make(map[string]tally); seq:=0
	for _,r:=range ordered { for _,it:=range r.items { v,ok:=counts[it.text]; if !ok { v=tally{first:it,order:seq};seq++ };v.n++;counts[it.text]=v } }
	all:=make([]struct{text string; v tally},0,len(counts));for x,v:=range counts {all=append(all,struct{text string;v tally}{x,v})}
	sort.Slice(all,func(i,j int)bool{if all[i].v.n!=all[j].v.n{return all[i].v.n>all[j].v.n};return all[i].v.order<all[j].v.order})
	limit:=75;if len(all)<limit{limit=len(all)}
	for _,x:=range all[:limit] { text:=[]rune(x.text);if len(text)>280{text=text[:280]};fmt.Printf("%d\t%s\n",x.v.n,string(text)) }
}
