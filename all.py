
import src.board_info as snl
import src.mode as mode
import src.player_turn as pt
import src.extra_func as x










class Player():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
    
    def congrat(self):
         print(f"Congratulations {self.name}!! You win the game!")

    
p1 = Player(x.nam("Player 1"), 0)
p2 = Player(x.nam("Player 2"), 0)

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
            p1.congrat()
            break
        elif p2_win :
            p2.congrat()
            break
        else:
            continue
    elif status == 1:
        (p2,p1_win,p2_win,status) = pt.turn_p2(mode,snl,p2,p1_win,p2_win,status)
        if p1_win :
            p1.congrat()
            break
        elif p2_win :
            p2.congrat()
            break
        else:
            continue