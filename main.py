import packages.check as check_winner
import packages.print as board_print


board = {
    "1" : ' ',
    "2" : ' ',
    "3" : ' ',
    "4" : ' ',
    "5" : ' ',
    "6" : ' ',
    "7" : ' ',
    "8" : ' ',
    "9" : ' '
}
print("-------------------------------------Hello and welcome to the classic 3 X 3 TIC-TAC-TOE Game------------------------------------------")
print("It will be a Two player game and the player wins if he/she gets 3 'X' continuously either vertically,horizontally or diagonally.\n" )

print("The block numbers of the board is as follows :")
print('1' + ' | ' + '2' + ' | ' + '3')
print('--+---+--')
print('4' + ' | ' + '5' + ' | ' + '6')
print('--+---+--')
print('7'+ ' | ' + '8' + ' | ' + '9')
print("So let,s start the game............\n")
print("Initial Board :          ")


want_to_play = 'y'
while want_to_play == 'y':
    board_print.board_print(board)
    player = 'X'
    blocks_filled = 0

    for turn in range(10):
        choice = input('Its your turn '+player+'...Chose a block(1-9) to insert your mark ')
        
        if int(choice) > 9:
            choice = input('Invalid choice. Enter a choice from 1 to 9 ')
            while int(choice) > 9:
                choice = input('Invalid choice. Enter a choice from 1 to 9 ')
        
        while board[choice] != ' ':
            choice = input('Invalid choice. Choose once again ')

        board[choice] = player
        

        blocks_filled = blocks_filled + 1
        board_print.board_print(board)

        if blocks_filled >= 5:
            winner = check_winner.check_winner(board,player,blocks_filled)
            if winner == True:
                board = {
                        "1" : ' ',
                        "2" : ' ',
                        "3" : ' ',
                        "4" : ' ',
                        "5" : ' ',
                        "6" : ' ',
                        "7" : ' ',
                        "8" : ' ',
                        "9" : ' '
                    }
                want_to_play = input('Do you want to play again ???(y or n)')
                break
            else:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

    
        else:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        
