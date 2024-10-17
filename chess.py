##########################################                                      CHESS                                   ###################################################
#                                                                                                                                                                         #
#       If you are not farmiliar with the rules of chess you can go here: https://en.wikipedia.org/wiki/Rules_of_chess                                                    #
#       If you want to be weird and use unicode symbols for the pieces you can go here: https://altcodeunicode.com/alt-codes-chess-symbols/                               #
#       That'll make it slightly harder to determine which is whose piece but you do you                                                                                  #
#                                                                                                                                                                         #
########################################################################################################################################################################### 

def board():
    '''
    This function takes no input and returns a board which represents the initial state of a game of chess
    You should use whatever strings you decide for the pieces (and ownership) but you must be consistent!

    I recommend using characters for each piece (Kn = knight, P = Pawn, etc..) and appending that on W or B, for which player it is
    I.e. WKn is a White Knight, WK would be the white king, BP is a black pawn, etc.
    '''


    board=[
    [-2, -3, -4, -5, -6, -4, -3, -2],  #1-> white; -1-> black
    [-1, -1, -1, -1, -1, -1, -1, -1],  
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [1, 1, 1, 1, 1, 1, 1, 1],         
    [2, 3, 4, 5, 6, 4, 3, 2]]           

    return board

def valid_move_empty_square(a,b,c,d):
    current_board=board()
    for row in range(a,c+1):
        for col in range(b,d+1):
            if current_board[row][col]!=0:
                return False
    return True

def valid_move_rook(a,b,c,d): #takes in current position of the rook(row,col):a,b & target position c,d
    #rook can only move if it's all zeros either in a straight file of rows:
    # i might have to be fluent with 2 lists
    current_board=board()
    for i in range(a,c+1):  #(2,2)->(5,2) move south to north: loop through a(rows)
        if current_board[i][b]!=0:
            print("Not allowed") #going from a to c(moving in the same row)-> looping over -> checking all col indices bw a to c
    print("Allowed movement of rook in this row until the target position")
        # else:
        #     print("Not allowed")
    for i in range(b,d+1): #move from west to east: loop through cols
        if current_board[a][i]!=0: # #going from b to d(moving in the same column)-> looping over -> checking all row indices bw b to d
            print("not allowed")
    print("Allowed movement of rook in this column until the target position")
        # else:
        #     print("not allowed")
valid_move_rook(2,2,5,2)


def any_check(board):
    '''
    This function will check to see if any piece is currently able to move to it's enemies king

    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
               Each spot should have a string representing which piece is in that spot and which player owns it
    Returns:
        winner: An int representing who is in check if anyone. It should have the value 1 if Player 1 is, -1 for Player 2 is
                And 0 if neither player is in check at the moment 
    '''

    ## TODO Implement check of a check mate
    ############################################



    ############################################

    return winner


def valid_move(board, player, origin=(0,0), destination=(0,2)):
    '''
    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
        origin: a pair of indeces (ints) representing a location on the board (0,0 would represent row 0, col 0 for example). We will try to move the piece that is at this location currently
        desination: another pair of indeces (ints) representing a location on the board. This is the location we will try to move our piece to.
    Returns:
        valid: A boolean representing whether this was a valid move 
    '''

    
    return valid

def move(board, player, origin=(0,0), destination=(0,2)):
    '''
    This function should ask the current player which move they'd like to make and then implement it if possible, else
    ask them to give a different move

   Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
        origin: a pair of indeces (ints) representing a location on the board (0,0 would represent row 0, col 0 for example). We will try to move the piece that is at this location currently
        desination: another pair of indeces (ints) representing a location on the board. This is the location we will try to move our piece to.
    Returns:
        new_board: A 2d list representing the updated board after making the move
    '''

    # P1's move: if x[a][b].split("_")[1]=="P2"
        
    ## TODO Implement a move (with check)
    ############################################



    ############################################
        
    return new_board


def any_check_mate(board):
    '''
    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
               Each spot should have a string representing which piece is in that spot and which player owns it
    Returns:
        winner: An int representing who won if anyone. It should have the value 1 if Player 1 won, -1 for Player 2
                And 0 if neither player has won yet 
    '''

    ## TODO Implement check of a check mate
    ############################################



    ############################################

    return winner

def play_game():
    '''
    This function has no input or output, but will run through the full game and print out the board after each move
    It should also print out a congrats message to whichever player won

    It should swap between players and make checks each move to see if the game is over, also it should tell a player on their turn when they are in check
    '''

    ## TODO The full game (using all previous functions)
    ############################################

    board = initialize_board()



    ############################################

    return None

play_game()