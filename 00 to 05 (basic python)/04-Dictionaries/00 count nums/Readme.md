# 🔢 00 - Count Nums

### 📌 Problem Statement:
Create a program that asks the user to enter numbers **one at a time**.  
When the user presses **Enter without typing anything**, the program should display how many times **each number** was entered using a **dictionary**.

---

### ✅ Steps:
- Use a `while` loop to collect numbers into a list  
- Create an empty dictionary to store counts  
- Loop through the list:
  - If a number is not in the dictionary → add it with a value of 1  
  - If it's already in the dictionary → increment its count  
- Print the final counts for each number

---

### 💡 Output Example:

Enter a number: 3
Enter a number: 4
Enter a number: 3
Enter a number: 6
Enter a number: 4
Enter a number: 3
Enter a number: 12
Enter a number:

3 appears 3 times.
4 appears 2 times.
6 appears 1 times.
12 appears 1 times.


---

### 🧠 Key Concepts:
- **Dictionaries** store key-value pairs — perfect for counting  
- `.get()` or `if...in` logic handles dynamic keys  
- Demonstrates user input, list handling, and dictionary manipulation

---

### 👨‍💻 Developer Notes:
- Separated the logic into clean helper functions (`get_user_numbers`, `count_nums`, `print_counts`)  
- Used **integers** for counting and list building  
- Scalable structure — can be adapted for word counting, vote tallies, etc.

---
