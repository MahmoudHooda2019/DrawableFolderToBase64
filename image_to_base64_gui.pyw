import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox

def sanitize_filename(filename):
    name, ext = os.path.splitext(filename)
    name = name.replace("-", "_").replace(" ", "_")
    ext = ext.replace(".", "_")
    return f"{name}{ext}"

def encode_images_to_base64(folder_path):
    supported_extensions = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp")
    result_lines = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_extensions):
            full_path = os.path.join(folder_path, filename)
            try:
                with open(full_path, "rb") as img_file:
                    encoded = base64.b64encode(img_file.read()).decode('utf-8')
                    variable_name = sanitize_filename(filename)
                    result_lines.append(f'public static final String {variable_name} = "{encoded}";')
            except Exception as e:
                print(f"Error encoding {filename}: {e}")

    return "\n".join(result_lines)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Image Folder")
    if not folder_path:
        return

    output = encode_images_to_base64(folder_path)

    if not output:
        messagebox.showinfo("Done", "No supported images found in the selected folder.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".java",
        filetypes=[("Java files", "*.java"), ("All files", "*.*")],
        title="Save Base64 Output as..."
    )

    if save_path:
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(output)
            messagebox.showinfo("Success", f"Base64 output saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Image to Base64 (Java Const Generator)")
root.geometry("420x200")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Convert folder of images to Base64 Java constant strings",
    wraplength=380,
    pady=20
)
label.pack()

button = tk.Button(root, text="Select Folder", command=select_folder, width=25, height=2)
button.pack(pady=10)

root.mainloop()
