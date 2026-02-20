print("=" * 40)
print("   Welcome to Python Calculator v3")
print("=" * 40) #just for visual appeal

# Store calculation history
history = []

# OPERATIONS

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
def power(a,b):
    return a**b
def modulus(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a%b

# Function for safe input
def input_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Please enter a number.")

# Dictionary based operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulus
}
def display_menu():
    print("\nChoose operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("^  Power")
    print("%  Modulus")
    print("h  View Calculation History")
    print("q  Quit Calculator")

# Main Calculator Loop

def calculator():


    while True:
        display_menu()
        choice = input("\nEnter your choice: ").lower()

        if choice == "q":
            print("\nThank you for using Python Calculator v3!")
            break

        elif choice == "h":
            if history:
                print("\nCalculation History (last 5):")
                for i, item in enumerate(history[-5:], start=1):
                    print(f"{i}: {item}")
            else:
                print("\nNo calculations yet.")
            continue

        elif choice in operations:
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            result = operations[choice](num1, num2)

            # Round result if it's a float
            if isinstance(result, float):
                result = round(result, 2)

            print("\nResult:", result)

            # Save to history
            history.append(f"{num1} {choice} {num2} = {result}")

        else:
            print("Invalid choice! Please select a valid operation.")

# Start the calculator
calculator()