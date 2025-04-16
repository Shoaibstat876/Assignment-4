# 🧠 Logic Recap: Guess My Number

| Variable        | What It Represents                     | User Input? | Explanation                                 |
|------------------|----------------------------------------|-------------|---------------------------------------------|
| `secret_number` | Random number from 1 to 99              | ❌ No        | Set using `random.randint(1, 99)`           |
| `guess`         | The number the user inputs              | ✅ Yes       | Continuously updated until correct          |
| `while guess != secret_number` | Loop until correct guess | ❌ No        | Repeats the loop while guess is wrong       |
| `if guess < secret_number`     | Check if guess is too low | ❌ No        | Prints "too low"                            |
| `else`                        | Guess is too high           | ❌ No        | Prints "too high"                           |
