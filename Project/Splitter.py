import tkinter as tk
from tkinter import filedialog, messagebox
import os

def split_file(input_file, output_folder, lines_per_file):
    file_count = 0
    line_count = 0
    output_file = None

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
            for line in infile:
                if line_count % lines_per_file == 0:
                    if output_file:
                        output_file.close()
                    output_file_path = os.path.join(output_folder, f"{os.path.basename(input_file)}_part{file_count}.txt")
                    output_file = open(output_file_path, 'w', encoding='utf-8')
                    file_count += 1
                output_file.write(line)
                line_count += 1

        if output_file:
            output_file.close()
        messagebox.showinfo("Success", "File split successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {input_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_file():
    input_file = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if input_file:
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            lines_per_file = lines_per_file_entry.get()
            if lines_per_file.isdigit() and int(lines_per_file) > 0:
                split_file(input_file, output_folder, int(lines_per_file))
            else:
                messagebox.showerror("Error", "Please enter a valid number of lines per file.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Splitter")

    tk.Label(root, text="Lines per File:").pack(pady=5)
    lines_per_file_entry = tk.Entry(root)
    lines_per_file_entry.pack(pady=5)

    tk.Button(root, text="Select File to Split", command=select_file).pack(pady=20)

    root.mainloop()
