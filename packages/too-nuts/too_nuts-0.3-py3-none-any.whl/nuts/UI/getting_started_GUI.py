"""Welcome page for GUI.

.. autosummary::

   load_markdown_file
   getting_started

"""

from pathlib import Path

import streamlit as st


def load_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def getting_started(UI_path: Path, NuTS_path: Path) -> None:
    md_file_path = UI_path / "README_GUI.md"
    md_content = load_markdown_file(md_file_path)
    st.markdown(md_content)
