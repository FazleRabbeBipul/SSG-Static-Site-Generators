from textnode import TextNode, TextType

if __name__ == "__main__":
    node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(node)
