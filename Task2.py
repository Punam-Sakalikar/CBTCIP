import random
def winner(player_choice,comp_choice):
    if player_choice==comp_choice:
        print("It's tie!!")
    elif ((player_choice=="rock" and comp_choice=="scissor")
          or (player_choice=="paper" and comp_choice=="rock")
          or (player_choice=="scissor" and comp_choice=="paper")):
              print("congratulation!! You Won")
    else:
        print("Ooops you lost!\nComputer won!")

def play():
    options=["rock","paper","scissor"]
    comp_choice=random.choice(options)
    player_choice=input("Enter your choice (rock,paper,scissor):").lower()
    if player_choice not in options:
        print("please choose the correct option")
        play()
    else:
        print("your chose:",player_choice)
        print("computer chose:",comp_choice)
        print()
        winner(player_choice,comp_choice)

print("\t\t\tWelcome to rock,paper,scissor game")
print("\t\t.......................................")
print()
start=input("want to start the game? (yes/no)")
if (start!="no"):
    while(start!="no"):
        play()
        start=input("\nDo you want to play again? (yes/no)").lower()

        print("\nThank you for playing the game!")