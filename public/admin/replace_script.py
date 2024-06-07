import os

def replace_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)

def replace_in_md_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, '{}', '[]')
                print(f'Replaced in: {file_path}')

if __name__ == "__main__":
    src_directory = '/src'  # Replace this with your actual source directory
    replace_in_md_files(src_directory)
