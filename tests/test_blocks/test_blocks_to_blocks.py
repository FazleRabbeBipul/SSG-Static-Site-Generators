import unittest
from src.blocks.blocks_to_blocks import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    # Existing test cases...

    def test_invalid_ordered_list(self):
        invalid_ordered_list = "1. Item 1\n3. Item 3\n5. Item 5"
        self.assertEqual(block_to_block_type(invalid_ordered_list), "paragraph")  # Not sequential

    def test_heading_with_space(self):
        valid_heading = "### Heading"
        self.assertEqual(block_to_block_type(valid_heading), "heading")

    def test_inline_code_paragraph(self):
        inline_code = "This is a paragraph with `inline code`."
        self.assertEqual(block_to_block_type(inline_code), "paragraph")

    def test_code_block(self):
        code_block = "```\ndef example():\n    return True\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

    def test_ordered_list(self):
        ordered_list = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ordered_list), "ordered_list")