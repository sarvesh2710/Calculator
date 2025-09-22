def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations available: +, -, *, /")
    print("Type 'exit' to quit the calculator\n")
    
    while True:
        # Get the first number
        try:
            num1 = input("Enter the first number (or 'exit' to quit): ")
            if num1.lower() == 'exit':
                print("Thank you for using the calculator. Goodbye!")
                break
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue
        
        # Get the operator
        operator = input("Enter an operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please use +, -, *, or /.\n")
            continue
        
        # Get the second number
        try:
            num2 = input("Enter the second number (or 'exit' to quit): ")
            if num2.lower() == 'exit':
                print("Thank you for using the calculator. Goodbye!")
                break
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue
        
        # Perform calculation
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.\n")
                    continue
                result = num1 / num2
            
            print(f"Result: {num1} {operator} {num2} = {result}\n")
        
        except Exception as e:
            print(f"An error occurred: {e}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()