import os
import shutil

def clear_build(path: str):
    shutil.rmtree(path, ignore_errors=True)
    os.mkdir(path)

def copy_static(from_path: str = 'static', to_path: str = 'docs'):
    copy_static_recursive(from_path, to_path)
        
def copy_static_recursive(from_path: str, to_path: str):
    paths = os.listdir(from_path)
    for path in paths:
        joined_path = os.path.join(from_path, path)
        if os.path.isdir(joined_path):
            copy_static_recursive(joined_path, to_path)
        elif os.path.isfile(joined_path):
            new_path = from_path.replace('static', to_path, 1)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            shutil.copy(joined_path, new_path)
            