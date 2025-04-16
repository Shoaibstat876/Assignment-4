# 🧠 Logic Recap: Fruit Inventory Checker

| Variable         | What It Represents                          | User Input? | Explanation                                         |
|------------------|---------------------------------------------|-------------|-----------------------------------------------------|
| `fruit`          | The name of the fruit user wants to check   | ✅ Yes      | Collected from user via input                       |
| `stock`          | Quantity of that fruit in inventory         | ❌ No       | Returned by `num_in_stock(fruit)`                   |
| `num_in_stock()` | Helper function to return fruit quantity    | ❌ No       | Contains hardcoded inventory values                 |
| `if stock == 0`  | Condition to check if fruit is not available| ❌ No       | Handles unavailable fruit case                      |
| `print(...)`     | Displays appropriate message to user        | ❌ No       | Based on inventory status                           |
