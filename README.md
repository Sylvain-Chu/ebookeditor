
# Ebook Metadata Editor

## Overview
This Python project provides a simple command-line interface to edit the metadata of EPUB files. It allows users to modify the title and author of any EPUB file within a specified directory.

## Features
- List all EPUB files in a specified directory.
- Select an EPUB file to edit.
- Modify the title and/or author of the selected EPUB file.
- Save the modified file as a new EPUB file, preserving the original.
- Display the updated metadata of the modified file.

## How to Use
1. Place the EPUB files in a directory.
2. Run the script and enter the path of the directory.
3. The script will list all EPUB files in the directory.
4. Enter the number corresponding to the file you want to modify.
5. Enter the new title and/or author for the file (leave blank if no changes are needed).
6. The script will create a modified version of the EPUB file with your changes.

## Requirements
- Python 3
- EbookLib: A Python library for managing EPUB2/EPUB3 files.

## Installation
Ensure you have Python 3 installed. Then, install EbookLib using pip:
```
pip install EbookLib
```

## Script File Description
- `main.py`: The main script that you run to start the editing process.

## Limitations
- The script currently does not support editing other metadata fields like publisher, publication date, etc.
- Only works with EPUB files.

## Future Enhancements
- Add support for editing additional metadata fields.
- Improve error handling and user feedback.
- Develop a graphical user interface for easier use.

---

This project is a simple tool for ebook enthusiasts and professionals who need to modify EPUB file metadata quickly and easily.
