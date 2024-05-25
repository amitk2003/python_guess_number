import random
# random guessing number
x=random.randint(0,100)
# y=print(x);\
print(x)
p=int(input("enter a number:"))
if p==x:

    print("you guessed right number");
elif p>x:
    print("you guess is high compared to computer")
else:
    print("your guess is  low as compared to computer")    