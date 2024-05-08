print("***********************************************************************************")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road.\nWhere do you want to go?\n")
direction=input("Type 'Left' or 'Right'")

if direction=="Left":
    print("You've come to a lake. There is an island in the middle of the lake.\n")
    Next=input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")

    if Next=="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue.") 
        color=input("Which colour do you choose?\n")

        if color=="red":
            print("It's a room full of fire. Game Over.")

        elif color=="blue":
            print("You enter a room of beasts. Game Over.")

        elif color=="yellow":
            print("YAY!\n Found the treasure\n YOU WIN!")

    elif Next=="Swim":
        print("You are attacked by sea monsters.Game Over")

elif direction=="right":
    print("Oops, wrong direction. Game Over")
