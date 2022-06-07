def add():
    print("Output: \n" + str(a + b))


def sub():
    print("Output: \n" + str(a - b))

def mult():
    print("Output: \n" + str(a * b))

def div():
    print("Output: \n" + str(a / b))

def function():
    x = 0

    while x == 0:
        try:
            global a
            a = float(input("Enter number:\n"))
            x = 1
        except:
            print("Please enter a valid number\n")
            x = 0

    s = 0

    while s == 0:

        k = input("Type + to Add, - to Subtract, * to Multiply, or / to Divide:\n")
        if k == "+":
            s = 1
            z = 1
        elif k == "-":
            s = 1
            z = 2
        elif k == "*":
            s = 1
            z = 3
        elif k == "/":
            s = 1
            z = 4
        else:
            s = 0

    while x == 1 and s == 1:
        try:
            global b
            b = float(input("Enter another number:\n"))
            x = 2
        except:
            print("Please enter a valid number\n")
            x = 1

    if z == 1:
        add()
    if z == 2:
        sub()
    if z == 3:
        mult()
    if z == 4:
        div()



t = 1
while t == 1:
    function()

