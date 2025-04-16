# 📤 07 - Print Divisors

### 📌 Problem Statement:
Write a helper function `print_divisors(num)` that prints **all the divisors** of a given number.  
A divisor is a number that divides the input with **no remainder**.

---

### ✅ Steps:
- Prompt the user to enter a number using `input()`  
- Pass that number to `print_divisors(num)`  
- Inside `print_divisors`, loop from 1 to `num`  
- For each number, check if it divides `num` cleanly using `%`  
- Print all divisors line by line

---

### 💡 Output Example:

Enter a number: 12
Here are the divisors of 12
1
2
3
4
6
12


---

### 🧠 Key Concepts:
- Loops (`for i in range(...)`)  
- Arithmetic condition: `num % divisor == 0`  
- Clean output and formatting  
- Good intro to helper function design

---

### 👨‍💻 Developer Notes:
- This is a great example of **reusability with helper functions**  
- You can reuse `print_divisors()` in prime checking or GCD logic later  
- Try extending this to print **only even divisors** or **count the total divisors**

---
