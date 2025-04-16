# ☎️ 01 - Phone Book

### 📌 Problem Statement:
Create a simple phone book using a **dictionary**.  
The program should let the user:
1. **Add contacts** (name and number)
2. **Print all saved contacts**
3. **Look up numbers** by name

---

### ✅ Steps:
- Ask the user for a **name** and **phone number**  
- Save the entry in a dictionary (`phonebook[name] = number`)  
- Keep asking until the user presses **Enter** without typing a name  
- Print all contacts from the dictionary  
- Then allow the user to **look up a contact** by name  
- If the name is not found, show a message saying so

---

### 💡 Output Example:

Name: Alice
Number: 1234
Name: Bob
Number: 5678
Name:

Alice -> 1234
Bob -> 5678

Enter name to lookup: Alice
1234
Enter name to lookup: Tom
Tom is not in the phonebook
Enter name to lookup:


---

### 🧠 Key Concepts:
- **Dictionaries** store key-value pairs (perfect for contacts)  
- `input()` collects user data  
- `if name in dict:` checks for existence before lookup  
- Great practice for **lookup logic and data management**

---

### 👨‍💻 Developer Notes:
- Code is broken into 3 clean functions:
  - `read_phone_numbers()` – to collect data
  - `print_phonebook()` – to display the list
  - `lookup_numbers()` – to perform live searches  
- Program continues until user enters a **blank line**  
- Easily extendable to support delete, update, etc.

---
