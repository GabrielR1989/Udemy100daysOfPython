import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions_ASCI = [rock, paper, scissors]
actions_str = ["rock", "paper", "scissors"]

#Get the index number
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
computer_choice = random.randint(0,len(actions_str)-1)

#Check if the number entered is listed
if not player_choice.isnumeric():
    print("Invalid selection!")
    exit()

if 0 <= int(player_choice) > len(actions_str) - 1:
    print("Invalid selection!")
    exit()

player_choice = int(player_choice)

#Get the text name of the index previously gotten
player_choice_element = actions_str[player_choice]
computer_choice_element = actions_str[computer_choice]

# print(player_choice_element)
# print(computer_choice_element)

print(f"You chose: {player_choice_element} \n {actions_ASCI[player_choice]}")
print(f"Computer chose: {computer_choice_element} \n {actions_ASCI[computer_choice]}")

if player_choice_element == computer_choice_element:
    print("It's a draw!")

if player_choice_element == "rock" and computer_choice_element == "scissors":
    print("You win!")
elif computer_choice_element == "rock" and player_choice_element == "scissors":
    print("You lose!")

if player_choice_element == "scissors" and computer_choice_element == "paper":
    print("You win!")
elif computer_choice_element == "scissors" and player_choice_element == "paper":
    print("You lose!")

if player_choice_element == "paper" and computer_choice_element == "rock":
    print("You win!")
elif computer_choice_element == "paper" and player_choice_element == "rock":
    print("You lose!")