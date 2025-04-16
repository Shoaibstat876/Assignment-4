# 🎯 05 - Get First Element

### 📌 Problem Statement:
Write a function that takes in a list and **prints the first element**.  
The list is built using user input — one element at a time — and is guaranteed to be non-empty.

---

### ✅ Steps:
- Prompt the user repeatedly to enter list items (until they press Enter)  
- Store the items in a list using a helper function `get_lst()`  
- Call `get_first_element(lst)` to print the first element using `lst[0]`

---

### 💡 Output Example:

Please enter an element of the list or press enter to stop. Apple
Please enter an element of the list or press enter to stop. Banana
Please enter an element of the list or press enter to stop. Mango
Please enter an element of the list or press enter to stop.
Apple


---

### 🧠 Key Concepts:
- **Indexing in lists starts from 0**  
- `lst[0]` gives the very first item  
- Demonstrates basic list input and access patterns

---

### 👨‍💻 Developer Notes:
- Used a while loop to dynamically build a list  
- No need for `.split()` or bulk input — added item-by-item  
- Printed the first element without returning anything  
- A great warm-up for list traversal and input gathering

---
