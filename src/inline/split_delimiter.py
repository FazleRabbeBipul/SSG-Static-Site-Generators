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
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
