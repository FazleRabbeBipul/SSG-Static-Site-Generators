import unittest
from src.node.textnode import TextNode, TextType
from src.inline.split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_case(self):
        node = TextNode("This is **bold** text", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_matches(self):
        node = TextNode("This is **bold** and **strong** text", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("strong", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("No special formatting here", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [TextNode("No special formatting here", TextType.NORMAL_TEXT)]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold and unclosed", TextType.NORMAL_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

    def test_mixed_delimiters(self):
        node = TextNode("This is **bold** and *italic* text", TextType.NORMAL_TEXT)
        # First, process **bold** delimiters, then process *italic* delimiters
        result = split_nodes_delimiter(
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT),
            "*",
            TextType.ITALIC_TEXT
        )
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_empty_text(self):
        node = TextNode("", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [TextNode("", TextType.NORMAL_TEXT)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
