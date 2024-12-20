import unittest
from src.inline.text_to_textnodes import text_to_textnodes
from src.node.textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "This is plain text"
        expected = [TextNode("This is plain text", TextType.NORMAL_TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_bold_text(self):
        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_image_and_link(self):
        text = "An image ![alt text](https://example.com/image.jpg) and a [link](https://example.com)"
        expected = [
            TextNode("An image ", TextType.NORMAL_TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()
