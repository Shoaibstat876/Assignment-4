# 📅 03 - Leap Year

### 📌 Problem Statement:
Write a program that asks the user to enter a **year**, and then tells whether it is a **leap year** or **not**, based on the official rules of the **Gregorian calendar**.

---

### 🧠 Leap Year Rules (Gregorian Calendar):

A year is a leap year if:

- It is **divisible by 4**, and  
  - Not divisible by **100**, unless  
    - It is also divisible by **400**

---

### ✅ Steps:
- Prompt the user to input a year  
- Use nested `if` statements to check leap year logic  
- Print `"That's a leap year!"` or `"That's not a leap year."` accordingly

---

### 💡 Output Examples:

Please input a year: 2024
That's a leap year!

Please input a year: 1900
That's not a leap year.

Please input a year: 2000
That's a leap year!


---

### 👨‍💻 Developer Notes:
- Used nested conditionals to follow **priority rules** of leap years  
- Applied `%` modulus operator for checking divisibility  
- No external libraries or date packages needed  
- A great practice in **mathematical conditions and logic nesting**

---
