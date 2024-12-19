import unittest
from src.node.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            tag="div",
            value="Hello, World!",
            children=[],
            props={"class": "container"}
        )
        expected_repr = ("HTMLNode(tag='div', value='Hello, World!', "
                         "children=[], props={'class': 'container'})")
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
