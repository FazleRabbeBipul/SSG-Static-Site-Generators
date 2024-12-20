import re
from src.inline.link_extractor import extract_markdown_links
from src.node.textnode import TextNode, TextType

def split_nodes_link(old_nodes):
    """
    Splits a list of TextNode objects based on link markdown into multiple TextNode objects.
    
    Args:
        old_nodes (list): A list of TextNode objects.
        
    Returns:
        list: A new list of TextNode objects, split as necessary.
    """
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            # Non-text nodes are passed through unchanged
            new_nodes.append(node)
            continue
        
        # Extract links using the regex extractor
        links = extract_markdown_links(node.text)
        
        if not links:
            # No links found, just append the original node
            new_nodes.append(node)
            continue
        
        # Split the text based on links
        last_end = 0
        for anchor_text, link_url in links:
            # Split the text before the link
            before_link = node.text[last_end:node.text.find(f"[{anchor_text}]({link_url})")]
            if before_link:
                new_nodes.append(TextNode(before_link, TextType.NORMAL_TEXT))
            
            # Create a new TextNode for the link itself
            new_nodes.append(TextNode(anchor_text, TextType.LINK, link_url))
            
            # Update the last position after the link
            last_end = node.text.find(f"[{anchor_text}]({link_url})") + len(f"[{anchor_text}]({link_url})")
        
        # Add the remaining text after the last link
        if last_end < len(node.text):
            new_nodes.append(TextNode(node.text[last_end:], TextType.NORMAL_TEXT))
    
    return new_nodes
