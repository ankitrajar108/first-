import random

user_input = input("Enter a choice : (rock, paper, scissor)")
possible_actions = ["rock", "paper", "scissor"]
computer_action = random.choice(possible_actions)
if user_input == computer_action:
    print("tie")
elif user_input == "rock":
    if computer_action == "paper":
        print("computer win!")
else:
    print("user win")

# print user action and computer action
