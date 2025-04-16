# 🔐 03 - Powerful Password

### 📌 Problem Statement:
You're building a **login system** that checks passwords **securely using hashes** — so that even you don’t store or see real passwords.  
This is done using a technique called **hashing** (specifically SHA256).

---

### ✅ Goal:
- Given a dictionary of `email → hashed_password`, write a function to:
  - Hash the **input password**
  - Compare it with the stored hash for that email
  - Return `True` if they match, `False` if they don’t

---

### 💡 Output Example:

False # "word" ≠ "password" True # "password" is correct True # "Karel" matches stored hash False # "karel" ≠ "Karel" False # Incorrect password for student True # "123!456?789" matches hash


---

### 🧠 Key Concepts:
- **SHA256 Hashing** (via `hashlib`) makes passwords unreadable  
- Passwords are verified by comparing **hashed versions**  
- Dictionaries are used for fast `email → hash` lookup

---

### 👨‍💻 Developer Notes:
- Function `hash_password()` converts a password to a unique hash  
- Function `login(email, stored_logins, password_to_check)` returns `True` if hashes match  
- Real-world login systems use the same logic — this is a **real security concept**

---

### 🛡️ Bonus:
This program doesn't store plain-text passwords at all — making it far more secure than basic login systems.

---
