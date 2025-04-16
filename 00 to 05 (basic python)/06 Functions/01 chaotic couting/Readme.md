# 🌀 01 - Chaotic Counting

### 📌 Problem Statement:
Create a program that prints the numbers from 1 to 10, but with a twist: before printing each number, the program will decide at random whether to continue counting or stop.  
The program uses a helper function, `done()`, that returns `True` with a probability defined by `DONE_LIKELIHOOD` (set to 0.2 in this case).  
If `done()` returns `True`, the function exits early; otherwise, it prints the current number. After the loop or early exit, the program prints `"I'm done"`.

---

### ✅ Steps:
- Import the `random` module to generate randomness  
- Define a constant `DONE_LIKELIHOOD` (0.2, meaning a 20% chance to stop)  
- In the `chaotic_counting()` function:
  - Loop through numbers 1 to 10 using a `for` loop  
  - For each number:
    - Call `done()` to randomly decide whether to stop  
    - If `done()` returns `True`, exit the loop immediately using `return`  
    - Otherwise, print the number
- In the `main()` function:
  - Print an introductory message  
  - Call `chaotic_counting()`  
  - After the function finishes, print `"I'm done"`

---

### 💡 Output Example:

One possible run:


I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done


---

### 🧠 Key Concepts:
- **While loops and control flow:** Using a loop to repeatedly check a condition  
- **Randomness:** Using `random.random()` and a probability threshold (`DONE_LIKELIHOOD`) to introduce unpredictability  
- **Early exit:** Utilizing `return` to exit a function before the loop completes

---

### 👨‍💻 Developer Notes:
- This exercise shows how to mix loops with random stopping conditions, making each run potentially unique  
- The use of a helper function (`done()`) improves code readability and separation of logic  
- Great for learning how to control flow in unpredictable or event-driven scenarios

---
