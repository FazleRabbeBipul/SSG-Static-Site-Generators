import unittest
from src.node.leafnodehtml import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_basic_rendering(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_attributes_rendering(self):
        link = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(link.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_raw_text_rendering(self):
        raw_text = LeafNode(None, "This is raw text.")
        self.assertEqual(raw_text.to_html(), "This is raw text.")

    def test_missing_value_error(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "LeafNode must have a value.")

if __name__ == "__main__":
    unittest.main()
