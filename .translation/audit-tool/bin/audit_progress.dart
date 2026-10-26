// Standalone translation progress auditor for flutter.docs / flutter.docs.cn.
// Run from the repository root: dart run .translation/audit-tool/bin/audit_progress.dart
import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'dart:isolate';

import 'package:archive/archive_io.dart';
import 'package:crypto/crypto.dart';
import 'package:html/dom.dart';
import 'package:html/parser.dart' as html_parser;
import 'package:path/path.dart' as p;

const ruleVersion = 'dart-audit-v1';
const unitTags = {
  'p',
  'h1',
  'h2',
  'h3',
  'h4',
  'h5',
  'h6',
  'li',
  'dt',
  'dd',
  'td',
  'th'
};
final wordPattern = RegExp(r"[A-Za-z]+(?:['’\-][A-Za-z]+)*");
final identifierPattern = RegExp(
    r'\b(?:[a-z]+[A-Z][A-Za-z0-9]*|[A-Z][a-z]+[A-Z][A-Za-z0-9]*|[A-Za-z]\w*[_.$]\w[\w.$]*|[A-Z][A-Z0-9_]+)\b');
final urlPattern = RegExp(r'https?://[^\s<>]+|www\.[^\s<>]+');
final hanPattern = RegExp(
    r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u{20000}-\u{2fa1f}\u{30000}-\u{323af}]',
    unicode: true);

late final String repoRoot;
late final String translationDir;
late final String auditDir;
late final Map<String, dynamic> pathMap;
final Map<String, String> archiveSources = {};
final Set<String> archiveRequired = {};

void loadCaseSourceOverrides() {
  final conflicting = pathMap.entries
      .where((entry) => entry.key != entry.value)
      .map((entry) => entry.key)
      .toSet();
  archiveRequired.addAll(conflicting);
  if (conflicting.isEmpty) return;
  final zipPath = p.join(repoRoot, 'flutter.docs', 'flutter.docs.zip');
  if (!File(zipPath).existsSync()) return;
  final input = InputFileStream(zipPath);
  try {
    final archive = ZipDecoder().decodeBuffer(input);
    for (final entry in archive.files) {
      if (!conflicting.contains(entry.name)) continue;
      archiveSources[entry.name] = utf8.decode(entry.content as List<int>);
    }
  } finally {
    input.close();
  }
}

String sha(String value) => sha256.convert(utf8.encode(value)).toString();
String readUtf8(String path) => File(path).readAsStringSync(encoding: utf8);
String pathMapHash() {
  final file = File(p.join(translationDir, 'case-paths.json'));
  return file.existsSync() ? sha(readUtf8(file.path)) : sha('{}');
}

String fileFingerprint(File file) {
  final stat = file.statSync();
  return '${stat.size}:${stat.modified.toUtc().microsecondsSinceEpoch}';
}

Map<String, String> sourceFingerprints() {
  final sourceRoot = p.join(repoRoot, 'flutter.docs');
  final root = Directory(p.join(sourceRoot, 'flutter'));
  final result = <String, String>{};
  for (final entity in root.listSync(recursive: true, followLinks: false)) {
    if (entity is File && entity.path.toLowerCase().endsWith('.html')) {
      final logical =
          p.relative(entity.path, from: sourceRoot).replaceAll('\\', '/');
      result[logical] = fileFingerprint(entity);
    }
  }
  final index = File(p.join(sourceRoot, 'index.html'));
  if (index.existsSync()) result['index.html'] = fileFingerprint(index);
  final archive = File(p.join(sourceRoot, 'flutter.docs.zip'));
  if (archive.existsSync()) {
    result['flutter.docs.zip'] = fileFingerprint(archive);
  }
  return result;
}

Map<String, String> targetFingerprints(Iterable<String> pages) => {
      for (final page in pages)
        page: File(targetPath(page)).existsSync()
            ? fileFingerprint(File(targetPath(page)))
            : ''
    };

bool sameFingerprintMap(Object? oldValue, Map<String, String> current) {
  if (oldValue is! Map || oldValue.length != current.length) return false;
  for (final entry in current.entries) {
    if (oldValue[entry.key] != entry.value) return false;
  }
  return true;
}

Map<String, dynamic>? latestCachedManifest() {
  final runs = Directory(p.join(auditDir, 'runs'));
  if (!runs.existsSync()) return null;
  final candidates = runs.listSync().whereType<Directory>().toList()
    ..sort((a, b) => b.path.compareTo(a.path));
  for (final directory in candidates) {
    final manifest = File(p.join(directory.path, 'manifest.json'));
    if (!manifest.existsSync() ||
        !File(p.join(directory.path, 'pages.jsonl')).existsSync() ||
        !File(p.join(directory.path, 'units.jsonl')).existsSync() ||
        !File(p.join(directory.path, 'report', 'index.md')).existsSync()) {
      continue;
    }
    final value = jsonDecode(readUtf8(manifest.path)) as Map<String, dynamic>;
    if (value['source_fingerprints'] is Map &&
        value['target_fingerprints'] is Map) return value;
  }
  return null;
}

void writeJson(String path, Object value) {
  final file = File(path)..parent.createSync(recursive: true);
  final temp = File('${file.path}.tmp');
  temp.writeAsStringSync(
      '${const JsonEncoder.withIndent('  ').convert(value)}\n',
      encoding: utf8);
  replaceWithTemp(temp, file);
}

Future<void> writeJsonLines(String path, Iterable<Object?> rows) async {
  final sink = File(path).openWrite(encoding: utf8);
  try {
    for (final row in rows) {
      sink.writeln(jsonEncode(row));
    }
    await sink.flush();
  } finally {
    await sink.close();
  }
}

Future<void> writeUnitsWithReplacements(
    String previousPath,
    String outputPath,
    Set<String> replacedPages,
    Iterable<Map<String, dynamic>> replacements) async {
  final sink = File(outputPath).openWrite(encoding: utf8);
  final pagePattern = RegExp(r'"page":"([^"]*)"');
  try {
    await for (final line in File(previousPath)
        .openRead()
        .transform(utf8.decoder)
        .transform(const LineSplitter())) {
      if (line.isEmpty) continue;
      final page = pagePattern.firstMatch(line)?.group(1);
      if (page == null || !replacedPages.contains(page)) sink.writeln(line);
    }
    for (final unit in replacements) {
      sink.writeln(jsonEncode(unit));
    }
    await sink.flush();
  } finally {
    await sink.close();
  }
}

void replaceWithTemp(File temp, File file) {
  if (!file.existsSync()) {
    temp.renameSync(file.path);
    return;
  }
  final backup = File('${file.path}.bak');
  if (backup.existsSync()) backup.deleteSync();
  file.renameSync(backup.path);
  try {
    temp.renameSync(file.path);
    backup.deleteSync();
  } catch (_) {
    if (!file.existsSync() && backup.existsSync()) backup.renameSync(file.path);
    rethrow;
  }
}

String cleanText(String text) => text
    .replaceAll(urlPattern, ' ')
    .replaceAll(identifierPattern, ' ')
    .replaceAll(RegExp(r'\s+'), ' ')
    .trim();
int sourceWords(String text) => wordPattern.allMatches(cleanText(text)).length;
int hanCount(String text) => hanPattern.allMatches(text).length;
bool isBlock(Element e) => unitTags.contains(e.localName);

String closestId(Element node) {
  Node? current = node;
  while (current != null) {
    if (current is Element && (current.attributes['id'] ?? '').isNotEmpty) {
      return current.attributes['id']!;
    }
    current = current.parent;
  }
  return '';
}

bool insideDescription(Element node) {
  Node? current = node.parent;
  while (current != null) {
    if (current is Element &&
        current.localName == 'section' &&
        current.classes.containsAll({'desc', 'markdown'})) return true;
    current = current.parent;
  }
  return false;
}

Map<String, dynamic> parseArgs(List<String> args) {
  final result = <String, dynamic>{'_': <String>[]};
  for (var i = 0; i < args.length; i++) {
    final arg = args[i];
    if (!arg.startsWith('--')) {
      (result['_'] as List<String>).add(arg);
    } else if (arg == '--help' || arg == '-h') {
      result['help'] = true;
    } else if (arg == '--full') {
      result['full'] = true;
    } else if (i + 1 < args.length && !args[i + 1].startsWith('--')) {
      result[arg.substring(2)] = args[++i];
    } else {
      throw FormatException('选项 $arg 缺少参数');
    }
  }
  return result;
}

void usage() {
  stdout.writeln('''Dart 翻译进度审计工具

用法:
  dart run .translation/audit-tool/bin/audit_progress.dart scan [--page PREFIX] [--workers N]
  dart run .translation/audit-tool/bin/audit_progress.dart report --run RUN_ID [--full]
  dart run .translation/audit-tool/bin/audit_progress.dart export-review --run RUN_ID [--out FILE]
  dart run .translation/audit-tool/bin/audit_progress.dart import-review --file FILE

扫描默认生成轻量目录汇总 Markdown；report --full 生成逐页详情。
运行 dart run ... --help 查看完整使用说明：.translation/audit-tool/README.md''');
}

String? attr(Element e, String name) => e.attributes[name];

List<String> linksIn(String markup, String logicalPath) {
  final doc = html_parser.parse(markup);
  String? baseHref = doc.querySelector('base[href]')?.attributes['href'];
  var base = Uri.parse('https://offline.local/$logicalPath');
  if (logicalPath.endsWith('-sidebar.html') && baseHref == null) {
    base = Uri.parse('https://offline.local/flutter/');
  }
  if (baseHref != null) {
    try {
      base = base.resolve(baseHref);
    } on FormatException {/* ignore malformed base */}
  }
  final found = <String>[];
  for (final e in doc.querySelectorAll(
      'a[href], [data-above-sidebar], [data-below-sidebar], meta[http-equiv]')) {
    final rawValues = <String?>[
      e.attributes['href'],
      e.attributes['data-above-sidebar'],
      e.attributes['data-below-sidebar'],
    ];
    final httpEquiv = (e.attributes['http-equiv'] ?? '').toLowerCase();
    if (e.localName == 'meta' && httpEquiv == 'refresh') {
      final match = RegExp(r'url\s*=\s*([^;\s]+)', caseSensitive: false)
          .firstMatch(e.attributes['content'] ?? '');
      if (match != null)
        rawValues.add(match.group(1)!.replaceAll('"', '').replaceAll("'", ''));
    }
    for (final raw in rawValues.whereType<String>()) {
      try {
        final uri = base.resolve(raw.trim());
        if (uri.scheme != 'https' || uri.host != 'offline.local') continue;
        var path =
            Uri.decodeComponent(uri.path).replaceFirst(RegExp(r'^/'), '');
        if (path.isEmpty || path.endsWith('/')) path += 'index.html';
        path = p.posix.normalize(path);
        if (path == 'index.html' || path.startsWith('flutter/'))
          found.add(path);
      } on FormatException {/* malformed local URL is skipped */}
    }
  }
  return found;
}

String sourcePath(String logical) =>
    p.join(repoRoot, 'flutter.docs', p.fromUri(Uri(path: logical)));
String targetPath(String logical) {
  final mapped = pathMap[logical] as String? ?? logical;
  return p.join(repoRoot, 'flutter.docs.cn', p.fromUri(Uri(path: mapped)));
}

String readSourceMarkup(String logical) {
  final archived = archiveSources[logical];
  if (archived != null) return archived;
  if (archiveRequired.contains(logical)) {
    throw StateError('大小写冲突页在 flutter.docs.zip 中缺失：$logical');
  }
  return readUtf8(sourcePath(logical));
}

Future<Map<String, dynamic>> inventory() async {
  final queue = <String>['index.html'];
  final seen = <String>{};
  final queued = <String>{'index.html'};
  final missing = <String>{};
  var cursor = 0;
  while (cursor < queue.length) {
    final page = queue[cursor++];
    if (!seen.add(page)) continue;
    final file = File(sourcePath(page));
    if (!file.existsSync() && !archiveSources.containsKey(page)) {
      missing.add(page);
      continue;
    }
    final markup = readSourceMarkup(page);
    for (final link in linksIn(markup, page)) {
      if (link != 'index.html' && !link.toLowerCase().endsWith('.html')) {
        continue;
      }
      if (seen.contains(link) || queued.contains(link)) continue;
      if (File(sourcePath(link)).existsSync() ||
          archiveSources.containsKey(link)) {
        queued.add(link);
        queue.add(link);
      } else if (link.toLowerCase().endsWith('.html')) {
        missing.add(link);
      }
    }
    if (cursor % 10000 == 0) stderr.writeln('已遍历 $cursor 个文档页...');
  }
  final pages = seen
      .where(
          (v) => v.startsWith('flutter/') && v.toLowerCase().endsWith('.html'))
      .toList()
    ..sort();
  final physical = Directory(p.join(repoRoot, 'flutter.docs', 'flutter'))
      .listSync(recursive: true, followLinks: false)
      .whereType<File>()
      .where((f) => f.path.toLowerCase().endsWith('.html'))
      .map((f) => p
          .relative(f.path, from: p.join(repoRoot, 'flutter.docs'))
          .replaceAll('\\', '/'))
      .toSet();
  final unreachable = physical.difference(seen).toList()..sort();
  return {
    'pages': pages,
    'missing_links': missing.toList()..sort(),
    'unreachable': unreachable
  };
}

String nodeText(Node node) {
  if (node is Text) return node.text;
  if (node is Element &&
      {'script', 'style', 'template', 'noscript', 'pre', 'code'}
          .contains(node.localName)) return '';
  if (node is Element &&
      node.localName == 'a' &&
      node.attributes['href'] != null) {
    final label = node.nodes
        .map(nodeText)
        .join(' ')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim();
    if (RegExp(r'^[A-Za-z_$][\w.$]*(?:\(\))?$').hasMatch(label)) return '';
  }
  return node.nodes.map(nodeText).join(' ');
}

String canonicalLink(
    String raw, String page, bool target, Map<String, dynamic> mappings) {
  try {
    final mappedPage = target ? mappings[page] as String? ?? page : page;
    final uri = Uri.parse('https://offline.local/$mappedPage').resolve(raw);
    if (uri.host != 'offline.local') return raw;
    var logical = Uri.decodeComponent(uri.path).replaceFirst(RegExp(r'^/'), '');
    for (final entry in mappings.entries) {
      if (entry.value == logical) {
        logical = entry.key;
        break;
      }
    }
    return '$logical${uri.hasQuery ? '?${uri.query}' : ''}${uri.hasFragment ? '#${uri.fragment}' : ''}';
  } on FormatException {
    return raw;
  }
}

void collectBlockUnits(
    Node node,
    String region,
    String page,
    bool target,
    Map<String, dynamic> mappings,
    List<Map<String, dynamic>> out,
    Map<String, int> indexes,
    {bool insideBlock = false}) {
  if (node is Text && !insideBlock) {
    final text = node.text.replaceAll(RegExp(r'\s+'), ' ').trim();
    if (text.isNotEmpty) {
      final index =
          indexes.update('$region:direct', (v) => v + 1, ifAbsent: () => 0);
      out.add({
        'region': region,
        'locator': 'direct[$index]',
        'anchor': '',
        'tag': 'direct',
        'source': text,
        'structure': jsonEncode({'tag': 'direct'}),
        'link_hash': sha('[]'),
        'code_hash': sha('[]')
      });
    }
    return;
  }
  if (node is Element) {
    final tag = node.localName ?? '';
    if ({'script', 'style', 'template', 'noscript', 'pre', 'code'}
        .contains(tag)) return;
    if (isBlock(node) && !insideBlock) {
      final text = nodeText(node).replaceAll(RegExp(r'\s+'), ' ').trim();
      final index =
          indexes.update('$region:$tag', (v) => v + 1, ifAbsent: () => 0);
      final anchor = node.attributes['id'] ?? closestId(node);
      final hrefs = node
          .querySelectorAll('a[href]')
          .map((e) =>
              canonicalLink(e.attributes['href'] ?? '', page, target, mappings))
          .toList();
      final code = node
          .querySelectorAll('code, pre')
          .map((e) =>
              '${e.localName}:${sha(e.text.replaceAll(RegExp(r'\s+'), ' ').trim())}')
          .toList();
      final structure = jsonEncode({'tag': tag});
      if (text.isNotEmpty) {
        out.add({
          'region': region,
          'locator': '$tag[$index]',
          'anchor': anchor,
          'tag': tag,
          'source': text,
          'structure': structure,
          'link_hash': sha(jsonEncode(hrefs)),
          'code_hash': sha(jsonEncode(code))
        });
      }
      return;
    }
  }
  for (final child in node.nodes) {
    collectBlockUnits(child, region, page, target, mappings, out, indexes,
        insideBlock: insideBlock || (node is Element && isBlock(node)));
  }
}

List<Map<String, dynamic>> extractUnits(
    String markup, String page, bool target, Map<String, dynamic> mappings) {
  final doc = html_parser.parse(markup);
  final result = <Map<String, dynamic>>[];
  final indexes = <String, int>{};
  var sectionNumber = 0;
  for (final section in doc.querySelectorAll('section.desc.markdown')) {
    final region = 'description:${section.attributes['id'] ?? sectionNumber++}';
    collectBlockUnits(section, region, page, target, mappings, result, indexes);
  }
  for (final dd in doc.querySelectorAll('dd')) {
    if (insideDescription(dd)) continue;
    collectBlockUnits(dd, 'summary', page, target, mappings, result, indexes);
  }
  return result;
}

int residualEnglish(String target) {
  final cleaned = cleanText(target);
  for (final sentence in cleaned.split(RegExp(r'(?<=[.!?。！？;；])\s+|\n+'))) {
    final ordinary = wordPattern.allMatches(sentence).where((m) {
      final word = m.group(0)!;
      final titleCase = word.isNotEmpty &&
          word[0].toUpperCase() == word[0] &&
          word.substring(1).toLowerCase() == word.substring(1);
      return word.toLowerCase() == word || titleCase;
    }).length;
    if (ordinary >= 4) return ordinary;
  }
  return 0;
}

Map<String, dynamic> scanPage(Map<String, dynamic> args) {
  final logical = args['page'] as String;
  final sourceFile = File(args['source'] as String);
  final targetFile = File(args['target'] as String);
  final output = <Map<String, dynamic>>[];
  final sourceMarkup = args['source_markup'] as String? ??
      sourceFile.readAsStringSync(encoding: utf8);
  final sourceHash = sha(sourceMarkup);
  final mappings = args['path_map'] as Map<String, dynamic>;
  final source = extractUnits(sourceMarkup, logical, false, mappings);
  final targetExists = targetFile.existsSync();
  final targetMarkup =
      targetExists ? targetFile.readAsStringSync(encoding: utf8) : null;
  final targetHash = targetMarkup == null ? '' : sha(targetMarkup);
  final target = targetMarkup == null
      ? <Map<String, dynamic>>[]
      : extractUnits(targetMarkup, logical, true, mappings);
  final sourceRegions = <String, List<Map<String, dynamic>>>{};
  final targetRegions = <String, List<Map<String, dynamic>>>{};
  for (final u in source) {
    (sourceRegions[u['region']] ??= []).add(u);
  }
  for (final u in target) {
    (targetRegions[u['region']] ??= []).add(u);
  }
  var changedWords = 0,
      modifiedWords = 0,
      totalWords = 0,
      confirmedWords = 0,
      reviewedWords = 0,
      excludedWords = 0;
  var unchangedUnits = 0,
      changedUnits = 0,
      suspiciousUnits = 0,
      unalignedUnits = 0,
      missingUnits = 0;
  for (final entry in sourceRegions.entries) {
    final oldUnits = entry.value;
    final newUnits = targetRegions[entry.key] ?? <Map<String, dynamic>>[];
    final targetRegionPresent = targetRegions.containsKey(entry.key);
    final regionAligned = targetExists &&
        targetRegionPresent &&
        oldUnits.length == newUnits.length &&
        List.generate(
                oldUnits.length,
                (i) =>
                    oldUnits[i]['tag'] == newUnits[i]['tag'] &&
                    oldUnits[i]['structure'] == newUnits[i]['structure'])
            .every((v) => v);
    for (var i = 0; i < oldUnits.length; i++) {
      final src = oldUnits[i];
      final words = sourceWords(src['source'] as String);
      if (words == 0) continue;
      totalWords += words;
      String? targetText;
      String auto;
      if (!targetExists) {
        auto = 'missing_target';
        missingUnits++;
      } else if (!targetRegionPresent) {
        auto = 'missing_unit';
        missingUnits++;
      } else if (!regionAligned) {
        auto = 'unaligned';
        unalignedUnits++;
      } else if (i >= newUnits.length) {
        auto = 'missing_unit';
        missingUnits++;
      } else {
        targetText = newUnits[i]['source'] as String;
        if (targetText != src['source']) modifiedWords += words;
        if (targetText == src['source']) {
          auto = 'unchanged';
          unchangedUnits++;
        } else if (hanCount(targetText) > 0 &&
            residualEnglish(targetText) < 4) {
          auto = 'changed';
          changedUnits++;
          changedWords += words;
        } else {
          auto = 'suspicious';
          suspiciousUnits++;
        }
      }
      final locator = '${src['region']}/${src['locator']}';
      final targetUnit = targetExists && regionAligned && i < newUnits.length
          ? newUnits[i]
          : null;
      final codeChanged =
          targetUnit != null && targetUnit['code_hash'] != src['code_hash'];
      final linksChanged =
          targetUnit != null && targetUnit['link_hash'] != src['link_hash'];
      final unitId = sha(
          '$logical|$locator|${sha(src['source'] as String)}|${sha(src['structure'] as String)}');
      final unit = <String, dynamic>{
        'unit_id': unitId,
        'rule_version': ruleVersion,
        'page': logical,
        'region': src['region'],
        'locator': src['locator'],
        'anchor': src['anchor'],
        'tag': src['tag'],
        'source': src['source'],
        'target': targetText,
        'source_words': words,
        'source_hash': sha(src['source'] as String),
        'target_hash': targetText == null ? '' : sha(targetText),
        'structure_hash': sha(
            '${src['structure']}|${src['link_hash']}|${targetUnit?['link_hash'] ?? ''}|${src['code_hash']}|${targetUnit?['code_hash'] ?? ''}'),
        'auto_status': auto,
        'review_status': 'pending',
        'review_reason': '',
        'issues': [
          if (auto.startsWith('missing') || auto == 'unaligned') auto,
          if (linksChanged) 'link_change',
          if (codeChanged) 'code_change'
        ],
      };
      output.add(unit);
    }
  }
  final keyHash = sha('$logical');
  return {
    'page': logical,
    'source_path': p
        .relative(sourceFile.path, from: args['repo_root'] as String)
        .replaceAll('\\', '/'),
    'target_path': p
        .relative(targetFile.path, from: args['repo_root'] as String)
        .replaceAll('\\', '/'),
    'source_hash': sourceHash,
    'target_hash': targetHash,
    'target_exists': targetExists,
    'unit_count': output.length,
    'source_words': totalWords,
    'changed_words': changedWords,
    'modified_words': modifiedWords,
    'changed_percent': totalWords == 0 ? null : changedWords * 100 / totalWords,
    'confirmed_words': confirmedWords,
    'reviewed_words': reviewedWords,
    'excluded_words': excludedWords,
    'unchanged_units': unchangedUnits,
    'changed_units': changedUnits,
    'suspicious_units': suspiciousUnits,
    'unaligned_units': unalignedUnits,
    'missing_units': missingUnits,
    'alignment_mismatch': unalignedUnits > 0,
    'units': output,
    'key': keyHash,
  };
}

Future<List<Map<String, dynamic>>> scanBatch(
    List<Map<String, dynamic>> batch) async {
  return Isolate.run(() => batch.map(scanPage).toList());
}

Future<List<Map<String, dynamic>>> parallelScan(
    List<Map<String, dynamic>> tasks, int workers) async {
  final result = <Map<String, dynamic>>[];
  final chunkSize = (tasks.length / workers).ceil().clamp(1, 192);
  for (var start = 0; start < tasks.length; start += chunkSize * workers) {
    final futures = <Future<List<Map<String, dynamic>>>>[];
    for (var worker = 0; worker < workers; worker++) {
      final from = start + worker * chunkSize;
      if (from >= tasks.length) break;
      final to = (from + chunkSize).clamp(0, tasks.length);
      futures.add(scanBatch(tasks.sublist(from, to)));
    }
    for (final batch in await Future.wait(futures)) {
      result.addAll(batch);
    }
    stderr.writeln('已扫描 ${result.length}/${tasks.length} 个页面');
  }
  return result;
}

Map<String, dynamic> readReviews() {
  final file = File(p.join(auditDir, 'reviews.jsonl'));
  final result = <String, dynamic>{};
  if (!file.existsSync()) return result;
  for (final line in file.readAsLinesSync(encoding: utf8)) {
    if (line.trim().isEmpty) continue;
    final row = jsonDecode(line) as Map<String, dynamic>;
    result[row['unit_id'] as String] = row;
  }
  return result;
}

double? percent(num n, num d) => d == 0 ? null : n * 100 / d;

Map<String, dynamic> aggregate(
    Iterable<Map<String, dynamic>> rows, Map<String, dynamic> reviews) {
  var pages = 0,
      words = 0,
      changed = 0,
      modified = 0,
      confirmed = 0,
      reviewed = 0,
      excluded = 0;
  var unchangedWords = 0,
      changedAutoWords = 0,
      suspiciousWords = 0,
      unalignedWords = 0,
      missingWords = 0,
      confirmedUnits = 0,
      excludedUnits = 0,
      unchangedUnits = 0;
  var changedUnits = 0,
      suspicious = 0,
      unaligned = 0,
      missing = 0,
      pending = 0,
      pendingWords = 0,
      eligiblePages = 0,
      completePages = 0;
  for (final row in rows) {
    pages++;
    var pageHasWords = false, pageComplete = true;
    final path = row['page'] as String;
    final unitRows = (row['units'] as List).cast<Map<String, dynamic>>();
    for (final unit in unitRows) {
      final w = unit['source_words'] as int;
      words += w;
      if (unit['auto_status'] == 'changed') {
        changed += w;
        changedAutoWords += w;
        changedUnits++;
      }
      if (unit['auto_status'] == 'changed' ||
          unit['auto_status'] == 'suspicious') modified += w;
      if (unit['auto_status'] == 'unchanged') {
        unchangedUnits++;
        unchangedWords += w;
      }
      if (unit['auto_status'] == 'suspicious') {
        suspicious++;
        suspiciousWords += w;
      }
      if (unit['auto_status'] == 'unaligned') {
        unaligned++;
        unalignedWords += w;
      }
      if ((unit['auto_status'] as String).startsWith('missing')) {
        missing++;
        missingWords += w;
      }
      final saved = reviews[unit['unit_id']];
      final valid = saved is Map &&
          saved['rule_version'] == ruleVersion &&
          saved['source_hash'] == unit['source_hash'] &&
          saved['target_hash'] == unit['target_hash'] &&
          saved['structure_hash'] == unit['structure_hash'];
      final savedDecision = valid ? saved['decision'] : null;
      final decision =
          (unit['issues'] as List).isEmpty || savedDecision == 'excluded'
              ? savedDecision
              : null;
      if (decision == 'excluded') {
        excluded += w;
        excludedUnits++;
        unit['review_status'] = 'excluded';
        unit['review_reason'] = saved['reason'];
      } else if (decision == 'translated' || decision == 'reviewed') {
        confirmed += w;
        confirmedUnits++;
        if (decision == 'reviewed') reviewed += w;
        unit['review_status'] = decision;
        unit['review_reason'] = saved['reason'] ?? '';
      } else {
        pending++;
        pendingWords += w;
        if (unit['auto_status'] != 'excluded') pageComplete = false;
      }
      if (unit['auto_status'] != 'excluded') pageHasWords = true;
      if (unit['auto_status'] == 'unaligned' ||
          (unit['auto_status'] as String).startsWith('missing'))
        pageComplete = false;
    }
    if (pageHasWords) {
      eligiblePages++;
      if (pageComplete) completePages++;
    }
    row['confirmed_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            ((u['review_status'] == 'translated' ||
                    u['review_status'] == 'reviewed')
                ? u['source_words'] as int
                : 0));
    row['confirmed_units'] = unitRows
        .where((u) =>
            u['review_status'] == 'translated' ||
            u['review_status'] == 'reviewed')
        .length;
    row['reviewed_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['review_status'] == 'reviewed' ? u['source_words'] as int : 0));
    row['pending_units'] =
        unitRows.where((u) => u['review_status'] == 'pending').length;
    final pageExcluded = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['review_status'] == 'excluded' ? u['source_words'] as int : 0));
    final pageModified = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            ((u['auto_status'] == 'changed' || u['auto_status'] == 'suspicious')
                ? u['source_words'] as int
                : 0));
    final pageWords = row['source_words'] as int;
    row['excluded_words'] = pageExcluded;
    row['excluded_units'] =
        unitRows.where((u) => u['review_status'] == 'excluded').length;
    row['unchanged_units'] =
        unitRows.where((u) => u['auto_status'] == 'unchanged').length;
    row['unchanged_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['auto_status'] == 'unchanged' ? u['source_words'] as int : 0));
    row['changed_auto_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['auto_status'] == 'changed' ? u['source_words'] as int : 0));
    row['suspicious_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['auto_status'] == 'suspicious' ? u['source_words'] as int : 0));
    row['unaligned_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['auto_status'] == 'unaligned' ? u['source_words'] as int : 0));
    row['missing_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            ((u['auto_status'] as String).startsWith('missing')
                ? u['source_words'] as int
                : 0));
    row['pending_words'] = unitRows.fold<int>(
        0,
        (sum, u) =>
            sum +
            (u['review_status'] == 'pending' ? u['source_words'] as int : 0));
    row['text_change_percent'] = percent(pageModified, pageWords);
    row['confirmed_translation_percent'] =
        percent(row['confirmed_words'] as int, pageWords - pageExcluded);
    row['reviewed_percent'] =
        percent(row['reviewed_words'] as int, pageWords - pageExcluded);
    row['page_completion_percent'] =
        pageHasWords ? (pageComplete ? 100.0 : 0.0) : null;
    row['page_count'] = 1;
    row['has_words'] = pageHasWords;
    row['folder'] = p.posix.dirname(path);
  }
  final denominator = words - excluded;
  return {
    'page_count': pages,
    'eligible_pages': eligiblePages,
    'complete_pages': completePages,
    'source_words': words,
    'excluded_words': excluded,
    'effective_source_words': denominator,
    'changed_words': changed,
    'modified_words': modified,
    'confirmed_words': confirmed,
    'reviewed_words': reviewed,
    'pending_units': pending,
    'pending_words': pendingWords,
    'changed_units': changedUnits,
    'unchanged_words': unchangedWords,
    'changed_auto_words': changedAutoWords,
    'suspicious_units': suspicious,
    'suspicious_words': suspiciousWords,
    'unaligned_units': unaligned,
    'unaligned_words': unalignedWords,
    'missing_units': missing,
    'missing_words': missingWords,
    'confirmed_units': confirmedUnits,
    'excluded_units': excludedUnits,
    'unchanged_units': unchangedUnits,
    'text_change_percent': percent(modified, words),
    'confirmed_translation_percent': percent(confirmed, denominator),
    'reviewed_percent': percent(reviewed, denominator),
    'page_completion_percent': percent(completePages, eligiblePages),
  };
}

Map<String, dynamic> readRun(String runId) {
  final dir = Directory(p.join(auditDir, 'runs', runId));
  if (!dir.existsSync()) throw FormatException('找不到运行快照: $runId');
  final pages = File(p.join(dir.path, 'pages.jsonl'))
      .readAsLinesSync(encoding: utf8)
      .where((s) => s.trim().isNotEmpty)
      .map((s) => jsonDecode(s) as Map<String, dynamic>)
      .toList();
  final unitsByPage = <String, List<Map<String, dynamic>>>{};
  final uf = File(p.join(dir.path, 'units.jsonl'));
  if (uf.existsSync())
    for (final line in uf.readAsLinesSync(encoding: utf8)) {
      if (line.trim().isEmpty) continue;
      final unit = jsonDecode(line) as Map<String, dynamic>;
      (unitsByPage[unit['page'] as String] ??= []).add(unit);
    }
  for (final page in pages) {
    page['units'] = unitsByPage[page['page']] ?? <Map<String, dynamic>>[];
  }
  return {
    'dir': dir.path,
    'pages': pages,
    'manifest': jsonDecode(readUtf8(p.join(dir.path, 'manifest.json')))
        as Map<String, dynamic>
  };
}

String formatPercent(Object? value) =>
    value is num ? '${value.toStringAsFixed(2)}%' : '不适用';
String escapeMarkdown(Object? value) => (value?.toString() ?? '')
    .replaceAll('\\', '\\\\')
    .replaceAllMapped(RegExp(r'([`*_{}\[\]()#+\-.!|<>~])'), (m) => '\\${m[0]}');

String encodePath(String value) =>
    value.split('/').map(Uri.encodeComponent).join('/');

Map<String, dynamic> buildTree(
    List<Map<String, dynamic>> pages, Map<String, dynamic> reviews) {
  final root = <String, dynamic>{
    'name': 'flutter',
    'path': 'flutter',
    'folders': <String, dynamic>{},
    'pages': <Map<String, dynamic>>[],
    'rows': <Map<String, dynamic>>[]
  };
  for (final page in pages) {
    final parts = (page['page'] as String).split('/');
    var node = root;
    for (var i = 0; i < parts.length - 1; i++) {
      final part = parts[i];
      final folders = node['folders'] as Map<String, dynamic>;
      node = folders.putIfAbsent(
          part,
          () => <String, dynamic>{
                'name': part,
                'path': parts.take(i + 1).join('/'),
                'folders': <String, dynamic>{},
                'pages': <Map<String, dynamic>>[],
                'rows': <Map<String, dynamic>>[]
              }) as Map<String, dynamic>;
    }
    (node['pages'] as List<Map<String, dynamic>>).add(page);
  }
  Map<String, dynamic> combineSummaries(
      Iterable<Map<String, dynamic>> summaries) {
    const additive = [
      'page_count',
      'eligible_pages',
      'complete_pages',
      'source_words',
      'excluded_words',
      'changed_words',
      'modified_words',
      'confirmed_words',
      'reviewed_words',
      'pending_units',
      'pending_words',
      'changed_units',
      'unchanged_words',
      'changed_auto_words',
      'suspicious_units',
      'suspicious_words',
      'unaligned_units',
      'unaligned_words',
      'missing_units',
      'missing_words',
      'confirmed_units',
      'excluded_units',
      'unchanged_units'
    ];
    final totals = <String, dynamic>{for (final key in additive) key: 0};
    for (final summary in summaries) {
      for (final key in additive) {
        totals[key] = (totals[key] as num) + (summary[key] as num? ?? 0);
      }
    }
    final words = totals['source_words'] as int;
    final excluded = totals['excluded_words'] as int;
    totals['effective_source_words'] = words - excluded;
    totals['text_change_percent'] = percent(totals['modified_words'], words);
    totals['confirmed_translation_percent'] =
        percent(totals['confirmed_words'], words - excluded);
    totals['reviewed_percent'] =
        percent(totals['reviewed_words'], words - excluded);
    totals['page_completion_percent'] =
        percent(totals['complete_pages'], totals['eligible_pages']);
    return totals;
  }

  Map<String, dynamic> finish(Map<String, dynamic> node) {
    final own = node['pages'] as List<Map<String, dynamic>>;
    final childNodes = (node['folders'] as Map<String, dynamic>)
        .values
        .cast<Map<String, dynamic>>()
        .toList();
    final childSummaries = childNodes.map(finish).toList();
    final pageSummaries = own.map((page) {
      if (page['units'] is List) return aggregate([page], reviews);
      const keys = [
        'page_count',
        'eligible_pages',
        'complete_pages',
        'source_words',
        'excluded_words',
        'changed_words',
        'modified_words',
        'confirmed_words',
        'reviewed_words',
        'pending_units',
        'pending_words',
        'changed_units',
        'unchanged_words',
        'changed_auto_words',
        'suspicious_units',
        'suspicious_words',
        'unaligned_units',
        'unaligned_words',
        'missing_units',
        'missing_words',
        'confirmed_units',
        'excluded_units',
        'unchanged_units',
        'effective_source_words',
        'text_change_percent',
        'confirmed_translation_percent',
        'reviewed_percent',
        'page_completion_percent'
      ];
      return {for (final key in keys) key: page[key] ?? 0};
    }).toList();
    final values = combineSummaries([...childSummaries, ...pageSummaries]);
    final rows = <Map<String, dynamic>>[];
    for (final child in childNodes) {
      rows.add({
        'kind': 'folder',
        'name': child['name'],
        'path': child['path'],
        'summary': child['summary']
      });
    }
    for (final page in own)
      rows.add({
        'kind': 'page',
        'name': p.posix.basename(page['page'] as String),
        'path': page['page'],
        'summary': page,
        'page': page
      });
    rows.sort((a, b) {
      if (a['kind'] != b['kind']) return a['kind'] == 'folder' ? -1 : 1;
      return (a['name'] as String)
          .toLowerCase()
          .compareTo((b['name'] as String).toLowerCase());
    });
    node['summary'] = values;
    node['rows'] = rows;
    return values;
  }

  finish(root);
  return root;
}

String metrics(Map<String, dynamic> v) =>
    '改动 ${formatPercent(v['text_change_percent'])} · ${((v['confirmed_units'] ?? 0) == 0) ? '未建立确认基线' : '已确认 ${formatPercent(v['confirmed_translation_percent'])}'} · 已审核 ${formatPercent(v['reviewed_percent'])} · 页面完成 ${formatPercent(v['page_completion_percent'])} · ${v['confirmed_words']}/${v['source_words']} 词 · ${v['page_count']} 页 · 异常 ${(v['unaligned_units'] as int) + (v['missing_units'] as int)}';

String statusSummary(Map<String, dynamic> v) =>
    '未改动 ${v['unchanged_units'] ?? 0}/${v['unchanged_words'] ?? 0} 词 · 改动 ${v['changed_units'] ?? 0}/${v['changed_auto_words'] ?? 0} 词 · 可疑 ${v['suspicious_units'] ?? 0}/${v['suspicious_words'] ?? 0} 词 · 未对齐 ${v['unaligned_units']}/${v['unaligned_words'] ?? 0} 词 · 缺失 ${v['missing_units']}/${v['missing_words'] ?? 0} 词 · 待确认 ${v['pending_units']}/${v['pending_words'] ?? 0} 词 · 排除 ${v['excluded_units'] ?? 0}/${v['excluded_words']} 词';

void writePageReport(
    String reportDir, Map<String, dynamic> page, String returnHref) {
  final path = p.join(reportDir, 'pages', '${sha(page['page'] as String)}.md');
  final body = StringBuffer()
    ..writeln('# 页面翻译进度')
    ..writeln()
    ..writeln('[← 返回目录]($returnHref)')
    ..writeln()
    ..writeln('页面：`${page['page']}`')
    ..writeln()
    ..writeln(metrics(page))
    ..writeln()
    ..writeln(statusSummary(page));
  for (final unit in (page['units'] as List).cast<Map<String, dynamic>>()) {
    body
      ..writeln()
      ..writeln(
          '## ${escapeMarkdown(unit['locator'])} · ${escapeMarkdown(unit['auto_status'])} / ${escapeMarkdown(unit['review_status'])}')
      ..writeln()
      ..writeln('- 原文词数：${unit['source_words']}')
      ..writeln(
          '- 完整性异常：${escapeMarkdown((unit['issues'] as List).join('、').isEmpty ? '无' : (unit['issues'] as List).join('、'))}')
      ..writeln('- 单元 ID：`${unit['unit_id']}`')
      ..writeln()
      ..writeln('### 原文')
      ..writeln()
      ..writeln('> ${escapeMarkdown(unit['source'])}')
      ..writeln()
      ..writeln('### 译文')
      ..writeln()
      ..writeln(unit['target'] == null
          ? '（缺失或无法可靠对齐）'
          : '> ${escapeMarkdown(unit['target'])}');
  }
  File(path)
    ..parent.createSync(recursive: true)
    ..writeAsStringSync(body.toString(), encoding: utf8);
}

void writeFolderReport(String reportDir, Map<String, dynamic> node,
    String relative, Map<String, dynamic> manifest,
    {required bool includePageDetails}) {
  final path = p.join(reportDir, relative, 'index.md');
  final current = node['summary'] as Map<String, dynamic>;
  final rows = node['rows'] as List<Map<String, dynamic>>;
  final body = StringBuffer()
    ..writeln('# 翻译进度 · ${escapeMarkdown(node['name'])}')
    ..writeln()
    ..writeln('**当前文件夹汇总：** ${metrics(current)}')
    ..writeln()
    ..writeln(statusSummary(current));
  if (relative != '.') {
    final up = List.filled(relative.split('/').length, '../').join();
    body
      ..writeln()
      ..writeln('[↑ 上级](${up}index.md)');
  }
  if (relative == '.') {
    body
      ..writeln()
      ..writeln(
          '范围：${escapeMarkdown(manifest['scope'])}；规则：`${manifest['rule_version']}`。');
    final missingLinks = (manifest['missing_links'] as List?)?.length ?? 0;
    final unreachable = (manifest['unreachable_pages'] as List?)?.length ?? 0;
    final inconsistent = (manifest['inconsistent_pages'] as List?)?.length ?? 0;
    if (missingLinks + inconsistent > 0) {
      body
        ..writeln()
        ..writeln('**完整性异常：** 断链 $missingLinks 项，扫描期间变化 $inconsistent 页。');
    }
    if (unreachable > 0) {
      body
        ..writeln()
        ..writeln('另有 $unreachable 个物理 HTML 页面未从首页导航发现，不自动纳入统计。');
    }
  }
  body
    ..writeln()
    ..writeln(
        '待确认：${current['pending_units']} 个单元 / ${current['pending_words']} 词；原文 ${current['source_words']} 词；人工排除 ${current['excluded_words']} 词。')
    ..writeln()
    ..writeln('## 当前目录内容')
    ..writeln();
  for (final row in rows) {
    final summary = row['summary'] as Map<String, dynamic>;
    final label = escapeMarkdown(row['name']);
    final href = row['kind'] == 'folder'
        ? '${Uri.encodeComponent(row['name'] as String)}/index.md'
        : '${List.filled(relative == '.' ? 0 : relative.split('/').length, '../').join()}pages/${sha(row['path'] as String)}.md';
    final icon = row['kind'] == 'folder' ? '📁' : '📄';
    if (row['kind'] == 'folder' || includePageDetails) {
      body.writeln('- $icon [$label]($href) — ${metrics(summary)}');
    } else {
      body.writeln('- $icon `$label` — ${metrics(summary)}');
    }
    if (row['kind'] == 'page' && includePageDetails) {
      final page = row['page'] as Map<String, dynamic>;
      final returnHref = relative == '.'
          ? '../index.md'
          : '../${encodePath(relative)}/index.md';
      writePageReport(reportDir, page, returnHref);
    }
  }
  File(path)
    ..parent.createSync(recursive: true)
    ..writeAsStringSync(body.toString(), encoding: utf8);
  for (final child in (node['folders'] as Map<String, dynamic>)
      .values
      .cast<Map<String, dynamic>>()) {
    final childName = child['name'] as String;
    writeFolderReport(reportDir, child,
        relative == '.' ? childName : '$relative/$childName', manifest,
        includePageDetails: includePageDetails);
  }
}

Future<void> renderReport(String runId, {bool full = true}) async {
  final run = readRun(runId);
  final pages = (run['pages'] as List).cast<Map<String, dynamic>>();
  final reviews = readReviews();
  final tree = buildTree(pages, reviews);
  writeJson(p.join(run['dir'] as String, 'summary.json'), {
    'run_id': runId,
    'summary': tree['summary'],
    'scope': (run['manifest'] as Map)['scope']
  });
  final reportDir = p.join(run['dir'] as String, 'report');
  final reportDirectory = Directory(reportDir);
  if (reportDirectory.existsSync()) reportDirectory.deleteSync(recursive: true);
  writeFolderReport(
      reportDir, tree, '.', run['manifest'] as Map<String, dynamic>,
      includePageDetails: full);
  stdout.writeln('报告已生成：${p.join(reportDir, 'index.md')}');
}

void renderSummaryReport(String runId, List<Map<String, dynamic>> pages,
    Map<String, dynamic> reviews, Map<String, dynamic> manifest) {
  final runDir = p.join(auditDir, 'runs', runId);
  final tree = buildTree(pages, reviews);
  writeJson(p.join(runDir, 'summary.json'), {
    'run_id': runId,
    'summary': tree['summary'],
    'scope': manifest['scope']
  });
  final reportDir = p.join(runDir, 'report');
  final reportDirectory = Directory(reportDir);
  if (reportDirectory.existsSync()) reportDirectory.deleteSync(recursive: true);
  writeFolderReport(reportDir, tree, '.', manifest, includePageDetails: false);
  stdout.writeln('轻量 Markdown 汇总已生成：${p.join(reportDir, 'index.md')}');
}

Future<int> rescanChangedTargets(
    Map<String, dynamic> cached,
    Map<String, String> currentSources,
    Map<String, String> currentTargets,
    int workers) async {
  final oldRunId = cached['run_id'] as String;
  final oldDir = p.join(auditDir, 'runs', oldRunId);
  final oldPages = File(p.join(oldDir, 'pages.jsonl'))
      .readAsLinesSync(encoding: utf8)
      .where((line) => line.isNotEmpty)
      .map((line) => jsonDecode(line) as Map<String, dynamic>)
      .toList();
  final oldTargets = cached['target_fingerprints'] as Map<String, dynamic>;
  final changedPages = currentTargets.keys
      .where((page) => oldTargets[page] != currentTargets[page])
      .toList()
    ..sort();
  if (changedPages.isEmpty ||
      (cached['inconsistent_pages'] as List? ?? const []).isNotEmpty) {
    return -1;
  }

  if (workers < 1 || workers > 64) throw FormatException('--workers 范围为 1..64');
  final watch = Stopwatch()..start();
  final tasks = changedPages
      .map((logical) => <String, dynamic>{
            'page': logical,
            'repo_root': repoRoot,
            'source': sourcePath(logical),
            'target': targetPath(logical),
            'path_map': pathMap,
            if (archiveRequired.contains(logical))
              'source_markup': readSourceMarkup(logical),
          })
      .toList();
  final changedRows = await parallelScan(tasks, workers);
  final reviews = readReviews();
  final changedByPath = <String, Map<String, dynamic>>{};
  for (final page in changedRows) {
    aggregate([page], reviews);
    changedByPath[page['page'] as String] = page;
  }

  final runId = DateTime.now()
      .toUtc()
      .toIso8601String()
      .replaceAll(':', '')
      .replaceAll('-', '')
      .replaceAll('.', '');
  final runDir = Directory(p.join(auditDir, 'runs', runId))
    ..createSync(recursive: true);
  final replacementUnits = changedRows
      .expand((page) => (page['units'] as List).cast<Map<String, dynamic>>())
      .toList();
  final allPages = <Map<String, dynamic>>[];
  for (final oldPage in oldPages) {
    allPages.add(changedByPath[oldPage['page']] ?? oldPage);
  }
  final newManifest = Map<String, dynamic>.from(cached)
    ..['run_id'] = runId
    ..['created_at'] = DateTime.now().toUtc().toIso8601String()
    ..['source_fingerprints'] = currentSources
    ..['target_fingerprints'] = currentTargets
    ..['workers'] = workers;
  final pageHashes = Map<String, dynamic>.from(cached['page_hashes'] as Map);
  for (final page in changedRows) {
    pageHashes[page['page']] = [page['source_hash'], page['target_hash']];
  }
  newManifest['page_hashes'] = pageHashes;
  writeJson(p.join(runDir.path, 'manifest.json'), newManifest);
  renderSummaryReport(runId, allPages, reviews, newManifest);
  await writeJsonLines(p.join(runDir.path, 'pages.jsonl'), allPages.map((page) {
    page.remove('units');
    return page;
  }));
  await writeUnitsWithReplacements(
      p.join(oldDir, 'units.jsonl'),
      p.join(runDir.path, 'units.jsonl'),
      changedPages.toSet(),
      replacementUnits);
  final summary =
      jsonDecode(readUtf8(p.join(runDir.path, 'summary.json')))['summary']
          as Map<String, dynamic>;
  final updatedTargets = targetFingerprints(changedPages);
  final inconsistent = <String>{
    ...(newManifest['inconsistent_pages'] as List? ?? const []).cast<String>(),
    for (final page in changedPages)
      if (updatedTargets[page] != currentTargets[page]) page,
  }.toList()
    ..sort();
  newManifest['inconsistent_pages'] = inconsistent;
  for (final page in changedPages) {
    currentTargets[page] = updatedTargets[page]!;
  }
  newManifest['target_fingerprints'] = currentTargets;
  watch.stop();
  newManifest['elapsed_ms'] = watch.elapsedMilliseconds;
  newManifest['has_issues'] =
      (newManifest['missing_links'] as List? ?? const []).isNotEmpty ||
          (newManifest['inconsistent_pages'] as List? ?? const []).isNotEmpty ||
          (summary['unaligned_units'] as int) != 0 ||
          (summary['missing_units'] as int) != 0;
  writeJson(p.join(runDir.path, 'manifest.json'), newManifest);
  stdout.writeln(
      '增量扫描 $runId：更新 ${changedPages.length} 页，${watch.elapsed.inSeconds} 秒。');
  return newManifest['has_issues'] == true ? 2 : 0;
}

Future<int> runScan(Map<String, dynamic> args) async {
  final sourceRoot = Directory(p.join(repoRoot, 'flutter.docs'));
  final targetRoot = Directory(p.join(repoRoot, 'flutter.docs.cn'));
  if (!sourceRoot.existsSync() || !targetRoot.existsSync())
    throw StateError('缺少 flutter.docs/ 或 flutter.docs.cn/');
  final watch = Stopwatch()..start();
  final prefix = (args['page'] as String?)
      ?.replaceAll('\\', '/')
      .replaceFirst(RegExp(r'^flutter/'), '');
  if (prefix == null) {
    final cached = latestCachedManifest();
    if (cached != null &&
        cached['rule_version'] == ruleVersion &&
        cached['case_path_map_hash'] == pathMapHash()) {
      final currentSources = sourceFingerprints();
      final cachedPages = (cached['page_hashes'] as Map).keys.cast<String>();
      final currentTargets = targetFingerprints(cachedPages);
      final sourceUnchanged =
          sameFingerprintMap(cached['source_fingerprints'], currentSources);
      final targetsUnchanged =
          sameFingerprintMap(cached['target_fingerprints'], currentTargets);
      if (sourceUnchanged && !targetsUnchanged) {
        final workers = int.tryParse(args['workers']?.toString() ?? '') ??
            Platform.numberOfProcessors.clamp(1, 12);
        final incremental = await rescanChangedTargets(
            cached, currentSources, currentTargets, workers);
        if (incremental >= 0) return incremental;
      }
      if (sourceUnchanged && targetsUnchanged) {
        final elapsed = watch.elapsedMilliseconds;
        stdout.writeln(
            '输入未变化，复用快照 ${cached['run_id']}（$elapsed ms）；Markdown：${p.join(auditDir, 'runs', cached['run_id'] as String, 'report', 'index.md')}');
        return cached['has_issues'] == true ? 2 : 0;
      }
    }
  }
  final sourceFingerprintsBefore = sourceFingerprints();
  final inv = await inventory();
  var pages = (inv['pages'] as List).cast<String>();
  if (prefix != null)
    pages = pages
        .where((s) =>
            s.startsWith('flutter/$prefix') ||
            s == 'flutter/${prefix.replaceFirst(RegExp(r'/$'), '')}')
        .toList();
  if (pages.isEmpty) throw StateError('没有匹配到可扫描页面');
  final targetFingerprintsBefore = targetFingerprints(pages);
  final workers = int.tryParse(args['workers']?.toString() ?? '') ??
      Platform.numberOfProcessors.clamp(1, 12);
  if (workers < 1 || workers > 64) throw FormatException('--workers 范围为 1..64');
  final tasks = pages
      .map((logical) => <String, dynamic>{
            'page': logical,
            'repo_root': repoRoot,
            'source': sourcePath(logical),
            'target': targetPath(logical),
            'path_map': pathMap,
            if (archiveRequired.contains(logical))
              'source_markup': readSourceMarkup(logical),
          })
      .toList();
  final rows = await parallelScan(tasks, workers);
  final sourceFingerprintsAfter = sourceFingerprints();
  final targetFingerprintsAfter = targetFingerprints(pages);
  final inconsistentPages = <String>{
    for (final key in {
      ...sourceFingerprintsBefore.keys,
      ...sourceFingerprintsAfter.keys
    })
      if (sourceFingerprintsBefore[key] != sourceFingerprintsAfter[key]) key,
    for (final key in {
      ...targetFingerprintsBefore.keys,
      ...targetFingerprintsAfter.keys
    })
      if (targetFingerprintsBefore[key] != targetFingerprintsAfter[key]) key,
  }.toList()
    ..sort();
  final unitRows = <Map<String, dynamic>>[];
  for (final row in rows) {
    unitRows.addAll((row['units'] as List).cast<Map<String, dynamic>>());
  }
  final runId = DateTime.now()
      .toUtc()
      .toIso8601String()
      .replaceAll(':', '')
      .replaceAll('-', '')
      .replaceAll('.', '')
      .replaceAll('Z', 'Z');
  final runDir = Directory(p.join(auditDir, 'runs', runId))
    ..createSync(recursive: true);
  final allSourcePaths = (inv['pages'] as List).cast<String>();
  final manifest = {
    'run_id': runId,
    'created_at': DateTime.now().toUtc().toIso8601String(),
    'rule_version': ruleVersion,
    'case_path_map_hash': pathMapHash(),
    'scope': prefix == null ? '全站 API 文档' : '局部扫描: $prefix',
    'page_count': pages.length,
    'inventory_page_count': allSourcePaths.length,
    'missing_links': inv['missing_links'],
    'unreachable_pages': inv['unreachable'],
    'inconsistent_pages': inconsistentPages,
    'workers': workers,
    'source_bytes': rows.fold<int>(
        0,
        (n, r) =>
            n +
            (archiveSources.containsKey(r['page'])
                ? utf8.encode(archiveSources[r['page']]!).length
                : File(p.join(repoRoot, r['source_path'] as String))
                    .lengthSync())),
    'elapsed_ms': watch.elapsedMilliseconds,
    'page_hashes': {
      for (final r in rows) r['page']: [r['source_hash'], r['target_hash']]
    },
    'source_fingerprints': sourceFingerprintsAfter,
    'target_fingerprints': targetFingerprintsAfter,
    'has_issues': (inv['missing_links'] as List).isNotEmpty ||
        inconsistentPages.isNotEmpty ||
        rows.any((r) =>
            r['unaligned_units'] != 0 ||
            r['missing_units'] != 0 ||
            !r['target_exists']),
  };
  writeJson(p.join(runDir.path, 'manifest.json'), manifest);
  final reviews = readReviews();
  renderSummaryReport(runId, rows, reviews, manifest);
  for (final row in rows) {
    row.remove('units');
  }
  await writeJsonLines(p.join(runDir.path, 'pages.jsonl'), rows);
  await writeJsonLines(p.join(runDir.path, 'units.jsonl'), unitRows);
  watch.stop();
  manifest['elapsed_ms'] = watch.elapsedMilliseconds;
  writeJson(p.join(runDir.path, 'manifest.json'), manifest);
  final issues = manifest['has_issues'] == true;
  stdout.writeln(
      '运行 $runId：${pages.length} 页、${unitRows.length} 单元，${watch.elapsed.inSeconds} 秒。');
  if ((args['page'] as String?) != null) stdout.writeln('此结果为局部扫描，不代表全站进度。');
  return issues ? 2 : 0;
}

Future<void> exportReview(String runId, String? output) async {
  final run = readRun(runId);
  final pages = (run['pages'] as List).cast<Map<String, dynamic>>();
  aggregate(pages, readReviews());
  final path = output ?? p.join(auditDir, 'runs', runId, 'review.jsonl');
  final pending = <Map<String, dynamic>>[];
  for (final page in pages) {
    for (final unit in (page['units'] as List).cast<Map<String, dynamic>>()) {
      if (unit['review_status'] == 'pending') {
        pending.add({
          'run_id': runId,
          'unit_id': unit['unit_id'],
          'rule_version': unit['rule_version'],
          'page': unit['page'],
          'locator': unit['locator'],
          'source': unit['source'],
          'target': unit['target'],
          'source_hash': unit['source_hash'],
          'target_hash': unit['target_hash'],
          'structure_hash': unit['structure_hash'],
          'decision': '',
          'reason': ''
        });
      }
    }
  }
  File(path).parent.createSync(recursive: true);
  File(path).writeAsStringSync(pending.map(jsonEncode).join('\n') + '\n',
      encoding: utf8);
  stdout.writeln('已导出 ${pending.length} 条待审核单元：$path');
}

Future<void> importReview(String path) async {
  final lines = File(path)
      .readAsLinesSync(encoding: utf8)
      .where((s) => s.trim().isNotEmpty)
      .toList();
  final additions = <Map<String, dynamic>>[];
  final runCache = <String, Map<String, dynamic>>{};
  final seenUnits = <String>{};
  for (var i = 0; i < lines.length; i++) {
    final row = jsonDecode(lines[i]) as Map<String, dynamic>;
    final decision = row['decision'];
    if (!{'translated', 'reviewed', 'excluded'}.contains(decision))
      throw FormatException('第 ${i + 1} 行 decision 无效');
    if (decision == 'excluded' &&
        (row['reason'] as String? ?? '').trim().isEmpty)
      throw FormatException('第 ${i + 1} 行排除决定必须填写 reason');
    final runId = row['run_id'] as String?;
    if (runId == null) throw FormatException('第 ${i + 1} 行缺少 run_id');
    if (!seenUnits.add('$runId:${row['unit_id']}')) {
      throw FormatException('第 ${i + 1} 行重复导入同一单元');
    }
    final run = runCache.putIfAbsent(runId, () => readRun(runId));
    Map<String, dynamic>? unit;
    for (final page in (run['pages'] as List).cast<Map<String, dynamic>>()) {
      unit = (page['units'] as List)
          .cast<Map<String, dynamic>>()
          .where((u) => u['unit_id'] == row['unit_id'])
          .firstOrNull;
      if (unit != null) break;
    }
    if (unit == null ||
        unit['rule_version'] != ruleVersion ||
        row['rule_version'] != unit['rule_version'] ||
        unit['source_hash'] != row['source_hash'] ||
        unit['target_hash'] != row['target_hash'] ||
        unit['structure_hash'] != row['structure_hash'] ||
        unit['page'] != row['page'] ||
        unit['locator'] != row['locator'] ||
        unit['source'] != row['source'] ||
        unit['target'] != row['target']) {
      throw FormatException('第 ${i + 1} 行单元不存在或扫描快照哈希不匹配');
    }
    if (decision != 'excluded' &&
        ((unit['issues'] as List).isNotEmpty ||
            unit['auto_status'] == 'unaligned' ||
            (unit['auto_status'] as String).startsWith('missing'))) {
      throw FormatException('第 ${i + 1} 行存在完整性异常，只能修复后确认或以 excluded 记录理由');
    }
    final src = File(sourcePath(row['page'] as String));
    final dst = File(targetPath(row['page'] as String));
    if ((!src.existsSync() && !archiveSources.containsKey(row['page'])) ||
        sha(readSourceMarkup(row['page'] as String)) !=
            run['manifest']['page_hashes'][row['page']][0])
      throw FormatException('第 ${i + 1} 行原始页面已变化，请重新扫描');
    final targetHash =
        dst.existsSync() ? sha(dst.readAsStringSync(encoding: utf8)) : '';
    if (targetHash != run['manifest']['page_hashes'][row['page']][1])
      throw FormatException('第 ${i + 1} 行中文页面已变化，请重新扫描');
    additions.add({
      'run_id': runId,
      'unit_id': row['unit_id'],
      'decision': decision,
      'reason': row['reason'] ?? '',
      'rule_version': row['rule_version'],
      'source_hash': row['source_hash'],
      'target_hash': row['target_hash'],
      'structure_hash': row['structure_hash'],
      'recorded_at': DateTime.now().toUtc().toIso8601String()
    });
  }
  final out = File(p.join(auditDir, 'reviews.jsonl'))
    ..parent.createSync(recursive: true);
  final existingLines = out.existsSync()
      ? out
          .readAsLinesSync(encoding: utf8)
          .where((s) => s.trim().isNotEmpty)
          .toList()
      : <String>[];
  final temp = File('${out.path}.tmp');
  temp.writeAsStringSync(
      [...existingLines, ...additions.map(jsonEncode)].join('\n') +
          (additions.isEmpty ? '' : '\n'),
      encoding: utf8);
  replaceWithTemp(temp, out);
  stdout.writeln('已导入 ${additions.length} 条确认记录。');
}

extension FirstOrNull<E> on Iterable<E> {
  E? get firstOrNull => isEmpty ? null : first;
}

Future<void> main(List<String> rawArgs) async {
  final scriptDir = Directory(p.dirname(Platform.script.toFilePath()));
  repoRoot = p.normalize(p.join(scriptDir.path, '..', '..', '..'));
  translationDir = p.join(repoRoot, '.translation');
  auditDir = p.join(translationDir, 'audit');
  final mappingFile = File(p.join(translationDir, 'case-paths.json'));
  pathMap = mappingFile.existsSync()
      ? jsonDecode(mappingFile.readAsStringSync(encoding: utf8))
          as Map<String, dynamic>
      : <String, dynamic>{};
  try {
    final args = parseArgs(rawArgs);
    final positional = (args['_'] as List<String>);
    if (args['help'] == true || positional.isEmpty) {
      usage();
      return;
    }
    final command = positional.first;
    if (command == 'scan') {
      loadCaseSourceOverrides();
      exitCode = await runScan(args);
    } else if (command == 'report') {
      final runId = args['run'] as String? ??
          (throw FormatException('report 需要 --run RUN_ID'));
      if (args['full'] == true) {
        await renderReport(runId);
      } else {
        final index =
            File(p.join(auditDir, 'runs', runId, 'report', 'index.md'));
        if (!index.existsSync()) {
          throw FormatException('该快照没有汇总报告，请重新扫描或使用 --full');
        }
        stdout.writeln('Markdown 汇总：${index.path}');
        stdout.writeln('如需逐页单元详情，请添加 --full。');
      }
    } else if (command == 'export-review') {
      final runId = args['run'] as String? ??
          (throw FormatException('export-review 需要 --run RUN_ID'));
      await exportReview(runId, args['out'] as String?);
    } else if (command == 'import-review') {
      loadCaseSourceOverrides();
      await importReview(args['file'] as String? ??
          (throw FormatException('import-review 需要 --file FILE')));
    } else {
      throw FormatException('未知命令: $command');
    }
  } on FormatException catch (e) {
    stderr.writeln('参数或数据错误：${e.message}');
    exitCode = 1;
  } catch (e, st) {
    stderr.writeln('执行失败：$e');
    stderr.writeln(st);
    exitCode = 1;
  }
}
