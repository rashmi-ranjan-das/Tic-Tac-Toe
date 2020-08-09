def check_winner(board,player,blocks_filled):
    if board['1'] == board['2'] == board['3'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['4'] == board['5'] == board['6'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['7'] == board['8'] == board['9'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['1'] == board['5'] == board['9'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['3'] == board['5'] == board['7'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['1'] == board['4'] == board['7'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['2'] == board['5'] == board['8'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif board['3'] == board['6'] == board['9'] != ' ':
        print("CONGRATULATIONS",player,"WINS")
        return True
    elif blocks_filled==9:
        print("ITS A TIE")
        return True
    else:
        return False