import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """Extract the first heading from the markdown content."""
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return "Untitled"
    
def generate_page_recursive(from_path: str, template_path: str, dest_path: str, basepath: str):
    children = os.listdir(from_path)
    if not children:
        return
    for child in children:
        if os.path.isfile(os.path.join(from_path, child)):
            with open(os.path.join(from_path, child), 'r', encoding='utf-8') as from_file:
                content = from_file.read()
                
            with open(template_path, 'r', encoding='utf-8') as from_file:
                template = from_file.read()
    
            html_node = markdown_to_html_node(content)
            html_content = html_node.to_html()
            title = extract_title(content)
            template = template.replace("{{ Content }}", html_content)
            template = template.replace("{{ Title }}", title)
            template = template.replace('href="/', f'href="{basepath}')
            template = template.replace('src="/', f'src="{basepath}')
            
            os.makedirs(dest_path, exist_ok=True)
    
            with open(os.path.join(dest_path, child.replace('md', 'html')), 'w', encoding='utf-8') as to_file:
                to_file.write(template)
        else:
            generate_page_recursive(
                os.path.join(from_path, child),
                template_path,
                os.path.join(dest_path, child),
                basepath
            )
    