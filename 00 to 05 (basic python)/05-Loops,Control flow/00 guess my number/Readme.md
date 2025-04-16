# 🎯 00 - Guess My Number

### 📌 Problem Statement:
Write a game where the program picks a **secret number between 1 and 99**, and the user must **keep guessing** until they get it right.

After each guess, the program should tell the user whether their guess was **too high** or **too low**.  
Once they guess correctly, the program congratulates them.

---

### ✅ Steps:
- Use `random.randint(1, 99)` to choose a secret number  
- Use a `while` loop to **repeat the guessing process**  
- Compare each guess with the secret number:
  - If it's lower → print `"Your guess is too low"`  
  - If it's higher → print `"Your guess is too high"`  
- When the guess is correct → print a **congrats message** with the secret number

---

### 💡 Output Example:

I am thinking of a number between 1 and 99...
Enter a guess: 50
Your guess is too high

Enter a new guess: 25
Your guess is too low

Enter a new guess: 48
Congrats! The number was: 48


---

### 🧠 Key Concepts:
- `random.randint()` for random number generation  
- `while` loop for continuous user interaction  
- Conditional branching with `if-else` to guide the player  
- Dynamic user input with `input()` and `int()` conversion

---

### 👨‍💻 Developer Notes:
- Code is clean and user-friendly  
- Designed with reusability — can be extended with guess limits, difficulty levels, or scoring  
- A fun and interactive way to master **loops + logic**

---
