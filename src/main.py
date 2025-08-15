import os

from copy_static import copy_static, clear_public
from generate_page import generate_page, generate_page_recursive

dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    clear_public()
    copy_static()
    
    # generate_page(
    #     os.path.join(dir_path_content, 'index.md'),
    #     template_path,
    #     os.path.join(dir_path_public, 'index.html'),
    # )
    
    generate_page_recursive(dir_path_content, template_path, dir_path_public)
    
    # generate_page(
    #     os.path.join(dir_path_content, 'blog/glorfindel/index.md'),
    #     template_path,
    #     os.path.join(dir_path_public, 'blog/glorfindel/index.html'),
    # )
    
    # generate_page(
    #     os.path.join(dir_path_content, 'blog/tom/index.md'),
    #     template_path,
    #     os.path.join(dir_path_public, 'blog/tom/index.html'),
    # )
    
    # generate_page(
    #     os.path.join(dir_path_content, 'blog/majesty/index.md'),
    #     template_path,
    #     os.path.join(dir_path_public, 'blog/majesty/index.html'),
    # )
    
    # generate_page(
    #     os.path.join(dir_path_content, 'contact/index.md'),
    #     template_path,
    #     os.path.join(dir_path_public, 'contact/index.html'),
    # )
    
if __name__ == "__main__":
    main()