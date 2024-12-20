import unittest
from src.node.textnode import TextNode, TextType
from src.inline.split_node_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [BootDev](https://www.boot.dev) and [YouTube](https://www.youtube.com)",
            TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("BootDev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("YouTube", TextType.LINK, "https://www.youtube.com")
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_links(self):
        node = TextNode("This is text without any links", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()
