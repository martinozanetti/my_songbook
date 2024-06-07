import os

def create_latex_in_current_directory(output_file):
    current_directory = os.getcwd()  # Get the current working directory
    with open(output_file, 'w') as tex_file:
        for dir_name in sorted(os.listdir(current_directory)):
            if dir_name == '.git':  # Skip the .git folder
                continue
            dir_path = os.path.join(current_directory, dir_name)
            if os.path.isdir(dir_path):
                tex_file.write(f'\\chapter{{{dir_name}}}\n')
                for file_name in sorted(os.listdir(dir_path)):
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path) and file_name.endswith(".txt"):
                        file_base, _ = os.path.splitext(file_name)
                        tex_file.write(f'\\section{{{file_base}}}\n')
                        relative_file_path = os.path.join(dir_name, file_name).replace("\\", "/")
                        tex_file.write(f'\\VerbatimInput{{{relative_file_path}}}\n')
                tex_file.write("\n")

# Example usage
create_latex_in_current_directory('body.tex')
