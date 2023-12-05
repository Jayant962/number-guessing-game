import random
Cnumber=random.randrange(1,6)
userinput=int(input("Enter your no.(1-5):"))
if Cnumber>userinput:
    print("Computer No.:",Cnumber)
    print("Your no. is low")
    print("Computer Win")
elif Cnumber<userinput:
    print("Computer No.:",Cnumber)
    print("Your no. is high")
    print("Computer Win")
else:
    print("Computer No.:",Cnumber)
    print("You win")