import os
import shutil

def copy_static():
    shutil.rmtree('public', ignore_errors=True)
    os.mkdir('public')
    copy_static_recursive()
        
def copy_static_recursive(old_path: str = 'static'):
    paths = os.listdir(old_path)
    for path in paths:
        joined_path = os.path.join(old_path, path)
        if os.path.isdir(joined_path):
            copy_static_recursive(joined_path)
        elif os.path.isfile(joined_path):
            new_path = old_path.replace('static', 'public', 1)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            shutil.copy(joined_path, new_path)
            