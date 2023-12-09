import os


def folder_structure(directory):
    structure = {}

    for root, dirs, files in os.walk(directory):
        current_level = structure
        folders = root.split(os.sep)[1:]

        for folder in folders:
            current_level = current_level.setdefault(folder, {})

    return structure


# Example usage:
directory_path = "/path/to/your/directory"
result = folder_structure(directory_path)
print(result)
