def markdown_to_blocks(markdown: str) -> list[str]:
    return list(map(lambda x: "\n".join(list(map(lambda y: y.strip(), x.strip().split("\n")))), markdown.split("\n\n")))