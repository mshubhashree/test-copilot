#!/usr/bin/env python3
"""
Simple Calculator Script

This script performs basic arithmetic operations (addition, subtraction, 
multiplication, division) on two numbers provided by the user.
It includes error handling for division by zero and allows multiple 
calculations in a continuous loop.
"""


def get_number(prompt):
    """
    Get a valid number from user input.
    
    Args:
        prompt (str): The prompt message to display to the user
        
    Returns:
        float: A valid number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    """
    Get a valid operation choice from the user.
    
    Returns:
        str: The chosen operation ('+', '-', '*', '/')
    """
    operations = {
        '1': '+',
        '2': '-', 
        '3': '*',
        '4': '/'
    }
    
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract second number from first number."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): The dividend
        b (float): The divisor
        
    Returns:
        float: The result of division
        
    Raises:
        ZeroDivisionError: If divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


def perform_calculation(num1, num2, operation):
    """
    Perform the specified calculation on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform ('+', '-', '*', '/')
        
    Returns:
        float: Result of the calculation, or None if error occurred
    """
    try:
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation!")
            return None
            
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to run the calculator."""
    print("=" * 50)
    print("          SIMPLE CALCULATOR")
    print("=" * 50)
    print("Welcome! This calculator performs basic arithmetic operations.")
    
    while True:
        print("\n" + "-" * 30)
        
        # Get the two numbers from user
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        # Get the operation from user
        operation = get_operation()
        
        # Perform the calculation
        result = perform_calculation(num1, num2, operation)
        
        # Display the result
        if result is not None:
            operation_names = {
                '+': 'Addition',
                '-': 'Subtraction', 
                '*': 'Multiplication',
                '/': 'Division'
            }
            
            print(f"\n{operation_names[operation]} Result:")
            print(f"{num1} {operation} {num2} = {result}")
        
        # Ask if user wants to continue
        print("\nDo you want to perform another calculation?")
        continue_choice = input("Enter 'y' for yes or any other key to exit: ").strip().lower()
        
        if continue_choice != 'y':
            print("\nThank you for using the calculator! Goodbye!")
            break


if __name__ == "__main__":
    main()