import time

def display_operations():
    """Display available arithmetic operations."""
    print("\nChoose the arithmetic operation you'd like to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def perform_calculation(num1, num2, operation):
    """Perform the calculation based on the selected operation."""
    if operation == '1':
        return f"{num1} + {num2} = {num1 + num2}"
    elif operation == '2':
        return f"{num1} - {num2} = {num1 - num2}"
    elif operation == '3':
        return f"{num1} * {num2} = {num1 * num2}"
    elif operation == '4':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return f"{num1} / {num2} = {num1 / num2}"
    else:
        return "Invalid operation!"

def get_number_input(prompt):
    """Prompt the user for a number until a valid one is provided."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That's not a valid number. Please try again.")

def calculator():
    """Main function to run the calculator."""
    print("=== Welcome to the Simple Calculator ===")
    
    while True:
        display_operations()
        operation = input("\nEnter the number corresponding to your choice: ")

        # Check if the user wants to exit
        if operation == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        # Validate the operation choice
        if operation not in ['1', '2', '3', '4']:
            print("Hmm, that's not a valid choice! Please select an operation from the list.")
            continue

        # Get user inputs for the numbers
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")

        # Perform the calculation
        result = perform_calculation(num1, num2, operation)
        
        # Display the result with a pause for better interaction
        print("\nCalculating...")
        time.sleep(1)  # Simulate a brief delay for effect
        print(f"Result: {result}\n")
        time.sleep(1)  # Pause before the next iteration

# Start the calculator application
if __name__ == "__main__":
    calculator()
