import os
import shutil
import tempfile

def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "fc_build")
    shutil.copytree(path, temp_path)
    return temp_path

def clean_items(where):
    def check(arr):
        for item in arr:
            if item.startswith('.'):
                continue
            if not item.startswith('__'):
                continue
            print("removing " + os.path.join(root, item))
            shutil.rmtree(os.path.join(root, item))
    for root, dirs, files in os.walk(where):
        check(dirs)
        check(files)

def create_resource_pack():
    temp_path = create_temporary_copy("./src")
    clean_items(temp_path)
    shutil.make_archive('froscraft-resource-pack', 'zip', temp_path)
    shutil.rmtree(temp_path)
   

if __name__ == "__main__":
    print("Creating resource pack.")
    create_resource_pack()
    print("Completed.")
