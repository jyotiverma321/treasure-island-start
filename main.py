print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
user_choice = input(
    "You're at a crossroad. Where do you want to go? Type left or right: ")
if user_choice == "left":
    user_choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for the boat.\n Type 'swim' to swim across: " )
    user_choice2_lowercase = user_choice2.lower()
    if user_choice2_lowercase == "wait":
        print("You are attacked by an angry trout. Game Over")
    elif user_choice2_lowercase == "swim":
        print(
            "You arrive at the island unharmed. There is a house with 3 doors. One Red, One Yellow and One Blue"
        )
        user_choice3 = input("Which colour do you choose? ")
        user_choice3_lowercase = user_choice3.lower()
        if user_choice3_lowercase == "red":
            print("Its a room full of fire. Game Over")
        elif user_choice3_lowercase == "blue":
            print("You found the Treasure! You Win")
        elif user_choice3_lowercase == "yellow":
            print("You entered a room of beasts. Game Over")
        else:
            print("You chose a room that doesn't exist")
    else:
        print("Your Don't have that choice. Start Over")

else:
    print("You Fell into a hole. Game Over")
