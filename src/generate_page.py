import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """Extract the first heading from the markdown content."""
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return "Untitled"

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r', encoding='utf-8') as from_file:
        content = from_file.read()
        
    with open(template_path, 'r', encoding='utf-8') as from_file:
        template = from_file.read()
    
    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()
    title = extract_title(content)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace("{{ Title }}", title)
    
    paths = os.path.dirname(dest_path)
    os.makedirs(paths, exist_ok=True)
    
    with open(dest_path, 'w', encoding='utf-8') as to_file:
        to_file.write(template)
    
    