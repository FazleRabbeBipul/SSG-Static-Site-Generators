class HTMLNode:
    def __init__(self, tag=None, value=None, attributes=None):
        self.tag = tag
        self.value = value
        self.attributes = attributes if attributes else {}
        self.children = []

    def to_html(self):
        raise NotImplementedError("This method should be implemented in subclasses")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, attributes)
        self.children = None  # Ensures no children are allowed

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")

        # Render as raw text if tag is None
        if self.tag is None:
            return self.value

        # Render with attributes if present
        attr_str = "".join(f' {key}="{value}"' for key, value in self.attributes.items())

        # Self-closing tags like <img>
        if self.tag in {"img", "br", "hr", "input"}:
            return f"<{self.tag}{attr_str}>"

        # Normal tags with content
        return f"<{self.tag}{attr_str}>{self.value}</{self.tag}>"

# Example tests
def test_leaf_node():
    # Test basic rendering
    leaf = LeafNode("p", "This is a paragraph of text.")
    assert leaf.to_html() == "<p>This is a paragraph of text.</p>"

    # Test attributes
    link = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    assert link.to_html() == '<a href="https://www.google.com">Click me!</a>'

    # Test raw text rendering
    raw_text = LeafNode(None, "This is raw text.")
    assert raw_text.to_html() == "This is raw text."

    # Test error on no value
    try:
        LeafNode("p", None)
    except ValueError as e:
        assert str(e) == "LeafNode must have a value."
    else:
        assert False, "ValueError not raised for missing value"

    print("All tests passed!")

# Run tests
test_leaf_node()
