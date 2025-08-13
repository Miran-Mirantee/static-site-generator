from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("matching closing delimiter is not found")
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        parts = extract_markdown_images(node.text)
        curr_text = node.text
        for part in parts:
            sections = curr_text.split(f"![{part[0]}]({part[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(part[0], TextType.IMAGE, part[1]))
            curr_text = sections[1]
        if curr_text:
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes
    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        parts = extract_markdown_links(node.text)
        curr_text = node.text
        for part in parts:
            sections = curr_text.split(f"[{part[0]}]({part[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(part[0], TextType.LINK, part[1]))
            curr_text = sections[1]
        if curr_text:
            new_nodes.append(TextNode(curr_text, TextType.TEXT))
    return new_nodes
