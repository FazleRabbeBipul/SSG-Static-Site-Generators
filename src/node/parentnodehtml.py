from src.node.leafnodehtml import HTMLNode, LeafNode

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
