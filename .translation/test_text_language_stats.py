import unittest

from text_language_stats import ProseParser, counts, ratios


class TextStatsTests(unittest.TestCase):
    def test_scope_entities_nested_summary_and_code(self):
        parser = ProseParser()
        parser.feed('<nav>Navigation</nav><section class="markdown desc">'
                    '<p>中文 <a href="English">Hello</a> &amp; &#x6587;'
                    '<code>ignored</code></p><dd>摘要</dd>'
                    '<script>ignored</script></section><dd>Summary</dd>')
        text = parser.text()
        self.assertEqual(text, '中文 Hello & 文\n摘要\nSummary')
        self.assertEqual(counts(text)['chinese_chars'], 5)
        self.assertEqual(counts(text)['english_letters'], 12)

    def test_body_scope_and_include_code(self):
        parser = ProseParser('body', True)
        parser.feed('<dd>Outside</dd><section class="desc markdown">'
                    '<p>中<code>API</code></p></section>')
        self.assertEqual(parser.text(), '中API')

    def test_empty_and_supplementary_han(self):
        self.assertIsNone(ratios(counts('123 &'))['chinese_percent'])
        result = ratios(counts('𠀀中ab!'))
        self.assertEqual(result['chinese_percent'], 50)
        self.assertEqual(result['english_percent'], 50)


if __name__ == '__main__':
    unittest.main()
