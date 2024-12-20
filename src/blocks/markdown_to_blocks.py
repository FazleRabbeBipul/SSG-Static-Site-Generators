def markdown_to_blocks(markdown):
    """
    Splits the raw Markdown string into distinct block strings.
    
    Parameters:
        markdown (str): The raw Markdown document as a string.

    Returns:
        list: A list of block strings with leading/trailing whitespace removed.
    """
    # Split markdown by two or more newlines (blank lines separate blocks)
    blocks = markdown.split("\n\n")
    
    # Strip leading/trailing whitespace and remove empty blocks
    blocks = [block.strip() for block in blocks if block.strip()]
    
    return blocks
