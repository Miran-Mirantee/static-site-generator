from enum import Enum
import re
from htmlnode import ParentNode, LeafNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    return [
        "\n".join(line.strip() for line in block.strip().split("\n"))
        for block in markdown.split("\n\n")
        if block.strip() != ""
    ]
    
def block_to_block_type(block: str) -> BlockType:
    if bool(re.match(r"^#{1,6}\s+.+", block)):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(part.startswith(">") for part in block.split("\n")):
        return BlockType.QUOTE
    elif all(part.startswith("- ") for part in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(bool(re.match(r"^\d+\.\s", part)) for part in block.split("\n")):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children = block_to_children(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_nodes.append(ParentNode("p", children))
            case BlockType.HEADING:
                level = block.count("#")
                html_nodes.append(ParentNode(f"h{level}", children))
            case BlockType.CODE:
                html_nodes.append(ParentNode("pre", [ParentNode("code", children)]))
            case BlockType.QUOTE:
                html_nodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                html_nodes.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                html_nodes.append(ParentNode("ol", children))

    return ParentNode("div", html_nodes)

def block_to_text(block: str, block_type: BlockType) -> list[str]:
    match block_type:
        case BlockType.PARAGRAPH:
            return [block.replace("\n", " ")]
        case BlockType.HEADING:
            return [re.match(r"^#+\s+(.+)", block.replace("\n", " ")).group(1)]
        case BlockType.CODE:
            return [block.replace("```", "").lstrip()]
        case BlockType.QUOTE:
            return [" ".join(
                re.match(r"^>\s*(.*)$", item).group(1)
                for item in block.split("\n")
            )]
        case BlockType.UNORDERED_LIST:
            return [re.match(r"^-\s+(.+)", item).group(1) for item in block.split("\n")]
        case BlockType.ORDERED_LIST:
            return [re.match(r"^\d+\.\s+(.+)", item).group(1) for item in block.split("\n")]

def block_to_children(block: str) -> list[LeafNode]:
    block_type = block_to_block_type(block)
    text_list = block_to_text(block, block_type)
    text_nodes = []
    html_nodes = []
    
    if block_type == BlockType.CODE:
        return [LeafNode("", text_list[0])]
    
    if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
        for text in text_list:
            text_nodes = text_to_textnodes(text)
            html_nodes.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_nodes]))
            
        return html_nodes
    
    for text in text_list:
        text_nodes.extend(text_to_textnodes(text))
        
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
        
    return html_nodes