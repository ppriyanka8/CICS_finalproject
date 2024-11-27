#Main Game Code

def validMove_Parallel(board, current_square,target_square):  #checks if the squares parallely forward to the current square are all empty

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if b!=d:   #to move in a particular rank, b needs to be same as d
        print("Invalid Move: b==d not in the same file")
        return False
    col=d    #only other condition is that b is same as d-> assign the final col as d

    if c>a:   #looing forward in positive direction (for white)
        print("c>a")
        start=a+1
        end=c+1
        step=1
        print(f"a+1: {a+1}")

    else:   #otherwise go negative (for black)
        start=a-1
        end=c-1
        step=-1

    for row in range(start,end,step):   #starts checking from a+1, because a is the currrent position, tht will never be empty square
        if board[row][col]!=0:

            # are we at the target square? If so, if the piece belongs to opposite player, valid move. Otherwise, invalid move.
            if row==c:
                print(f"a,b: {a,b}")
                print(type(board[a][b]))
                print(type(board[c][d]))
                #this function will not work for a pawn. will only work for rooks and queen
                if board[a][b].name=="Rook" or "Queen":

                    if board[a][b].color=="White" and board[c][d].color=="Black": #[(5,0) should store an object, instead storing an int] #check if the current sq piece is white and target is black
                        print("White Captured a black piece")
                        return True
                    elif board[a][b].color=="Black" and board[c][d].color=="White":
                        print("Black Captured a white piece")
                        return True
                    else:  
                        return False
                    
                elif board[a][b].name=="Pawn":
                    # if d-1<0:

                    if board[a][b].color=="White" and (board[c][d+1]=="Black" or board[c][d-1]=="Black"):
                        print("White Captured a black piece")
                        return True
                    elif board[a][b].color=="Black" and (board[c][d+1]=="White" or board[c][d-1]=="White"):
                        print("Black Captured a white piece")
                        return True
                    else:
                        return False

                else:
                    return False
            else:
                    print("validMoveParallel: board[row][col] == 0 that means can move further")
    return True



#Account in for the diagonal case here, where if it's the opponent's piece, it can move. (capturing basically means moving it there and removing that(opponent's) piece altogether)
def valid_Pawn(board, current_sq,target_sq):
    #pawn can only move in a file
    a,b=current_sq #unpacks coordinates of original_square into var a & b
    c,d=target_sq

    #It needs to see first if there are any opponent pieces on the diagonal'
    if (d-b==1 or d-b==-1) and board[c][d]!=0:  #can only go to the diagonal capture if it's a non-empty piece
        print("d-b==1")
        if board[a][b].color!=board[c][d].color:   #if it's the opposite color
            print("target square piece is different colored")
            if c-a==1:  #if c-a is positive, that means it's white's turn
            #can move -> capture piece
                print("White pawn caputures target sq piece")
                return True    
        
            elif c-a==-1:
                print("Black pawn caputures target sq piece")
                return True
    if b==d: #now check if you're moving in a straight line  [It's directly entering this because b==d]
        if board[c][d]==0:  #check if target square is empty
            return True 
        else:
            print("Invalid move for pawn because the target square is already occupied")
            return False



class Piece:
    def __init__(self, Name, Color, Points):
        self.name=Name
        self.color=Color
        self.points=Points

    def can_move(self, board, original_sq,target_sq ):
        if self.name=="Pawn":
            return valid_Pawn(board, original_sq,target_sq)  #it returns whatever gets returned from that fn
        
        if self.name=="Rook":
            return valid_Rook(original_sq,target_sq)  #the function valid_rook is not defined outside the scope of this class. do i need to pass as an argument in can_move method
        
    #     if self.name=="Bishop":
    #         return None
        
    #     if self.name=="Knight":
    #         return None
        
    #     if self.name=="Queen":
    #         return None
        
    #     if self.name=="King":
    #         return None




def initial_board():
    board=[
        [Piece("Rook", "White", 5), Piece("Knight", "White", 3), Piece("Knight", "White", 3), Piece("Queen", "White", 9), Piece("King", "White", 88), Piece("Knight", "White", 3), Piece("Bishop", "White", 3), Piece("Rook", "White", 5)], #1-> white; -1-> black
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
        for j in range(8):
            piece=board[i][j]   #i do not want to "update" the board itself. so created a new variable that points to the same board object 

            if piece==0: 
                display.append("___")
            elif piece.color=="White":

                if piece.name=="Rook":
                    display.append("W_R")
                    # after this the board[i][j] is updated as the string

                elif piece.name=="Bishop":
                    display.append("W_B")
                
                elif piece.name=="Knight":
                    display.append("W_K")
                
                elif piece.name=="Queen":
                    display.append("W_Q")
                
                elif piece.name=="King":
                    display.append("W_K")
                
                elif piece.name=="Pawn":
                    display.append("W_P")
                
            elif piece.color=="Black":

                if piece.name=="Rook":
                    display.append("B_R")
                
                elif piece.name=="Knight":
                    display.append("B_Kn")
                
                elif piece.name=="Bishop":
                    display.append("B_B")
                
                elif piece.name=="Queen":
                    display.append("B_Q")
                
                elif piece.name=="King":
                   display.append("B_K")
                
                elif piece.name=="Pawn":
                   display.append("B_P")

        print(" ".join(display))


#Main Game Loop

def play_game():
    gameRunning=True

    game_board=initial_board()  #initialise the board
    display_board(game_board)   #print the board  -> it's printing the matrix with objects
    #define another function to display board
    
    current_player="white"
    print(f"{current_player}\'s turn")


    while gameRunning: #while this variable is True, the game loop will run. i have initialised ths as true outside of this

        input_string_current=input("Enter the current square coordinates ( separated by comma) : ")
        a=int(input_string_current.split(",")[0])   #a,b will go as the indices of board. they must be integers
        b=int(input_string_current.split(",")[1])

        input_string_target=input("Enter the target square coordinates ( separated by comma) : ")
        c=int(input_string_target.split(",")[0])
        d=int(input_string_current.split(",")[1])

         #can_move is a method defined under the class Piece
        if game_board[a][b]==0:
            print(f"board[a][b]: {game_board[a][b]}")
            print("Invalid move")
            continue

        print("Before checking valid move. A,B=" + str(game_board[a][b]))
        print("before check can move: A:" + str(a) + ", B:" + str(b))
        if (game_board[a][b]).can_move(game_board, (a,b), (c,d)):   #for (1,0)-> (2,0) it is returning True as it should
                #update the board 
            game_board[c][d]=game_board[a][b]
            game_board[a][b]=0
            print(f"after updating current_sq: {game_board[a][b]}")
            print(f"after updating , updated_sq: {game_board[c][d].name}")
        
        else:
            gameRunning=False

        display_board(game_board)

        # if current_player=="white":
        #     current_player="black"
        # else:
        #     current_player="white"
        # gameRunning=False


    return None

play_game()