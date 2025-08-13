from textnode import TextNode, TextType
from util import split_nodes_delimiter


def main():
    # textNode = TextNode('imgay', TextType.LINK, "https://www.boot.dev")
    # print("Hello, World!")
    # print(textNode)
    node = TextNode("This is text with a `code block` word **bold** `cz` `what` `exactly`", TextType.TEXT)
    node2 = TextNode("`code block`", TextType.TEXT)
    node3 = TextNode("This is an _italic and **bold** word_.", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node, node2, node3], "_", TextType.ITALIC)
    print(new_nodes)
    
if __name__ == "__main__":
    main()