import sys
from random import randint
a=randint(1,9)
z=3
for i in range(z):
    b=int(input("Please guess what number it is:"))
    if (b==a):
        print("It is correct, you are so clever")
        sys.exit("Correct answer given")
    elif(b>a):
            print("Your answer is incorrect. The answer should be smaller than",b,", you have",z-1-i,"chances left")
          
    else:
            print("Your answer is incorrect. The answer should be bigger than",b,", you have",z-1-i,"chances left")
print(a)  