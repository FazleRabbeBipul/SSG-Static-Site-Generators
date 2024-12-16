from leafnodehtml import HTMLNode, LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if children is None or not isinstance(children, list):
            raise ValueError("ParentNode must have children as a list.")
        
        super().__init__(tag, None, attributes)
        self.children = children

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to render.")
        
        children_html = ''.join(child.to_html() for child in self.children)
        attr_str = ''.join(f' {key}="{value}"' for key, value in self.attributes.items())
        return f"<{self.tag}{attr_str}>{children_html}</{self.tag}>"

# Example tests
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

# Run tests
test_parent_node()
