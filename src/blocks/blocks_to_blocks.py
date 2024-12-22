import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def block_to_block_type(block):
    """
    Determines the type of a Markdown block.

    :param block: A single block of stripped Markdown text.
    :return: A string representing the type of the block (e.g., "heading", "paragraph", etc.).
    """
    

    # Split the block into lines
    lines = block.split("\n")

    # Heading: Starts with 1-6 # characters followed by a space
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    
    # Code block: Starts and ends with 3 backticks on separate lines
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    
    # Quote block: Every line starts with >
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    # Unordered list: Every line starts with * or - followed by a space
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    
    # Ordered list: Every line starts with a number followed by . and a space
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph