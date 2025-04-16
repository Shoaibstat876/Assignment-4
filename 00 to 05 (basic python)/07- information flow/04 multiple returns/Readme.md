# 📬 04 - User Info Collector (Tuple Return)

### 📌 Problem Statement:
Create a function `get_user_info()` that collects a user's:
- First name
- Last name
- Email address  
…and returns all three values using **tuple packing**.

---

### ✅ Steps:
1. Use `input()` to collect first name, last name, and email.
2. Return all three values using a return statement with commas.
3. Store the returned tuple and print it in `main()`.

---

### 💡 Sample Output:

What is your first name?: Jane What is your last name?: Stanford What is your email address?: janestanford@stanford.edu Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')


---

### 🧠 Key Concepts:
- Tuple packing (returning multiple values from a function)
- User input collection
- Clean separation of data and presentation logic

---

### 👨‍💻 Developer Notes:
- You can also unpack the tuple if you want separate variables:
  ```python
  fname, lname, email = get_user_info()
