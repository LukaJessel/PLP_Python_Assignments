def main():
    print("Basic Calculator Program")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print (f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print (f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print (f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 == 0:
       print (f"Error: Division by Zero isn't allowed!")
    else:
       result = num1 / num2
       print (f"{num1} / {num2} = {result}")