import unittest
from src.blocks.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "# This is a heading"
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, ["# This is a heading"])

    def test_multiple_blocks(self):
        markdown = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])

    def test_empty_lines(self):
        markdown = (
            "\n\n"
            "# This is a heading\n\n"
            "\nThis is a paragraph of text.\n\n"
            "\n* This is a list item\n\n"
        )
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# This is a heading",
            "This is a paragraph of text.",
            "* This is a list item"
        ])

    def test_no_blocks(self):
        markdown = "   \n   \n"  # Only whitespace and newlines
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [])  # Should return an empty list

    def test_leading_and_trailing_whitespace(self):
        markdown = (
            "   # This is a heading   \n\n"
            "   This is a paragraph.   \n\n"
            "* This is a list item   "
        )
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# This is a heading",
            "This is a paragraph.",
            "* This is a list item"
        ])

if __name__ == "__main__":
    unittest.main()
