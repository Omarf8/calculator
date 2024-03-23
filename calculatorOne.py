def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    operation = str(input("What operation would you like to use? (or type \'Stop\' to exit the program) ")).lower()
    if operation == "stop":
        break

    if operation == "+":
        user = None
        user2 = None
        while True:
            try:
                user = int(input("What number do you want to use? "))
            except:
                print("Not an integer")
                continue

            try:
                user2 = int(input("What number should be added to the previous number? "))
            except:
                print("Not an integer")
                continue

            break

        print(add(user, user2))
    elif operation == "-":
        user = None
        user2 = None

        while True:
            try:
                user = int(input("What number do you want to use? "))
            except:
                print("Not an integer")
                continue

            try:
                user2 = int(input("What number do you want to subtract from the previous integer? "))
            except:
                print("Not an integer")
                continue

            break

        print(subtract(user, user2))
    elif operation == "*":
        user = None
        user2 = None

        while True:
            try:
                user = int(input("What number do you want to use? "))
            except:
                print("Not an integer")
                continue

            try:
                user2 = int(input("What number do you want to multiply the previous integer by? "))
            except:
                print("Not an integer")
                continue

            break

        print(multiply(user, user2))
    elif operation == "/":
        user = None
        user2 = None

        while True:
            try:
                user = int(input("What number do you want to use? "))
            except:
                print("Not an integer")
                continue

            try:
                user2 = int(input("What number do you want to divide the previous number by? "))
            except:
                print("Not an integer")
                continue

            break
        print(divide(user, user2))
    else:
        print("Not a valid operation")

