# 📸 TextExtract (Image OCR Tool)

TextExtract is a simple Python desktop application that allows you to **upload or paste images** and automatically extract text from them using OCR (Tesseract). You can then copy the extracted text with one click.

---

## 🚀 Features

- 📁 Upload images from your computer  
- 📋 Paste images directly from clipboard (Ctrl + V)  or using the paste button
- 🔍 Extract text using Tesseract OCR  
- 🖼️ Preview uploaded images  
- 📋 Copy extracted text instantly  
- 🪟 Simple and lightweight Tkinter GUI  

---

## 🧠 How It Works

SnapText uses:
- **Tkinter** → for the graphical interface  
- **Pillow (PIL)** → for image processing  
- **pytesseract** → for OCR text extraction  

---

## 📦 Installation

1. Download `TextExtract.zip` from the latest release.
2. Extract the ZIP file to any folder.
3. Run `TextExtract.exe`.

No installation is required.

## Building from Source

### 1. Clone the repository
```bash
git clone https://github.com/InzamanCareem/TextExtract.git
cd TextExtract
```

### 2. Create Virtual Environment

```bash
uv venv venv
```

### 3. Activate Environment

#### Windows

```bash
.\venv\Scripts\activate.bat
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
uv sync
```

### 5. Install Tesseract OCR

Download and install from: https://github.com/tesseract-ocr/tesseract

Put the entire tesseract folder inside the `TextExtract` folder.
Make sure to rename the folder to `tesseract`.


### ▶️ Run the App

```bash
uv run python main.py
```

### 🖥️ How to Use

- Click Upload Image or press Ctrl + V to paste an image
- The image will be displayed in the app
- Text will be automatically extracted
- Click Copy Text to copy it to clipboard


## 📌 Notes
Works best with clear, high-resolution images
OCR accuracy depends on image quality
First launch may take slightly longer due to library loading


## 📄 License

This project is open-source and free to use.
