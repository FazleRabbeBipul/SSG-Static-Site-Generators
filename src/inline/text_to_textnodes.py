from src.inline.split_node_image import split_nodes_image
from src.inline.split_node_link import split_nodes_link
from src.inline.split_delimiter import split_nodes_delimiter
from src.node.textnode import TextNode, TextType

def text_to_textnodes(text):
    # Start with the whole text wrapped in a normal text node
    nodes = [TextNode(text, TextType.NORMAL_TEXT)]
    
    # Apply the splitting functions in order
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    
    return nodes
