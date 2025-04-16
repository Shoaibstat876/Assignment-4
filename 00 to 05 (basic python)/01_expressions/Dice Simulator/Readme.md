# 🎲 01 - Dice Simulator

### 📌 Problem Statement:
Simulate rolling two dice, three times. Print the result of each roll and demonstrate how **variable scope** works between `main()` and another function.

---

### ✅ Steps:
- Create a constant `NUM_SIDES = 6` to represent dice sides
- Define a function `roll_dice()` to generate two random dice rolls
- Call `roll_dice()` three times from within `main()`
- Print the value of `die1` inside `main()` to show variable scope

---

### 💡 Output Example:

die1 in main() starts as: 10
Total of two dice: 7
Total of two dice: 11
Total of two dice: 6
die1 in main() is: 10


*(Output will vary because of random dice rolls)*

---

### 👨‍💻 Developer Notes:
- Used `random.randint(1, 6)` to simulate dice rolls 🎲  
- Demonstrated **variable scope**: `die1` inside `main()` stays unchanged  
- Created a reusable function `roll_dice()` for clarity  
- Code is structured and clean, perfect for learning scope basics  

---
