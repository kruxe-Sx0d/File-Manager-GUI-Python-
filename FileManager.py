import os
import shutil
import easygui
from tkinter import filedialog, messagebox, Button, Tk, Label


def select_file():
    """Open a file selection dialog and return the path."""
    return easygui.fileopenbox()


def select_directory():
    """Open a directory selection dialog and return the path."""
    return filedialog.askdirectory()


def open_file():
    """Open a selected file using the OS default handler."""
    path = select_file()
    if not path:
        return
    try:
        os.startfile(path)
    except Exception:
        messagebox.showerror("Error", "Unable to open file.")


def copy_file():
    """Copy a file to a selected directory."""
    source = select_file()
    destination = select_directory()
    if not source or not destination:
        return

    try:
        shutil.copy(source, destination)
        messagebox.showinfo("Success", "File copied successfully.")
    except Exception:
        messagebox.showerror("Error", "File copy failed.")


def delete_file():
    """Delete a selected file."""
    path = select_file()
    if not path:
        return

    try:
        os.remove(path)
        messagebox.showinfo("Success", "File deleted successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to delete file.")


def rename_file():
    """Rename a selected file."""
    file_path = select_file()
    if not file_path:
        return

    directory = os.path.dirname(file_path)
    extension = os.path.splitext(file_path)[1]
    new_name = input("Enter new name: ")

    if not new_name:
        messagebox.showerror("Error", "Invalid name.")
        return

    new_path = os.path.join(directory, new_name + extension)

    try:
        os.rename(file_path, new_path)
        messagebox.showinfo("Success", "File renamed successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to rename file.")


def move_file():
    """Move a file to another directory."""
    source = select_file()
    destination = select_directory()
    if not source or not destination:
        return

    if os.path.dirname(source) == destination:
        messagebox.showerror("Error", "Source and destination are the same.")
        return

    try:
        shutil.move(source, destination)
        messagebox.showinfo("Success", "File moved successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to move file.")


def create_directory():
    """Create a new folder inside a selected directory."""
    base_path = select_directory()
    if not base_path:
        return

    name = input("Enter directory name: ")
    if not name:
        messagebox.showerror("Error", "Invalid directory name.")
        return

    full_path = os.path.join(base_path, name)

    try:
        os.mkdir(full_path)
        messagebox.showinfo("Success", "Directory created successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to create directory.")


def remove_directory():
    """Remove a selected directory."""
    path = select_directory()
    if not path:
        return

    try:
        os.rmdir(path)
        messagebox.showinfo("Success", "Directory removed successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to remove directory.")


def list_files():
    """List all files inside a selected directory."""
    path = select_directory()
    if not path:
        return

    try:
        files = sorted(os.listdir(path))
        print("Files in directory:")
        for f in files:
            print(f)
    except Exception:
        messagebox.showerror("Error", "Unable to list files.")


# GUI window setup
window = Tk()
window.title("File Manager")
window.configure(bg="black")
window.geometry("300x400")

Label(window, text="Select an Action:", fg="white", bg="black").pack(pady=10)

Button(window, command=open_file, text="Open File",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=copy_file, text="Copy File",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=delete_file, text="Delete File",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=rename_file, text="Rename File",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=move_file, text="Move File",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=create_directory, text="Create Directory",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=remove_directory, text="Remove Directory",
       fg="blue", bg="white").pack(pady=3)

Button(window, command=list_files, text="List Files",
       fg="blue", bg="white").pack(pady=3)

window.mainloop()

