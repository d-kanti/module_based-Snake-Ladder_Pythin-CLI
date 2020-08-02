
import src.board_info as snl
import src.mode as mode
import src.player_turn as pt










class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
    
name_temp = input("Enter the name of the Player 1 :  ")
p1 = Player(name_temp, 0)
name_temp = input("Enter the name of the Player 2 :  ")
p2 = Player(name_temp, 0)

mode = mode.mode_select()




##############################################
print("############start##########")
status = 0
p1_win = False
p2_win = False
while not p1_win and not p2_win:
    if status == 0:
        (p1,p2_win,p1_win,status) = pt.turn_p1(mode,snl,p1,p2_win,p1_win,status)
        if p1_win :
            print("Congratulations {}!! You win the game!".format(p1.name))
            break
        elif p2_win :
            print("Congratulations {}!! You win the game!".format(p2.name))
            break
        else:
            continue
    elif status == 1:
        (p2,p1_win,p2_win,status) = pt.turn_p2(mode,snl,p2,p1_win,p2_win,status)
        if p1_win :
            print("Congratulations {}!! You win the game!".format(p1.name))
            break
        elif p2_win :
            print("Congratulations {}!! You win the game!".format(p2.name))
            break
        else:
            continue