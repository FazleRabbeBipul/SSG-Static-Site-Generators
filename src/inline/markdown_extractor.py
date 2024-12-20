import re

def extract_markdown_images(text):
    """
    Extracts images from markdown text.
    
    Args:
        text (str): Raw markdown text containing images.
        
    Returns:
        list: A list of tuples where each tuple contains the alt text and the image URL.
    """
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_pattern, text)
    return matches
