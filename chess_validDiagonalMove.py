board=[[2, 3, 4, 5, 6, 4, 3, 2],  #global variable-> to keep updating the state of the board
    [1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],          
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1],          
    [-2, -3, -4, -5, -6, -4, -3, -2]]

def validMove_DiagonalPositive(player,original_square,target_square): #White: (3,2)-> (6,5)

    a,b=original_square #unpacks coordinates of original_square into var a & b
    c,d=target_square
    # current_board=board #create the updated version of board as the current_board

    if player in "Ww":
        print('white\'s turn')

        for row in range(a+1,c+1):  #loops all indexes along x axis ie each column index
            for col in range(b+1,d+1):  #loops along y axis ie each row index
                if board[row][col]!=0:    #selects diagonal sq
                    return False
        return True

    if player in "Bb":
        print('black moves')
        for row in range(a,c-1,-1):  #loops all indexes along x axis ie each column index
            for col in range(b,d-1,-1):  #loops along y axis ie each row index
                if board[row][col]!=0:    #selects diagonal sq
                    return False
        return True
    
# validMove_DiagonalPositive("b" , (5,4), (3,2))

def validMove_DiagonalNegative(player:str,current_square,target_square):  #takes input player=W/B

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if player in "Ww":
        print('white\'s turn')

        for row in range(a,c-1,-1):  #loops all indexes along x axis ie each column index
            for col in range(b,d-1,-1):  #loops along y axis ie each row index
                if board[row][col]!=0:    #selects diagonal sq
                    return False
        return True

    if player in "Bb":
        print('black moves')
        for row in range(a+1,c+1):  #loops all indexes along x axis ie each column index
            for col in range(b+1,d+1):  #loops along y axis ie each row index
                if board[row][col]!=0:    #selects diagonal sq
                    return False
        return True