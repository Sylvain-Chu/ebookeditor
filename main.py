import os
from ebooklib import epub


def list_epub_files(directory):
    """
    List all EPUB files in the specified directory.
    """
    return [file for file in os.listdir(directory) if file.endswith('.epub')]


def edit_epub_metadata(epub_file, new_title=None, new_author=None):
    # Load the EPUB file
    book = epub.read_epub(epub_file)

    # Replace the existing title if a new title is provided
    if new_title:
        book.metadata['http://purl.org/dc/elements/1.1/'].pop('title', None)
        book.set_title(new_title)

    # Replace existing authors if a new author is provided
    if new_author:
        book.metadata['http://purl.org/dc/elements/1.1/'].pop('creator', None)
        book.add_author(new_author)

    # Build a new file name with the prefix 'modified_'
    directory, filename = os.path.split(epub_file)
    new_filename = 'modified_' + filename
    new_file_path = os.path.join(directory, new_filename)

    # Save the modifications in a new file
    epub.write_epub(new_file_path, book)

    return new_file_path


def read_epub_metadata(epub_file):
    book = epub.read_epub(epub_file)

    titles = book.get_metadata('DC', 'title')
    authors = book.get_metadata('DC', 'creator')

    print("Title(s):")
    for title in titles:
        print(title[0])

    print("Author(s):")
    for author in authors:
        print(author[0])


def main():
    directory = input("Enter the path of the folder containing your EPUB files: ")

    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    epub_files = list_epub_files(directory)

    if not epub_files:
        print("No EPUB files found in the specified directory.")
        return

    print("EPUB Files Found:")
    for idx, file in enumerate(epub_files, 1):
        print(f"{idx}. {file}")

    try:
        choice = int(input("Enter the number of the EPUB file you wish to modify: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice < 0 or choice >= len(epub_files):
        print("Invalid file number.")
        return

    selected_file = epub_files[choice]

    new_title = input("Enter the new title (leave blank if no change): ")
    new_author = input("Enter the new author (leave blank if no change): ")

    try:
        modified_file = edit_epub_metadata(os.path.join(directory, selected_file), new_title, new_author)
        print(f"Modified file saved as: {modified_file}")
        read_epub_metadata(modified_file)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
