#defining a mode of the game, 'auto' mode means randomly
# a number of moves will be made. 
#'manual' mode means the input will be provided by the player (<=20)

mode = ""
while(not mode):
    temp = input("Please enter the Mode of the Game: ")
    if temp == 'auto' or temp == 'manual':
        mode = temp
    else:
        print("Invalid Input !!")
        continue