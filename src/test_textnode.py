import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test when two TextNode objects are identical
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node1, node2)

    def test_inequality_different_text(self):
        # Test inequality when text properties are different
        node1 = TextNode("Text node 1", TextType.BOLD_TEXT)
        node2 = TextNode("Text node 2", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

    def test_inequality_different_text_type(self):
        # Test inequality when text_type properties are different
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node1, node2)

    def test_equality_with_url(self):
        # Test equality with the optional `url` parameter
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, url="https://example.com")
        self.assertEqual(node1, node2)

    def test_default_url(self):
        # Test default value of `url`
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()
