def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("You can't divide by zero, idiot.")
    return a / b

print("Ugh, it's you. Welcome to meh-culator I guess.")
try:
    num1 = float(input("Give me your first number."))
    num2 = float(input("Okay now I need your second number."))
except ValueError:
    print("Umm thats not even a number.")
    exit()

operation = input("What operation do you want? (+, -, *, /)")

if operation == "+":
    print("Your sum is", add(num1, num2),". Are you done now?")

elif operation == "-":
    print("Your total is", subtract(num1, num2),". You done??")

elif operation == "*":
    print("Your total is", multiply(num1, num2),". Is that all or are you gonna keep bothering me?")

elif operation == "/":
    try: 
        print("Your total is", divide(num1, num2),". What else do you need?")
    except ValueError as e:
        print(e)
else:
    print("I dont even know what operation that is.")
