# 🔢 01 - Fibonacci

### 📌 Problem Statement:
Write a program to display the **Fibonacci sequence** — a famous number pattern where each number is the sum of the two before it — starting from `0` and stopping before it exceeds **10,000**.

The sequence starts like this:
0 1 1 2 3 5 8 13 21 34 ..


---

### ✅ Steps:
- Set a constant `MAX_TERM_VALUE = 10000`  
- Start with two initial terms:
  - `curr_term = 0`
  - `next_term = 1`  
- Use a `while` loop to keep generating the next term:
  - Print the current number
  - Calculate the next number as the sum of the last two  
  - Update values and repeat until `curr_term > MAX_TERM_VALUE`

---

### 💡 Output Example:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


---

### 🧠 Key Concepts:
- **Fibonacci sequence**: `Fib(n) = Fib(n-1) + Fib(n-2)`  
- **While loop** keeps running until the sequence exceeds 10,000  
- Controlled variable updates to move through the series

---

### 👨‍💻 Developer Notes:
- Used a `while` loop for continuous calculation  
- Optimized output to display neatly in one line  
- Excellent use of variable tracking and iteration logic  
- Can be modified to print *n* terms, or accept user input in the future!

---
