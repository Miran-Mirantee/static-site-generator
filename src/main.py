from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link


def main():
    # textNode = TextNode('imgay', TextType.LINK, "https://www.boot.dev")
    # print("Hello, World!")
    # print(textNode)
    # node = TextNode("This is text with a `code block` word **bold** `cz` `what` `exactly`", TextType.TEXT)
    # node2 = TextNode("`code block`", TextType.TEXT)
    # node3 = TextNode("This is an _italic and **bold** word_.", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node, node2, node3], "_", TextType.ITALIC)
    # print(new_nodes)
    # node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_image([node])
    node = TextNode(
        "![image](https://www.example.COM/IMAGE.PNG)",
        TextType.TEXT,
    )
    node_link = TextNode(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        TextType.TEXT,
    )
    # new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link([node_link])
    print(new_nodes)
    
if __name__ == "__main__":
    main()