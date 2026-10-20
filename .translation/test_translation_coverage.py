import unittest

from translation_coverage import analyze, evidence, tree_report, units


def page(text):
    return '<section class="desc markdown">' + text + '</section>'


class CoverageTests(unittest.TestCase):
    def test_scope_and_nested_blocks(self):
        markup = '<nav>Ignore this</nav>' + page('<ul><li>List <p>nested prose</p></li></ul>'
                 '<p>A <code>code words</code> <a href="x">Widget</a> works.</p>') + '<dd>Summary words</dd>'
        result = units(markup)
        self.assertEqual([k for k, _ in result], ['li', 'p', 'dd'])
        self.assertEqual(result[0][1], 'List nested prose')
        self.assertEqual(result[1][1], 'A works.')

    def test_verified_and_partial_word_weights(self):
        stats, details = analyze([('p', 'First sentence. Second sentence.')],
                                 [('p', '第一句。 Second sentence.')], [('First sentence.', '第一句。')])
        self.assertEqual(stats['source_words'], 4)
        self.assertEqual(stats['mapped_words'], 2)
        self.assertEqual(stats['partial_units'], 1)
        # A stale mapping cannot receive coverage merely because it exists.
        stale, _ = analyze([('p', 'First sentence.')], [('p', 'First sentence.')], [('First sentence.', '第一句。')])
        self.assertEqual(stale['mapped_words'], 0)
        self.assertEqual(stale['uncovered_units'], 1)

    def test_overlap_not_double_counted(self):
        stats, _ = analyze([('p', 'First sentence.')], [('p', '第一句。')],
                           [('First sentence.', '第一句。'), ('First', '第一')])
        self.assertEqual(stats['mapped_words'], 2)
        self.assertEqual(stats['mapped_units'], 1)

    def test_misalignment_not_shifted(self):
        stats, details = analyze([('p', 'Four ordinary English words.')], [('li', '四个英文词。')],
                                 [('Four ordinary English words.', '四个英文词。')])
        self.assertEqual(stats['alignment_mismatch_pages'], 1)
        self.assertEqual(stats['mapped_words'], 0)
        self.assertIsNone(details[0]['target'])

    def test_mapping_and_fragment_evidence(self):
        pairs = evidence(page('<p>First sentence.</p>'), 'x.html',
                         {'x.html': {'0': '<p>第一句。</p>'}}, {}, {})
        self.assertIn(('First sentence.', '第一句。'), pairs)

    def test_tree_uses_weighted_totals(self):
        tree = tree_report([dict(page='flutter/a/one.html', source_words=10, mapped_words=10),
                            dict(page='flutter/a/sub/two.html', source_words=90, mapped_words=0)])
        self.assertEqual(tree['totals']['weighted_mapping_percent'], 10)
        self.assertEqual(tree['totals']['page_count'], 2)
        self.assertEqual(tree['children'][0]['name'], 'a')


if __name__ == '__main__':
    unittest.main()
