
#***********Functions defined **********
def isTargetValidPawnDiag(board, a,b, c, d, current_player): #would return True if the target is one of the diagonal squares relative to the selected_sq
    if current_player=="White" and (c==a+1) and abs(d-b)==1: #white is increasing the indices
        return True

    elif current_player=="Black" and (c==a-1) and abs(d-b)==1:  
        return True
    return False
        
def isOpponentPiece(board, c,d, current_player):  #check if the target square is opposite color/opponent's piece
    if board[c][d]!=0:  
        if board[c][d].color!=current_player:
            return True
    return False

def isTargetValidForward(board, a,b, c, d, current_player):
    #check if the target square is one square forward in the same file
    if current_player=="White" and c==a+1 and b==d :
        return True
    elif current_player=="Black" and c==a-1 and b==d:
        return True
    return False

def isSquareEmpty(board, c, d):
    if board[c][d]==0:
        return True
    return False


def valid_Pawn(board, a,b,c,d, current_player):

    if isTargetValidPawnDiag(board,a,b,c,d, current_player):  #checks if the target square is diagonal to the current square
        if isOpponentPiece(board,c,d,current_player):  #checks if there is an opponent color piece
            return True
        else:
            return False

    
    # Checks if target square is 1 in front of pawn
    elif isTargetValidForward(board, a,b,c,d, current_player):
        if isSquareEmpty(board, c,d):
            return True
        else:
            return False
    elif current_player == "White" and a==1 and isTargetValidForward(board, a+1, b, c, d, current_player):
        if isSquareEmpty(board, c,d) and isSquareEmpty(board, c-1, d):
            return True
        else:
            return False
    elif current_player == "Black" and a==6 and isTargetValidForward(board, a-1, b, c, d, current_player):
        if isSquareEmpty(board, c,d) and isSquareEmpty(board, c+1, d):
            return True
        else:
            return False
    return False

#***************  Valid ROOK function*********************

#SameFile: checks if target square is on the same file
def sameFile(board, a,b,c,d,current_player):
    if b==d:
        return True
    return False

def loopFileValid(board, a,b,c,d,current_player): #checks if all the squares, looping through the same file are empty(valid to move)
    col=d
    if c > a:   #moving forward-> increasing indices-> positive "for" lop
        start=a+1
        end=c+1
        step=1

    elif c < a:   #moving downwards-> decreasing indices-> negative "for" lop
        start=a-1
        end=c-1
        step=-1
    for i in range(start,end,step):
        if board[i][col]!=0:  #instead if the square is occupied
            if (i == end-1 or i == end+1) and board[i][col].color!=current_player:  #check if the square is occupied by opponent
                return True
            else:
                return False
    return True    #if the squares are empty, return True-> can(valid) move

def sameRank(board, a,b,c,d,current_player):
    if a==c:
        return True
    return False

def loopRankValid(board,a,b,c,d,current_player):
    row=c
    if d>b:
        start=b+1
        end=d+1
        step=1
    elif d<b:
        start=b-1
        end=d-1
        step=-1

    for j in range(start, end, step):
        if board[row][j]!=0:
            if (j==end-1 or j==end+1) and board[row][j].color!=current_player:
                return True
            else:
                return False
    return True


def valid_Rook(board, a,b,c,d,current_player):
    if sameFile(board, a,b,c,d,current_player):
        if loopFileValid(board, a,b,c,d,current_player):
            return True
    elif sameRank(board,a,b,c,d,current_player):
        if loopRankValid(board,a,b,c,d,current_player):
            return True
    return False

#***************  Valid BISHOP function *********************

def isDiagonal(a,b,c,d):
    if abs(c-a)==abs(d-b):
        return True
    #print("Bishop only moves diagonally")
    return False

def loopDiagonalValid(board,a,b,c,d,current_player):
    if c>a and d>b:
        start_row=a+1
        end_row=c+1
        step_row=1

        start_col=b+1
        end_col=d+1
        step_col=1

    elif c>a and d<b:
        start_row=a+1
        end_row=c+1
        step_row=1

        start_col=b-1
        end_col=d-1
        step_col=-1

    elif c<a and d>b:
        start_row=a-1
        end_row=c-1
        step_row=-1

        start_col=b+1
        end_col=d+1
        step_col=1

    elif c<a and d<b:
        start_row=a-1
        end_row=c-1
        step_row=-1

        start_col=b-1
        end_col=d-1
        step_col=-1

    for row in range(start_row, end_row, step_row):
        for col in range(start_col, end_col, step_col):
            if not isDiagonal(row, col, start_row, start_col):
                #if a == 7 and b == 5:
                    #print(f"diag:row is {row}, end_row is {end_row}, col is {col}, end_col is {end_col}, color is {board[row][col].color}, player is {current_player}")
                continue
            if board[row][col]!=0:
                if (row==end_row+1 or row==end_row-1) and (col==end_col+1 or col==end_col-1) and board[row][col].color!=current_player:
                    return True
                else:
                    #if a == 7 and b == 5:
                        #print(f"row is {row}, end_row is {end_row}, col is {col}, end_col is {end_col}, color is {board[row][col].color}, player is {current_player}")
                    return False
    return True


def valid_Bishop(board,a,b,c,d,current_player):
    #print(f"Checking diagonal from {a,b} to {c,d}")
    if isDiagonal(a,b,c,d):
        #print(f"Checking loop diagonal from {a,b} to {c, d}")
        if loopDiagonalValid(board,a,b,c,d,current_player):
            #print(f"Loop diagonal valid from {a,b} to {c,d}")
            return True
    return False
    # If not a valid diagonal, return false
    # else return loopDiagonalValid(...)

# ***************  Valid KNIGHT function*********************

def KnightValidMove(board, a,b,c,d,current_player):
    validSquares=[(1,2),(2,1),(-1,2),(-2,1),(2,-1),(-2,-1),(-1,-2),(1,-2)]
    if (c-a, d-b) in validSquares:
        return True
    #print("Invalid move for Knight")
    return False

def isTargetSqEmpty(board, a,b,c,d,current_player): #board[c][d] here is 0 because it's empty
    if not isSquareEmpty(board,c,d):
        if board[c][d].color!=current_player:
            return True
        else:
            return False
    return True


def valid_Knight(board, a,b,c,d,current_player):
    if KnightValidMove(board, a,b,c,d,current_player):
        if isTargetSqEmpty(board, a,b,c,d,current_player):
            return True
    return False

#***************  Valid QUEEN function*********************

def valid_Queen(board, a, b, c, d, current_player):
    if valid_Rook(board, a, b, c, d, current_player) or valid_Bishop(board, a, b, c, d, current_player):
        return True
    #print("Invalid move for a Queen")
    return False

def KingValidMove(board, a, b, c, d, current_player):
    validKinSq=[(1,0), (-1,-1), (0,-1), (1,-1), (-1,0), (0,1), (1,1),(-1,1)]
    if (c-a, d-b) in validKinSq:
        return True
    #print("Invalid move for King")
    return False

def valid_King(board, a, b, c, d, current_player):
    if KingValidMove(board, a, b, c, d, current_player) and isTargetSqEmpty(board, a,b,c,d,current_player):
        return True
    #print("Invalid move for King")
    return False



def check(board, white_king_coords, black_king_coords, current_player):
    # for piece in board:
    # if piece is opponent's:
    # if piece has validPawn/Rook/etc on target_square=white_king_coords/black_king_coords:
    # return True
    # if loop completes and nothing returned true, we assume no opponent piece has line of sight to our King
    # and we can return False (not in check)

    
    for i in range(8):    #loop over all squares on board
        for j in range(8):
            if board[i][j]!=0 and board[i][j].color!=current_player:  #check if the square is occupied by opponent

                if board[i][j].color=="White":  #check if any of the white pieces can attack black king
                    if can_move(board[i][j].name ,board, i, j, black_king_coords[0], black_king_coords[1], "White"):
                        return True
                    
                elif board[i][j].color=="Black":   #check if any of the black pieces can attack white king
                    if can_move(board[i][j].name, board, i, j, white_king_coords[0], white_king_coords[1], "Black"):
                        return True
    return False


# def any_checkmate(board, a, b, c, d, current_player):
#     if check(board,a, b, c, d, current_player):
#         pass

class Piece:
    def __init__(self, Name, Color, Points):
        self.name=Name
        self.color=Color
        self.points=Points

def can_move(name, board, a, b, c, d, current_player ):
    if name=="Pawn":
        return valid_Pawn(board, a, b, c, d, current_player)  
    
    if name=="Rook":
        return valid_Rook(board,a,b,c,d,current_player)  
    
    if name=="Bishop":
        return valid_Bishop(board,a,b,c,d,current_player)
    
    if name=="Knight":
        return valid_Knight(board,a,b,c,d,current_player)
    
    if name=="Queen":
        return valid_Queen(board,a,b,c,d,current_player)
    
    if name=="King":
        return valid_King(board,a,b,c,d,current_player)



def initial_board():
    board=[
        [Piece("Rook", "White", 5), Piece("Knight", "White", 3), Piece("Bishop", "White", 3), Piece("King", "White", 88), Piece("Queen", "White", 9), Piece("Bishop", "White", 3), Piece("Knight", "White", 3), Piece("Rook", "White", 5)], #1-> white; -1-> black
        [Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1), Piece("Pawn", "White", 1)], 
        [0, 0, 0, 0, 0, 0, 0, 0],          
        [0, 0, 0, 0, 0, 0, 0, 0],          
        [0, 0, 0, 0, 0, 0, 0, 0],          
        [0, 0, 0, 0, 0, 0, 0, 0],
        [Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1), Piece("Pawn", "Black", -1)],          
        [Piece("Rook", "Black", -5), Piece("Knight", "Black", -3), Piece("Bishop", "Black", -3), Piece("King", "Black", -88), Piece("Queen", "Black", -3), Piece("Bishop", "Black", -3), Piece("Knight", "Black", -3), Piece("Rook", "Black", -3)]] 

    return board  


#Display board function
def display_board(board):
    for i in range(8):
        display=[]
        display.append(f"{i}|")
        for j in range(8):
            piece=board[i][j]   #i do not want to "update" the board itself. so created a new variable that points to the same board object 

            if piece==0: 
                display.append("_")
            elif piece.color=="White":

                if piece.name=="Rook":
                    display.append(u'\u2656')
                    # after this the board[i][j] is updated as the string

                elif piece.name=="Bishop":
                    display.append(u'\u2657')
                
                elif piece.name=="Knight":
                    display.append(u'\u2658')
                
                elif piece.name=="Queen":
                    display.append(u'\u2655')
                
                elif piece.name=="King":
                    display.append(u'\u2654')
                
                elif piece.name=="Pawn":
                    display.append(u'\u2659')
                
            elif piece.color=="Black":

                if piece.name=="Rook":
                    display.append(u'\u265C')
                
                elif piece.name=="Knight":
                    display.append(u'\u265E')
                
                elif piece.name=="Bishop":
                    display.append(u'\u265D')
                
                elif piece.name=="Queen":
                    display.append(u'\u265B')
                
                elif piece.name=="King":
                   display.append(u'\u265A')
                
                elif piece.name=="Pawn":
                   display.append(u'\u265F')

        print(" ".join(display))
    # print("  u'\U+203E', u'\U+203E', u'\U+203E', u'\U+203E' ")

def validRange(x):
    valid_range=[0,1,2,3,4,5,6,7]
    if x in valid_range:
        return True
    return False


#Main Game Loop

def play_game():
    gameRunning=False

    game_board=initial_board()  #initialise the board
    display_board(game_board)   #print the board  -> it's printing the matrix with objects
    #define another function to display board
    
    current_player="White"
    print(f"{current_player}\'s turn")

    white_king_coords = (0,3)
    black_king_coords = (7,3)


    while gameRunning: #while this variable is True, the game loop will run. i have initialised ths as true outside of this

        try:
            input_string_current=input("Enter the current square coordinates ( separated by comma) : ")

            a=int(input_string_current.split(",")[0])   #a,b will go as the indices of board. they must be integers
            b=int(input_string_current.split(",")[1])

            if not (validRange(a) and validRange(b)):
                print(f"{a}, {b} squares are out of the range of board")
                continue

            input_string_target=input("Enter the target square coordinates ( separated by comma) : ")

            c=int(input_string_target.split(",")[0])
            d=int(input_string_target.split(",")[1])

            if not (validRange(c) and validRange(d)):
                print(f"{c}, {d} squares are out of the range of board")
                continue

        except ValueError:
            if input_string_current=="exit":
                print("Game Exited")
                return None
            print("Invalid input")
            continue
        except IndexError:
            print("Invalid input")
            continue


        if a == c and b == d:
            print("Cannot move piece to same square")
            continue

        if game_board[a][b]==0:  #checks if there's a piece on the current sq
            print(f"board[a][b]: {game_board[a][b]}")
            print("Invalid move")
            continue     #goes back to the while loop

        if game_board[a][b].color!=current_player:
            print(f"{current_player} cannot move {game_board[a][b].color} piece")
            continue


        if can_move(game_board[a][b].name, game_board, a,b, c,d, current_player):   #for (1,0)-> (2,0) it is returning True as it should
            if check(game_board, a, b, c, d, current_player, white_king_coords, black_king_coords):
                print("Check: Invalid move")
                
            if game_board[a][b].name == "King":
                if current_player=="White":
                    white_king_coords=(c,d)
                else:
                    black_king_coords=(c,d)
            game_board[c][d]=game_board[a][b]
            game_board[a][b]=0

            if current_player=="White":
                current_player="Black"
            else:
                current_player="White"

            print(f"{current_player}'s turn")
        else:
            print("Invalid move")
            print(f"{current_player}'s turn")

        
        display_board(game_board)


    return None


# if __name__ == "__main__":
    # play_game()