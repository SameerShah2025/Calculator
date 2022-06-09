#All originally written by SameerShah2025

#add function
def add():
    print("Output: \n" + str(a + b))

#subtraction function
def sub():
    print("Output: \n" + str(a - b))

#multiply function
def mult():
    print("Output: \n" + str(a * b))

# divide function
def div():
    print("Output: \n" + str(a / b))


#function defining the input and ouptut
def function():
    x = 0
#make a true statement to run a input loop
    while x == 0:
        try:
            global a
            a = float(input("Enter number:\n"))
            x = 1
            # if the user enters anything but a number, the function will prompt it to enter again. if the user does, I changed the variable to stop the loop.
        except:
            print("Please enter a valid number\n")
            x = 0
    # another variable to make a true statement for a input loop
    s = 0

    while s == 0:

        k = input("Type + to Add, - to Subtract, * to Multiply, or / to Divide:\n")
        # basically I am using variables to store data when the user decides to add, subtract, multiply, or divide
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
            #I have specifically prompted the user to use the symbols when deciding on add, subtract, multiply, or divide. If the user types anything else, it will ask to try again.
        else:
            s = 0

            # only after the user has completed both steps above, will the last input appear. here I am making a loop based on after the user succesfully completed the steps above 
    while x == 1 and s == 1:
        try:
            global b
            b = float(input("Enter another number:\n"))
            x = 2
        except:
            print("Please enter a valid number\n")
            x = 1
#here the stored variables for data are being called after the inputs fininsh. depending on what the user chose, I am calling which function should be executed.
    if z == 1:
        add()
    if z == 2:
        sub()
    if z == 3:
        mult()
    if z == 4:
        div()


#here I am using a variable to make a true statement, just to keep the function above ^ running over and over again. 
t = 1
while t == 1:
    function()

