#!/usr/bin/python3
"""
Script to explore Python's datetime module.
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    Save the date in a variable called current_date.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(days):
    """
    Calculate and display the future date after adding the given number of days.
    Save the future date in a variable named future_date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Prompt user for days and calculate future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value.")


if __name__ == "__main__":
    main()
