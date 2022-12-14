# Libraries
import pickle
import os
os.system("cls")

# Clears everything within Navigation_Coords.txt
with open("Navigation_Coords.txt", "a+") as f:
    f.truncate(0)

'''
Developed by HudsonProgramming
    - Layton Hudson

        15:32 PM
        05/12/2022
'''

# Variables "x_pos" & "y_pos" used to store x and y coordinates separately.
x_pos = 0
y_pos = 0

# Variables "last_x_pos" & "last_y_pos" used to store previous x and y coordinates separately.
last_x_pos = x_pos
last_y_pos = y_pos

# Creates an infinite loop
while True:

    coordinates = [x_pos,y_pos]

    # Adds current coordinates to a new line within Navigation_Coords.txt
    with open("Navigation_Coords.txt", "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(str(coordinates))
    
    print( "---------------------------------------------------------------" )
    print( "\  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \ " )
    print( "---------------------------------------------------------------\n" )
    print( "Current coordinates: [",x_pos,"/",y_pos,"]" )
    print( "Last coordinates: [",last_x_pos,"/",last_y_pos,"]" )
    print( "\n---------------------------------------------------------------" )
    print( "\  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \ " )
    print( "---------------------------------------------------------------\n" )
    print("You can currently travel:\n> North ( N )\n> East ( E )\n> South ( S )\n> West ( W )\n")

    # Stores user input as "user_option"
    user_option = input("> ")
    # Used to create a break in the lines ( Note \n can also be used to break lines )
    print("")

    # IF USER CHOOSES NORTH
    if user_option == "n":

        print("You travel North ( N )\n")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current Y coordinate
        y_pos = y_pos + 1

    # IF USER CHOOSES EAST   
    elif user_option == "e":

        print("You travel East ( E )\n")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current X coordinate
        x_pos = x_pos + 1

    # IF USER CHOOSES SOUTH   
    elif user_option == "s":

        print("You travel South ( S )\n")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current Y coordinate
        y_pos = y_pos - 1

    # IF USER CHOOSES WEST
    elif user_option == "w":

        print("You travel West ( W )\n")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current X coordinate
        x_pos = x_pos - 1

    # IF USER CHOOSES AN OPTION OTHER THAN STATED
    else:
        print("> Please enter a valid command")
        
    
    
