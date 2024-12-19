import unittest
from src.node.leafnodetohtmlnode import TextNode, text_node_to_html_node, TextType


def test_text_node_to_html_node():
    # Test TEXT
    text_node = TextNode(TextType.TEXT, "Just some text")
    assert text_node_to_html_node(text_node).to_html() == "Just some text"

    # Test BOLD
    bold_node = TextNode(TextType.BOLD, "Bold text")
    assert text_node_to_html_node(bold_node).to_html() == "<b>Bold text</b>"

    # Test ITALIC
    italic_node = TextNode(TextType.ITALIC, "Italic text")
    assert text_node_to_html_node(italic_node).to_html() == "<i>Italic text</i>"

    # Test CODE
    code_node = TextNode(TextType.CODE, "print('Hello, World!')")
    assert text_node_to_html_node(code_node).to_html() == "<code>print('Hello, World!')</code>"

    # Test LINK
    link_node = TextNode(TextType.LINK, "OpenAI", url="https://www.openai.com")
    assert text_node_to_html_node(link_node).to_html() == '<a href="https://www.openai.com">OpenAI</a>'

    # Test IMAGE
    image_node = TextNode(TextType.IMAGE, "", url="https://example.com/image.jpg", alt_text="Example Image")
    assert text_node_to_html_node(image_node).to_html() == '<img src="https://example.com/image.jpg" alt="Example Image">'

    # Test invalid LINK without URL
    try:
        invalid_link_node = TextNode(TextType.LINK, "Invalid Link")
        text_node_to_html_node(invalid_link_node)
    except ValueError as e:
        assert str(e) == "LINK TextNode must have a URL."

    # Test invalid IMAGE without URL or alt text
    try:
        invalid_image_node = TextNode(TextType.IMAGE, "", alt_text="Missing URL")
        text_node_to_html_node(invalid_image_node)
    except ValueError as e:
        assert str(e) == "IMAGE TextNode must have a URL and alt text."

    print("All tests passed!")
    

if __name__ == "__main__":
    unittest.main()