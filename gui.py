import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from epub_editor import edit_epub_metadata


class EPUBMetadataEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("EPUB Metadata Editor")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Sans', '10'))
        self.style.configure('TLabel', font=('Sans', '10'))
        self.style.configure('TEntry', font=('Sans', '10'))

        self.create_widgets()

        self.epub_file = None

    def create_widgets(self):
        # File Selection
        ttk.Label(self.master, text="Select EPUB File:").grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        file_button = ttk.Button(self.master, text="Browse", command=self.select_epub_file)
        file_button.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="ew")
        self.file_label = ttk.Label(self.master, text="No file selected", font=('Sans', '8', 'italic'))
        self.file_label.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")

        # Title Entry
        ttk.Label(self.master, text="New Title:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.title_entry = ttk.Entry(self.master)
        self.title_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Author Entry
        ttk.Label(self.master, text="New Author:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.author_entry = ttk.Entry(self.master)
        self.author_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Update Button
        update_button = ttk.Button(self.master, text="Update Metadata", command=self.submit_changes)
        update_button.grid(row=3, column=1, pady=20)

        # Status Label
        self.status_label = ttk.Label(self.master, text="", font=('Sans', '8'))
        self.status_label.grid(row=4, column=0, columnspan=3, pady=(5, 20))

    def select_epub_file(self):
        self.epub_file = filedialog.askopenfilename(title="Open EPUB File", filetypes=[("EPUB files", "*.epub")])
        if self.epub_file:
            self.file_label.config(text=f"Selected: {self.epub_file}")

    def submit_changes(self):
        new_title = self.title_entry.get()
        new_author = self.author_entry.get()
        if self.epub_file and new_title and new_author:
            try:
                edit_epub_metadata(self.epub_file, new_title, new_author)
                self.status_label.config(text="Metadata updated successfully!", foreground='green')
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            self.status_label.config(text="Please fill out all fields and select a file.", foreground='red')


def run_app():
    root = tk.Tk()
    app = EPUBMetadataEditorApp(root)
    root.mainloop()