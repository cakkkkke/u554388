def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def calculator():
    print("Select type of operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice (1/2/3/4):")

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice =="1":
        print(add(num1, num2))
    elif choice =="2":
        print(sub(num1, num2))
    elif choice =="3":
        print(multi(num1, num2))
    elif choice =="4":
        print(divide(num1,num2))
    else:
        print("error")

calculator()
