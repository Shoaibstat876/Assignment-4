# 🎲 04 - Random Numbers

### 📌 Problem Statement:
Write a Python program that prints **10 random numbers** between **1 and 100** (inclusive). The results should differ each time the program is run.

---

### ✅ Steps:
- Import the `random` module
- Define constants for how many numbers to generate and their range
- Loop 10 times using `range(N_NUMBERS)`
- In each iteration, generate a random number using `random.randint()`
- Print the numbers on the same line

---

### 💡 Output Example:
45 79 61 47 52 10 16 83 19 12


---

### 👨‍💻 Developer Notes:
- Used `random.randint(MIN, MAX)` for number generation
- Controlled output format with `print(..., end=" ")` for inline printing
- Constants improve code readability and maintainability

---
