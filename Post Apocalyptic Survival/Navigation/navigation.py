'''
Developed by HudsonProgramming
    - Layton Hudson

        15:32 PM
        05/12/2022
'''

# Variables "x_pos" & "y_pos" used to store x and y coordinates separately.
x_pos = 0
y_pos = 0

last_x_pos = x_pos
last_y_pos = y_pos

# Variable "player_pos" used to store both x & y coordinates.
current_pos = x_pos , y_pos
last_pos = current_pos

# Creates an infinite loop
while True:
    
    print( "---------------------------------------------------------------" )
    print( "\  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \ " )
    print( "---------------------------------------------------------------\n" )
    print( "Current coordinates: [",x_pos,"/",y_pos,"]" )
    print( "Last coordinates: [",last_x_pos,"/",last_y_pos,"]" )
    print( "\n---------------------------------------------------------------" )
    print( "\  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \ " )
    print( "---------------------------------------------------------------\n" )
    print("You can currently travel:\n> North ( N )\n> East ( E )\n> South ( S )\n> West ( W )\n")

    # Stores user input as "user_option"
    user_option = input("> ")
    # Used to create a break in the lines ( Note \n can also be used to break lines )
    print("")

    # IF USER CHOOSES NORTH
    if user_option == "n":

        print("You travel North ( N )")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current Y coordinate
        y_pos = y_pos + 1

    # IF USER CHOOSES EAST   
    elif user_option == "e":

        print("You travel East ( E )")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current X coordinate
        x_pos = x_pos + 1

    # IF USER CHOOSES SOUTH   
    elif user_option == "s":

        print("You travel South ( S )")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current Y coordinate
        y_pos = y_pos - 1

    # IF USER CHOOSES WEST
    elif user_option == "w":

        print("You travel West ( W )")

        # Used to get the last coordinates
        last_x_pos = x_pos
        last_y_pos = y_pos

        # Updates current X coordinate
        x_pos = x_pos - 1

    # IF USER CHOOSES AN OPTION OTHER THAN STATED
    else:
        print("> Please enter a valid command")
        
    
    
