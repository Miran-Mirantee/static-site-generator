from textnode import TextNode, TextType


def main():
    textNode = TextNode(TextType.LINK, 'imgay', "https://www.boot.dev")
    print("Hello, World!")
    print(textNode)
    
if __name__ == "__main__":
    main()