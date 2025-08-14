from enum import Enum
import re

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
