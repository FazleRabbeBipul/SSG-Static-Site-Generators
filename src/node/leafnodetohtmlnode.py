from enum import Enum
from src.node.leafnodehtml import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text_type, text, url=None, alt_text=None):
        self.text_type = text_type
        self.text = text
        self.url = url
        self.alt_text = alt_text

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK TextNode must have a URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.alt_text:
            raise ValueError("IMAGE TextNode must have a URL and alt text.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt_text})

    else:
        raise ValueError("Unsupported TextType.")
