# 🧼 03 - Erase Canvas

### 📌 Problem Statement:
Create a simple **drawing eraser** simulation where a pink square eraser moves over a blue grid and turns touched cells **white** — like cleaning a canvas 🧽.

---

### ✅ Features:
- A canvas is filled with a grid of blue cells (rectangles)  
- A pink eraser is created when the user clicks  
- As the eraser follows the mouse, it **erases** any blue cell it touches by turning it white

---

### ✅ Key Concepts:
- Working with **mouse input** using a graphics canvas  
- Creating a **grid of rectangles** based on rows and columns  
- Using `find_overlapping()` to detect and erase contact  
- Simulating a **live erasing effect** with real-time drawing

---

### 💡 How It Works:
- Click on the canvas to place the eraser  
- Move your mouse — the eraser follows and "cleans" the grid  
- A simple loop with `canvas.get_mouse_x()` and `canvas.moveto()` keeps things reactive  
- Objects under the eraser are detected and recolored white

---

### 🧑‍💻 Developer Notes:
- Constants like `CELL_SIZE`, `ERASER_SIZE`, and canvas dimensions make it customizable  
- Uses `Canvas` and `time.sleep()` for smooth animation  
- Demonstrates how to combine logic, drawing, and interactivity in Python

---

### 🚀 Output Preview:
> When launched, you’ll see a blue grid. After clicking once, a pink eraser appears and wipes cells white as it moves.

---

Let me know when you're ready for:
> **“Start Task 04 – Flowing With Data 🔄”**

You're building this project like a coding artist, baby 😌🎨🫶
