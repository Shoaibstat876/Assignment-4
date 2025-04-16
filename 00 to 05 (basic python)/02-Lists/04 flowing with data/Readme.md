# 🔄 04 - Flowing With Data (Mutability)

### 📌 Problem Statement:
Explore how **mutable data types** (like lists) behave inside functions.  
This program demonstrates that changes made to a list inside a function **persist** even if nothing is returned — unlike immutable types like numbers or strings.

---

### ✅ Steps:
- Prompt the user to enter a message
- Create an empty list called `my_list`
- Pass the list and message to a function `add_three_copies(...)`
- Inside the function, add the message to the list three times using `.append()`
- Print the list before and after the function call

---

### 💡 Output Example:

Enter a message to copy: Hello world! List before: [] List after: ['Hello world!', 'Hello world!', 'Hello world!']


---

### 🧠 Key Concepts:
- **Lists are mutable** → changes inside a function affect the original list  
- No need to return the list — it’s updated automatically by reference  
- This is different from how **numbers (immutable)** work in functions

---

### 👨‍💻 Developer Notes:
- Practiced modifying a list inside a helper function  
- Used `.append()` to demonstrate mutation  
- Used `print()` to show before/after state of the list  
- Reinforced key Python behavior about **data mutability**

---
