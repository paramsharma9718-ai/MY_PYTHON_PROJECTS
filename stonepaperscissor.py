'''
import random
item_list=["Stone","Paper","Scissor"]

user_choice=input("ENTER YOUR CHOICE (Stone , Paper , Scissor) = ")
comp_choice=random.choice(item_list)

print(f"user choice = {user_choice} , coumoter choice = {comp_choice}")


if user_choice == comp_choice:
    print("BOTH CHOICES ARE SAME := MATCH TIE")
elif user_choice == "Stone":
    if comp_choice == "Paper":
        print("COMPUTER WIN")
    else:
        print("YOU WIN")  
elif user_choice == "Paper":
    if comp_choice == "scissor":
        print("COMPUTER WIN")
    else:
        print("YOU WIN")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("YOU WIN")
    else:
        print("COMPUTER WIN")
                                     '''

import random

item_list = ["Stone", "Paper", "Scissor"]

# take input from user
user_choice = input("ENTER YOUR CHOICE (Stone, Paper, Scissor) = ").title()


# computer random choice

comp_choice = random.choice(item_list)

print(f"user choice = {user_choice} , computer choice = {comp_choice}")

# game logic
if user_choice == comp_choice:
    print("BOTH CHOICES ARE SAME : MATCH TIE")

elif user_choice == "Stone":
    if comp_choice == "Paper":
        print("COMPUTER WIN")
    else:
        print("YOU WIN")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("COMPUTER WIN")
    else:
        print("YOU WIN")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("YOU WIN")
    else:
        print("COMPUTER WIN")

else:
    print("INVALID INPUT! Please enter Stone, Paper or Scissor.")
