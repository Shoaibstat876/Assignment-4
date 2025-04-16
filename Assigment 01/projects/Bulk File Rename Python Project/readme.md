# 📁 Bulk File Re-namer Python Project

This is a simple Python script that allows you to **rename multiple files in bulk** with a consistent prefix. It's especially useful when organizing folders filled with unstructured or randomly named files.

---

## 🚀 Features

- Rename all files in a directory
- Add a custom prefix like `photo_`, `doc_`, `file_`, etc.
- Auto-numbered files (e.g. `file_1.jpg`, `file_2.jpg`, etc.)
- Supports all file types (PDFs, JPGs, TXT, etc.)

---

## 🧠 How It Works

1. The script asks for the folder path where the files are located.
2. You provide a **prefix** that will be used in the renamed files.
3. It loops through all files in the folder and renames them using your prefix and an index.

---

## 🔧 Example

**Before:**
dog.jpg randomfile.png notes.txt


**Input:**
Folder path: D:/Images Prefix: vacation


**After:**
vacation_1.jpg vacation_2.png vacation_3.txt


---

## 🛠 Requirements

- Python 3.x
- No additional libraries needed (uses built-in `os` module)

---

## ▶️ How to Run

```bash
python main.py


Use Cases
Renaming hundreds of images from a camera roll

Organizing downloaded documents

Resetting file names for a clean backup

Preparing datasets for ML models

❤️ Made With Python
Quick utility with huge time-saving potential — tidy your digital workspace in seconds!


---

Let me know when you're ready to move on to the **Weather Info**, **Timer**, or the next project in your list 😌📦
