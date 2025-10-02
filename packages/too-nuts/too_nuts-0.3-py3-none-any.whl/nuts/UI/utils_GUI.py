"""Utils functions fo GUI.

.. autosummary::

   load_markdown_file
   load_toml_file
   save_toml_file

"""

import toml


# Function to load markdown files
def load_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


# Function to load a TOML file
def load_toml_file(file_path):
    return toml.load(file_path)


# Function to save changes to a TOML file
def save_toml_file(file_path, data):
    with open(file_path, "w") as file:
        toml.dump(data, file)
