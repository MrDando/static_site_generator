import os
import shutil

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    title = list(filter(lambda line: line.startswith("# "), markdown.split("\n")))

    return title


def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    with open(template_path, 'r') as f:
        template_string = f.read()

    dir_list = os.listdir(from_path)

    for item in dir_list:
        item_path = os.path.join(from_path, item)
        if os.path.isfile(item_path):
            md_path = os.path.join(dest_path, item)
            html_path = md_path.replace("md", "html")
            generate_page(item_path, html_path, template_string)
        else:
            new_from_path = os.path.join(from_path, item)
            new_dest_path = os.path.join(dest_path, item)
            generate_pages_recursive(new_from_path, template_path, new_dest_path)

def generate_page(item_path, html_path, template_string):
    with open(item_path, 'r') as f:
        markdown_string = f.read()

    html_content = markdown_to_html_node(markdown_string).to_html()
    title = extract_title(markdown_string)[0][1:].strip()

    html_file = template_string.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    f = open(html_path, "w")
    f.write(html_file)
    f.close()

# def generate_page(from_path, template_path, dest_path):
#     print(f"Generating page from {from_path} to {dest_path} using {template_path}")

#     with open(from_path, 'r') as f:
#         markdown_string = f.read()

#     with open(template_path, 'r') as f:
#         template_string = f.read()

    
#     html_content = markdown_to_html_node(markdown_string).to_html()
#     title = extract_title(markdown_string)[0][1:].strip()

#     html_file = template_string.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
#     f = open(dest_path, "w")
#     f.write(html_file)
#     f.close()