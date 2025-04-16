## 🧠 Explanation: Planetary Weight Calculator

This project is divided into two parts:

---

### ✅ Part 1: Weight on Mars

This section calculates the equivalent weight of a person on Mars using a fixed gravitational multiplier.

**Key steps:**
1. Prompt the user to enter their weight on Earth.
2. Multiply the entered weight by `0.378`, which represents Mars' gravity as a percentage of Earth’s.
3. Use the `round()` function to round the result to 2 decimal places.
4. Print the final weight on Mars.

**Why this matters:**
Mars has significantly weaker gravity, and this program helps users visualize their weight difference between planets.

---

### 🌌 Part 2: Weight on Any Planet

Here, we extend the same logic but apply it to any of the following planets:
Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune.

**Key steps:**
1. Prompt the user for their Earth weight.
2. Prompt the user for the name of a planet (capitalized).
3. Use a series of `if-elif-else` statements to select the appropriate gravity constant:
   - Mercury: `0.376`
   - Venus: `0.889`
   - Mars: `0.378`
   - Jupiter: `2.36`
   - Saturn: `1.081`
   - Uranus: `0.815`
   - Neptune: `1.14`
4. Multiply the Earth weight by the gravity constant of the selected planet.
5. Round the result to 2 decimal places.
6. Print the equivalent planetary weight.

**Why this matters:**
Each planet has its own gravitational pull. This extended calculator allows users to explore and compare their weights across the solar system.

---

### 🧪 Concepts Practiced
- `input()` and user interaction
- Type conversion (`float`)
- Arithmetic operations and constants
- `if-elif-else` control flow
- `round()` for formatting
- Output formatting with `print()`

This task combines real scientific context with core Python programming fundamentals, giving learners both practical skill and cosmic curiosity! 🚀

