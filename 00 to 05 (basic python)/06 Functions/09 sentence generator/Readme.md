# 📝 09 - Sentence Generator

### 📌 Problem Statement:
Create a sentence generator using a function `make_sentence(word, part_of_speech)`  
that selects the sentence structure based on the type of word (noun, verb, or adjective).

---

### ✅ Steps:
- Prompt the user to input a **word**
- Ask the user what type of word it is:
  - `0` for noun
  - `1` for verb
  - `2` for adjective
- Call `make_sentence()` and generate the sentence
- Handle invalid inputs (like numbers other than 0, 1, or 2)

---

### 💡 Output Example:

Please type a noun, verb, or adjective: groovy
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2
Looking out my window, the sky is big and groovy!


---

### 🧠 Key Concepts:
- Using conditional logic with `if-elif-else`
- Passing parameters into functions
- Making sentence templates dynamic with user input
- Gracefully handling invalid options

---

### 👨‍💻 Developer Notes:
- Try expanding this to include more parts of speech (like adverbs or prepositions)
- This is a great intro to **basic NLP templating** logic
- Excellent for creative CLI tools or text games

---

