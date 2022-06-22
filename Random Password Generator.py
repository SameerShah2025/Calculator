#All of this work was made alone by SameerShah2025

# I will need import random to set the random password output. To make it easier, I called random as r
import random as r
# here I set a variable c (stands for all the possible Characters)
c = "`1234567890-=qwertyuiop[]|asdfghjkl;zxcvbnm,./<>QWERTYUIOPASDFGHJKLZXCVBNM?"

# next I made a true statement to start a while loop
x = 0

while x == 0:
    # I used two try/except to ensure the user puts only a number when prompted both seperate questions
    try:
        pl= int(input("How long do you want your password?\n"))
    except:
       print("Please enter a valid number")

    try:
        pn = int(input("Enter how many passwords you want:\n"))
    except:
        print("Please enter a valid number")
#here I set for-in loop to call out the sequence of numbers.
    for a in range(0, pn):
        # I set z as a short variable to call out  the random sequence, and p (which stands for the Password itself) to combine with z to create the password funtion.
        # I used r.choice (r is short for random as mentioned above ^^) to choose a random sequence for the password
        p = ""
        for a in range(0,pl):
            z = r.choice(c)
            p = p + z
    #Here I called out the output of the password(s)
        print("Password(s): " + p)


    x = 1
#end of code

