# ✨ 02 - Count Even

### 📌 Problem Statement:
Write a program that:
1. **Collects a list of integers** from the user  
2. **Counts and prints how many of them are even**

---

### ✅ Steps:
- Use a helper function `get_list_of_ints()` to prompt for user input until Enter is pressed  
- Define a function `count_even(lst)` to count the even numbers using a loop  
- Display the total count of even numbers

---

### 💡 Output Example:

Enter an integer or press enter to stop: 2 Enter an integer or press enter to stop: 5 Enter an integer or press enter to stop: 8 Enter an integer or press enter to stop: 2


> In the above run, there are 2 even numbers: `2` and `8`

---

### 🧠 Key Concepts:
- **List construction** from user input  
- Use of **modulus operator (`%`)** to detect even numbers  
- Separation of input logic and processing logic using **functions**  
- Clean iteration using `for num in lst`

---

### 👨‍💻 Developer Notes:
- The even-checking logic (`num % 2 == 0`) is reusable  
- Try enhancing it to also return the **list of even numbers**  
- Great for practicing **looping + conditionals + function reuse**

---
