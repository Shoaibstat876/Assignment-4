# 🪐 Planetary Weight Calculator - Handout

## 🎯 Objective:
Create a Python program that calculates a user's weight on another planet based on their Earth weight. This helps students understand basic arithmetic operations, input/output, constants, control flow, and formatting.

---

## 🛠 Milestone #1: Mars Weight
**Goal:** Calculate a user’s weight on Mars.

- Prompt the user: `Enter a weight on Earth:`
- Multiply that weight by Mars’s gravity constant: `0.378`
- Round the result to 2 decimal places using `round(value, 2)`
- Print the result in the format:

  ```
  The equivalent on Mars: 45.36
  ```

### 🔍 Example:
```bash
Enter a weight on Earth: 120
The equivalent on Mars: 45.36
```

---

## 🪐 Milestone #2: Add All Planets
**Goal:** Allow the user to enter any of the 7 other planets and get their weight accordingly.

### 🌌 Planet Gravities (as a % of Earth's):
- Mercury: `0.376`
- Venus: `0.889`
- Mars: `0.378`
- Jupiter: `2.36`
- Saturn: `1.081`
- Uranus: `0.815`
- Neptune: `1.14`

### 💡 Program Steps:
1. Ask for Earth weight: `Enter a weight on Earth:`
2. Ask for planet name: `Enter a planet:`
3. Use `if`/`elif` to match the planet and apply correct multiplier
4. Round and print:
   ```
   The equivalent weight on [Planet]: [value]
   ```

### 🧪 Sample Run:
```bash
Enter a weight on Earth: 150
Enter a planet: Jupiter
The equivalent weight on Jupiter: 354.0
```

---

## 🧠 Tips:
- Use constants for gravity values for clarity.
- Always convert string input to float before doing math.
- Use `round(result, 2)` for final output.

---

## 📦 Extension Idea:
Let users input planet names in any case (e.g. `jupiter`, `JUPITER`, `Jupiter`) using `.capitalize()` or `.lower()` with mapping.

---

## ✅ Learning Outcomes:
- Understand variable assignments
- Use of constants
- User input handling
- Control flow using `if`/`elif`
- String formatting and rounding output
- Use of functions for modularity

