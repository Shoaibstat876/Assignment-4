# 🛍️ 02 - Pop-Up Shop

### 📌 Problem Statement:
You’re shopping at a local fruit stand and want to calculate how much your basket will cost.  
This program loops through a dictionary of fruits with prices, asks how many of each fruit you want to buy, and calculates the total cost.

---

### ✅ Steps:
- A dictionary stores each fruit with its **price per unit**  
- For every fruit:
  - Prompt the user: **"How many (fruit) do you want to buy?"**  
  - Multiply the quantity by the unit price  
  - Add that to a running `total_cost`  
- Print the final total after all items are processed

---

### 💡 Output Example:

How many (apple) do you want?: 2
How many (durian) do you want?: 0
How many (jackfruit) do you want?: 1
How many (kiwi) do you want?: 0
How many (rambutan) do you want?: 1
How many (mango) do you want?: 3

Your total is $99.5


---

### 🧠 Key Concepts:
- **Dictionaries** are used to store item-price mappings  
- **Looping through keys** lets us prompt for each item  
- Calculations are done on-the-fly using `total += price × quantity`

---

### 👨‍💻 Developer Notes:
- The program is flexible — you can easily add more fruits or update prices  
- Great practice for combining `input()`, `for` loops, and `dict` usage  
- Output is clean and user-friendly — like a self-checkout machine!

---
