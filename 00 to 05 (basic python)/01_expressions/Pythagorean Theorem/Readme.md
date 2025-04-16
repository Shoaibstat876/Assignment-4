# 📐 04 - Pythagorean Theorem

### 📌 Problem Statement:
Write a program that calculates the **hypotenuse (BC)** of a right triangle using the **Pythagorean Theorem**:

BC² = AB² + AC²


Where:
- AB and AC are the perpendicular sides entered by the user  
- BC is the hypotenuse (longest side)

---

### ✅ Steps:
- Ask the user for sides `AB` and `AC`
- Use the formula `BC = sqrt(AB² + AC²)`
- Print the length of `BC` (the hypotenuse)

---

### 💡 Output Example:

Enter the length of AB: 3
Enter the length of AC: 4
The length of BC (the hypotenuse) is: 5.0


---

### 👨‍💻 Developer Notes:
- Used the `math.sqrt()` function for square root calculation  
- Inputs were cast to `float` to support decimal values  
- Applied `ab ** 2 + ac ** 2` inside `sqrt()` for correct math  
- Final result is printed in a clear sentence for the user

---
