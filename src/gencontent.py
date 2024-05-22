import os
from markdown_blocks import extract_title, markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    with open(from_path) as m:
        markdown = m.read()
    
    with open(template_path) as t:
        template = t.read()

    title = extract_title(markdown)
    all_html = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", all_html)

    with open(dest_path, 'w') as n:
        n.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        html_dest_path = os.path.join(dest_dir_path, "index.html")
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {html_dest_path}")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, html_dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

    