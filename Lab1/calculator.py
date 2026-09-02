try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = first_number + second_number
        print(f"Result: {result}")
    elif operation == "-":
        result = first_number - second_number
        print(f"Result: {result}")
    elif operation == "*":
        result = first_number * second_number
        print(f"Result: {result}")
    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"Result: {result}")
    else:
        print("Error: Invalid operation.")
except ValueError:
    print("Error: Please enter valid numbers.")