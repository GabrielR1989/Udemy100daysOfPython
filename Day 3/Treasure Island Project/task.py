from operator import truediv

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

LR_direction = input("You're at a cross road. Where do you want to go?.       \n Type "'left'" or "'right'".\n").upper()
winner = False
losing_action = ""

if LR_direction == "LEFT":
    Wait_swim = input("You've come to a lake. There is an island in the middle of the lake.       \n "
      "Type "'wait'" to wait for a boat. Type ""swim"" to swim across.\n").upper()

    if Wait_swim == "WAIT":
        door_col = input("You arrive at the island unharmed. There is a house with 3 doors      \n "
              "One red, one yellow and one blue. Which colour do you choose?\n").upper()

        if door_col == "YELLOW":
            winner = True
        elif door_col == "RED":
            losing_action = "It's a room full of fire"
        elif door_col == "BLUE":
            losing_action = "You entered a room of beasts"
        else:
            losing_action = "The color chosen is not valid"
    else:
        losing_action = "You get attacked by an angry trout"

else:
    losing_action = "You fell into a hole"


if winner:
    print("You found the treasure! You Win!")
else:
    print(f"You Lose! {losing_action}. Game Over!")