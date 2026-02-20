# 🧮 Python Calculator v3

A command-line calculator built with Python, progressively improved across 3 versions as part of my Python learning journey.

---

## 🚀 Features

- ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division
- ⚡ Power (`^`) and 📐 Modulus (`%`) operations
- 📋 Calculation history — view your last 5 calculations
- ✅ Input validation — handles invalid inputs without crashing
- 🔑 Dictionary-based operations — clean and scalable code structure

---

## 📸 Preview

```
===================================
   Welcome to Python Calculator v3
===================================

Choose operation:
+  Addition
-  Subtraction
*  Multiplication
/  Division
^  Power
%  Modulus
h  View Calculation History
q  Quit Calculator

Enter your choice: +
Enter first number: 15
Enter second number: 7

Result: 22.0
```

---

## 🛠️ How to Run

1. Make sure Python is installed on your system. Download it from [python.org](https://www.python.org/)
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-calculator.git
   ```
3. Navigate to the folder:
   ```bash
   cd python-calculator
   ```
4. Run the calculator:
   ```bash
   python calculator_v3.py
   ```

---

## 📂 Project Structure

```
python-calculator/
│
├── calculator_v1.py   # Basic calculator — functions, loops
├── calculator_v2.py   # Added input validation, try/except, symbols
└── calculator_v3.py   # Added history, power, modulus, dictionary operations
```

---

## 🧠 Concepts Used

| Concept | Where it's used |
|---|---|
| Functions | Each operation has its own function |
| Dictionary | Maps symbols to functions — replaces long if/elif |
| try/except | Input validation — handles invalid entries |
| while loop | Keeps calculator running until user quits |
| List & slicing | `history[-5:]` stores and displays last 5 results |
| f-strings | Clean formatted output |

---

## 📈 Version History

| Version | What was added |
|---|---|
| v1 | Basic calculator with if/elif, number-based menu |
| v2 | Separated functions, symbol-based menu, input validation |
| v3 | History, power & modulus, dictionary-based operations |

---

## 🎯 What's Next

- [ ] Square root operation
- [ ] Save history to a text file
- [ ] Unit converter mode

---

## 👤 About Me

I'm a student from Pakistan in 11th grade, currently learning Python through the **Python for Everybody (Py4E) Specialization** by University of Michigan on Coursera. I share one project every week on LinkedIn to document my progress.

🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/muhammad-rehan-javed-847701211)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
