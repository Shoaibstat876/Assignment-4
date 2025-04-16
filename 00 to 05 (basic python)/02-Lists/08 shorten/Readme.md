# ✂️ 08 - Shorten

### 📌 Problem Statement:
Create a function that removes elements from the **end of a list** until the list contains only a maximum of `MAX_LENGTH` items.  
The removed elements should be printed one by one.

---

### ✅ Steps:
- Define a constant `MAX_LENGTH = 3`
- Prompt the user to enter values into a list  
- If the list is longer than `MAX_LENGTH`, use `.pop()` to remove and print each extra item  
- Once it's shortened, print the final trimmed list

---

### 💡 Output Example:

Please enter an element of the list or press enter to stop. A
Please enter an element of the list or press enter to stop. B
Please enter an element of the list or press enter to stop. C
Please enter an element of the list or press enter to stop. D
Please enter an element of the list or press enter to stop.
Removed: D
Shortened list: ['A', 'B', 'C']


---

### 🧠 Key Concepts:
- `.pop()` removes and returns the **last element** of a list  
- Lists are **mutable**, so changes inside the function affect the original list  
- Loops can be used to **trim** data down to a target length

---

### 👨‍💻 Developer Notes:
- Cleanly demonstrates mutation of lists via `.pop()`  
- Prints every deleted item for transparency  
- Final list is kept at a defined constant size (`MAX_LENGTH`)  
- A great exercise in **data cleanup and constraint logic**

---
