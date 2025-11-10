num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            result = None
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")
        result = None

if result is not None:
    print(f"The result is: {result}")
