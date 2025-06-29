
import random

choices = ["snake", "water", "gun"]

# print(type(choices))

print("Choices:\nsnake\nwater\ngun")

while True:
    your_input = input("Enter your choice: ").lower()
    
    if your_input in choices:
        break  
    else:
        print("Enter a valid choice (snake, water, or gun)\n")

computer = random.choice(choices)

print(f"\nYour choice: {your_input}")
print(f"Computer's choice: {computer}")


if your_input == computer:
    print("Drawn!!")
else:
        if(computer =="water" and your_input =="snake"):
            print("computer wins !!")

        elif(computer =="snake" and your_input=="water"):
            print("you win !!")

        elif(computer =="gun" and your_input =="water"):
            print("you win !!")

        elif(computer =="water" and your_input =="gun"):
            print("computer wins !!")

        elif(computer =="snake" and your_input=="gun"):
            print("you win !!")

        elif(computer =="gun" and your_input=="snake"):
            print("computer win !!")

        else:
            print("something went wrong")

