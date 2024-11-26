def validMove_ParallelPositive(player,current_square,target_square):  #takes input player=W/B

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if player in "Ww":          #see if it's white's turn
        print('white\'s turn')
        if c>a:
            for row in range(a+1,c+1):   #starts checking from a+1, because a is teh currrent position, tht will never be empty square
                print(f'row: {row}')   #loops all indexes along x axis ie each column index : for a,b=(1,1) c,d=(2,1) started with a=1, c=

                if b!=d:   # if b=d, range for col variable will be 0, it will not access that var
                    for col in range(b+1,d+1):
                        print("entering col for loop")
                        print(f'col: {col}')  #loops along y axis ie each row index
                        if board[row][col]!=0:    
                            print("Entering if condition")
                            return False
                else:
                    col=d
            print('can move')
            print(row, col)

            return True
        print("Invalid move")
    
    if player in "Bb":
        print('black moves')
        if c<a:
            for row in range(a,c-1,-1): #loops all indexes along x axis ie each column index
                print(f'row: {row}')

            if b!=d:     # if b=d, range for col variable will be 0, it will not access that var
                for col in range(b,d-1,-1):  #loops along y axis ie each row index
                    print(f'row: {row}')
                    if board[row][col]!=0:
                        return False
            else:    # it cannot land on a different column value if it's going in a straight line
                col=d
                    
            print('can move')
            print(row, col)
            return True
        print("Invalid move")
    
# validMove_ParallelPositive("B", (6,2), (5,2)) 

def validMove_ParallelNegative(player,current_square,target_square):  #(5,1)-> (2,1) (white) For black: (2,1)-> (5,1)

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if player in "Ww":          #see if it's white's turn
        print('white\'s turn')
        if a>c:   #check if it's only going in negative direction for W
            for row in range(a,c-1,-1):   #starts checking from a+1, because a is teh currrent position, tht will never be empty square
                print(f'row: {row}')   #loops all indexes along x axis ie each column index : for a,b=(1,1) c,d=(2,1) started with a=1, c=

                if b!=d:   # if b=d, range for col variable will be 0, it will not access that var
                    for col in range(b+1,d+1):
                        print("entering col for loop")
                        print(f'col: {col}')  #loops along y axis ie each row index
                        if board[row][col]!=0:    #fault here: entering if conditon on the current sq coord
                            print(row, col)
                            print("Entering if condition")
                            return False
                else:
                    col=d
            print('can move')
            print(row, col)

            return True
        
        print("Invalid move")
    
    if player in "Bb":
        print('black moves')
        if a<c:   #check if it's only going in negative direction for B
            for row in range(a+1,c+1,1): #loops all indexes along x axis ie each column index
                print(f'row: {row}')

            if b!=d:     # if b=d, range for col variable will be 0, it will not access that var
                for col in range(b+1,d+1,1):  #loops along y axis ie each row index
                    print(f'row: {row}')
                    if board[row][col]!=0:
                        return False
            else:    # it cannot land on a different column value if it's going in a straight line
                col=d
                    
            print('can move')
            print(row, col)
            return True
        
        print("Invalid move")
# validMove_ParallelNegative("B", (5,1),(2,1))

def validMove_NormalPositive(player:str,current_square,target_square):  #takes input player=W/B

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if player in "Ww":          #see if it's white's turn
        print('white\'s turn')
    
    if player in "Bb":
        print("black\'s turn")
    if a!=c:
        return "Invalid move"
    row=c
    for col in range(b+1,d+1,1):
        # print("entering col for loop")
        # print(f'col: {col}')  #loops along y axis ie each row index

        if board[row][col]!=0:    #fault here: entering if conditon on the current sq coord
            print(row, col)
            
            return False

    
    print("can move")
    print(row, col)
    return True

def validMove_NormalNegative(player:str,current_square,target_square):  #takes input player=W/B

    a,b=current_square #unpacks coordinates of original_square into var a & b
    c,d=target_square

    if player in "Ww":          #see if it's white's turn
        print('white\'s turn')
    
    if player in "Bb":
        print("black\'s turn")
    if a!=c:
        return "Invalid Move"
    row=c
    for col in range(b,d-1,-1):
        # print("entering col for loop")
        # print(f'col: {col}')  #loops along y axis ie each row index

        if board[row][col]!=0:    #fault here: entering if conditon on the current sq coord
            print(row, col)
            
            return False

    
    print("can move")
    print(row, col)
    return True