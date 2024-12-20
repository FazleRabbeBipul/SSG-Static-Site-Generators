import unittest
from src.node.textnode import TextNode, TextType
from src.inline.split_node_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![image alt text](https://i.imgur.com/sample.jpg)",
            TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
            TextNode("image alt text", TextType.IMAGE, "https://i.imgur.com/sample.jpg")
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_images(self):
        node = TextNode("This is text without any images", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()
