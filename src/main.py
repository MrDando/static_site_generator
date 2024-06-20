import os
import shutil

from website_generator import (
    generate_pages_recursive
)

def main():

    public_exists = os.path.exists("./public")
    if public_exists:
        shutil.rmtree("./public")

    copy_folder("static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

def copy_folder(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    dir_list = os.listdir(source_path)
    
    for item in dir_list:
        if os.path.isfile(f"{source_path}/{item}"):
            shutil.copy(f"{source_path}/{item}", f"{dest_path}/{item}")
        else:
            new_source_path = f"{source_path}/{item}"
            new_dest_path = f"{dest_path}/{item}"
            os.mkdir(new_dest_path)
            copy_folder(new_source_path, new_dest_path)


main()