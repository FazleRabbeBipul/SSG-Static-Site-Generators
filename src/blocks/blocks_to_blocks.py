import re

def block_to_block_type(block):
    """
    Determines the type of a Markdown block.

    :param block: A single block of stripped Markdown text.
    :return: A string representing the type of the block (e.g., "heading", "paragraph", etc.).
    """
    # Split the block into lines
    lines = block.split("\n")

    # Code block: Starts and ends with 3 backticks on separate lines
    if len(lines) >= 2 and lines[0] == "```" and lines[-1] == "```":
        return "code"

    # Heading: Starts with 1-6 # characters followed by a space
    if re.match(r"^#{1,6} ", block):
        return "heading"

    # Quote block: Every line starts with >
    if all(line.startswith(">") for line in lines):
        return "quote"

    # Unordered list: Every line starts with * or - followed by a space
    if all(line.startswith(("* ", "- ")) for line in lines):
        return "unordered_list"

    # Ordered list: Every line starts with a number followed by . and a space
    if all(re.match(r"^\d+\. ", line) for line in lines):
        try:
            # Validate that the numbers are sequential
            numbers = [int(re.match(r"^(\d+)\. ", line).group(1)) for line in lines]
            if numbers == list(range(1, len(numbers) + 1)):
                return "ordered_list"
        except ValueError:
            pass

    # Inline code block: Contains `inline code`
    if "`" in block and block.count("`") % 2 == 0:
        return "paragraph"  # Inline code blocks are part of a paragraph

    # If none of the above, it's a paragraph
    return "paragraph"
