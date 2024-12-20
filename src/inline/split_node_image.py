import re
from src.inline.markdown_extractor import extract_markdown_images
from src.node.textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    """
    Splits a list of TextNode objects based on image markdown into multiple TextNode objects.
    
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
        
        # Extract images using the regex extractor
        images = extract_markdown_images(node.text)
        
        if not images:
            # No images found, just append the original node
            new_nodes.append(node)
            continue
        
        # Split the text based on images
        last_end = 0
        for alt_text, image_url in images:
            # Split the text before the image
            before_image = node.text[last_end:node.text.find(f"![{alt_text}]({image_url})")]
            if before_image:
                new_nodes.append(TextNode(before_image, TextType.NORMAL_TEXT))
            
            # Create a new TextNode for the image itself
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            
            # Update the last position after the image
            last_end = node.text.find(f"![{alt_text}]({image_url})") + len(f"![{alt_text}]({image_url})")
        
        # Add the remaining text after the last image
        if last_end < len(node.text):
            new_nodes.append(TextNode(node.text[last_end:], TextType.NORMAL_TEXT))
    
    return new_nodes
