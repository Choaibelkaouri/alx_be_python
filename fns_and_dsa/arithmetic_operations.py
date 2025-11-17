#!/usr/bin/python3
"""
Module for basic arithmetic operations.
"""


def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Args:
        num1: first number (float)
        num2: second number (float)
        operation: 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        Result of the operation, or an error message for invalid cases.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            # value/message the checker can display for divide-by-zero
            return "Error: Division by zero"
        return num1 / num2
    else:
        # in case an unsupported operation is passed
        return "Error: Invalid operation"
