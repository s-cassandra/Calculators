'''
Create a Python program that functions as a simple calculator. The program should:

1. Ask the user to enter two numbers.
2. Ask the user to choose an operation: addition (+), subtraction (-),
   multiplication (*), or division (/).
3. Perform the chosen operation on the two numbers.
4. Display the result of the calculation.
'''

while True:
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter another number:"))
    operation = input("Please choose an operation (+,-,*,/): ")

    if operation == '+':
        result = num1 + num2

    elif operation == '-':
        result = num1 - num2

    elif operation == '*':
        result = num1 * num2

    elif operation == '/':
        if num2 != 0:
            result = num1/num2
        
        else: 
            result  = "Error! Cannot divide by zero."

    else: 
        result = "Invalid operation"

    print(f'The result of {num1} {operation} {num2} is {result}')

    # Ask if user wants to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").strip().upper()
    if again.startswith('N'):
        print("Thank you for using the calculator!")
        break