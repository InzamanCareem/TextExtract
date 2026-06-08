import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import os
import sys
import easyocr
import numpy as np


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class TextExtract:
    def __init__(self, root):
        self.root = root
        self.root.title("TextExtract")
        self.root.iconbitmap(resource_path("icon.ico"))
        self.root.geometry("600x600")

        self.image_frame = tk.Frame(root, width=400, height=200, relief="groove", bd=2)
        self.image_frame.pack(pady=10)
        self.image_frame.pack_propagate(False)

        self.image_label = tk.Label(self.image_frame, text="Upload or Paste an Image")
        self.image_label.pack(fill="both", expand=True)

        self.status_label = tk.Label(root, fg="red")
        self.status_label.pack(pady=5)

        tk.Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)

        tk.Button(root, text="Paste Image (Ctrl+V)", command=self.paste_image).pack(pady=5)

        root.bind("<Control-v>", lambda event: self.paste_image())

        tk.Label(root, text="Text:").pack(pady=(10, 0))

        self.text_box = tk.Text(root, width=50, height=10)
        self.text_box.pack(pady=5)

        tk.Button(root, text="Copy Text", command=self.copy_text).pack(pady=5)

        self.reader = easyocr.Reader(['en'], verbose=False)

    def display_image(self, img):
        original_img = img.copy()
        original_img = original_img.convert("L")

        display_img = img.copy()
        display_img.thumbnail((400, 200))

        self.photo = ImageTk.PhotoImage(display_img)
        self.image_label.config(image=self.photo)

        text = self.grab_text_from_image(original_img)
        # text = " ".join(text)
        print(text)

        self.text_box.delete("1.0", tk.END)
        self.text_box.insert("1.0", text)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.webp")])

        if file_path:
            try:
                img = Image.open(file_path)
                self.display_image(img)
                self.set_status("Image loaded successfully!", "green")
            except Exception as e:
                self.set_status(f"Upload error: {e}")

    def paste_image(self):
        try:
            img = ImageGrab.grabclipboard()

            if isinstance(img, Image.Image):
                self.display_image(img)
                self.set_status("Image loaded successfully!", "green")
            else:
                self.set_status("No image found in clipboard.")

        except Exception as e:
            self.set_status(f"Error pasting image: {e}")

    def set_status(self, message, color="red"):
        self.status_label.config(text=message, fg=color)

    def grab_text_from_image(self, img):
        result = self.reader.readtext(np.array(img), detail=1, paragraph=True, contrast_ths=0.1, adjust_contrast=0.5,
                                      text_threshold=0.75, low_text=0.4, link_threshold=0.4, mag_ratio=2)

        print(result)
        result = sorted(result, key=lambda x: x[0][0][1])
        text = " ".join([r[1] for r in result])
        return text

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_box.get("1.0", tk.END).strip())
        self.root.update()


root = tk.Tk()
app = TextExtract(root)
root.mainloop()
