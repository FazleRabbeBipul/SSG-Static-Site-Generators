from src.node.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits nodes based on a given delimiter into multiple TextNodes.

    Args:
        old_nodes (list): List of TextNode objects to process.
        delimiter (str): The delimiter to split by (e.g., "**", "*", "`").
        text_type (TextType): The type to assign to text between delimiters.

    Returns:
        list: A new list of TextNode objects, split as necessary.

    Raises:
        ValueError: If a delimiter is unmatched in the text.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            # Non-text nodes are passed through unchanged
            new_nodes.append(node)
            continue

        # If the text is empty, return the node as is
        if node.text == "":
            new_nodes.append(TextNode("", TextType.NORMAL_TEXT))
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        for i, part in enumerate(parts):
            if i % 2 == 0:  # Outside delimiters
                if part:
                    new_nodes.append(TextNode(part, TextType.NORMAL_TEXT))
            else:  # Inside delimiters
                if part:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes
