import unittest
from ejpcsvparser import utils


class TestUtils(unittest.TestCase):
    def test_allowed_tags(self):
        self.assertIsNotNone(utils.allowed_tags(), "allowed_tags not returned")

    def test_entity_to_unicode(self):
        passes = []
        passes.append(
            (
                "N-terminal &#x03B1;-helix into the heterodimer interface",
                "N-terminal \u03b1-helix into the heterodimer interface",
            )
        )

        passes.append(
            (
                "N-terminal &alpha;-helix into the heterodimer interface",
                "N-terminal \u03b1-helix into the heterodimer interface",
            )
        )

        passes.append(
            (
                (
                    "&#x00A0; &#x00C5; &#x00D7; &#x00EF; &#x0394; &#x03B1; &#x03B2; &#x03B3; &#x03BA; "
                    + "&#x03BB; &#x2212; &#x223C; &alpha; &amp; &beta; &epsilon; &iuml; &ldquo; &ordm; "
                    + "&rdquo;"
                ),
                (
                    "\xa0 \xc5 \xd7 \xef \u0394 \u03b1 \u03b2 \u03b3 \u03ba \u03bb \u2212 \u223c "
                    + '\u03b1 &amp; \u03b2 \u03b5 \xcf " \xba "'
                ),
            )
        )

        for string_input, string_output in passes:
            self.assertEqual(utils.entity_to_unicode(string_input), string_output)

    def test_escape_angle_brackets(self):
        passes = []
        passes.append((None, None))
        passes.append((0, 0))
        passes.append(
            (
                "N-terminal &#x03B1;-helix into the heterodimer interface",
                "N-terminal &#x03B1;-helix into the heterodimer interface",
            )
        )
        passes.append(("<i>i</i>", "&lt;i&gt;i&lt;/i&gt;"))
        for string_input, string_output in passes:
            self.assertEqual(utils.escape_angle_brackets(string_input), string_output)

    def test_get_elife_doi(self):
        article_id = 3
        expected = "10.7554/eLife.00003"
        self.assertEqual(utils.get_elife_doi(article_id), expected)
