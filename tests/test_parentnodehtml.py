import unittest
from src.node.parentnodehtml import ParentNode, LeafNode

def test_parent_node():
    # Test basic rendering
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
    )
    assert node.to_html() == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

    # Test nested ParentNodes
    nested_node = ParentNode(
        "div",
        [
            ParentNode(
                "p",
                [LeafNode("b", "Nested Bold"), LeafNode(None, "Nested Text")]
            ),
            LeafNode("span", "Span Text")
        ]
    )
    assert nested_node.to_html() == "<div><p><b>Nested Bold</b>Nested Text</p><span>Span Text</span></div>"

    # Test error for missing tag
    try:
        ParentNode(None, [])
    except ValueError as e:
        assert str(e) == "ParentNode must have a tag."
    else:
        assert False, "ValueError not raised for missing tag"

    # Test error for missing children
    try:
        ParentNode("div", None)
    except ValueError as e:
        assert str(e) == "ParentNode must have children as a list."
    else:
        assert False, "ValueError not raised for missing children"

    print("All ParentNode tests passed!")

if __name__ == "__main__":
    unittest()