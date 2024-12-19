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