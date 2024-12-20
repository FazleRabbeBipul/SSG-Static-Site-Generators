import re

def extract_markdown_links(text):
    """
    Extracts links from markdown text.
    
    Args:
        text (str): Raw markdown text containing links.
        
    Returns:
        list: A list of tuples where each tuple contains the anchor text and the link URL.
    """
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    return matches
