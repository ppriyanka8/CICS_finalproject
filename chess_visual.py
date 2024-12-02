import sys
import pygame
import chess_NEW as c

   #Dimensions for chessboard
WIDTH, HEIGHT= 800,800
SQUARE_SIZE=WIDTH//8
# WHITE=(255,255,255) #RGB for white
# BLACK=(0,0,0) #RGB for black
LIGHT_COLOR=(240,217,181)
DARK_COLOR=(181,136,99)

pygame.init()   #initialise all pygame modules
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #initialise screen
pygame.display.set_caption("2-Player Chess")

#white pieces
W_Pawn=pygame.image.load("CICS_finalproject/pieces-basic-png/white-pawn.png")
W_Rook=pygame.image.load("CICS_finalproject/pieces-basic-png/white-rook.png")
W_Bishop=pygame.image.load("CICS_finalproject/pieces-basic-png/white-bishop.png")
W_Knight=pygame.image.load("CICS_finalproject/pieces-basic-png/white-knight.png")
W_Queen=pygame.image.load("CICS_finalproject/pieces-basic-png/white-queen.png")
W_King=pygame.image.load("CICS_finalproject/pieces-basic-png/white-king.png")

B_Pawn=pygame.image.load("CICS_finalproject/pieces-basic-png/black-pawn.png")
B_Rook=pygame.image.load("CICS_finalproject/pieces-basic-png/black-rook.png")
B_Bishop=pygame.image.load("CICS_finalproject/pieces-basic-png/black-bishop.png")
B_Knight=pygame.image.load("CICS_finalproject/pieces-basic-png/black-knight.png")
B_Queen=pygame.image.load("CICS_finalproject/pieces-basic-png/black-queen.png")
B_King=pygame.image.load("CICS_finalproject/pieces-basic-png/black-king.png")


W_Pawn=pygame.transform.scale(W_Pawn,(SQUARE_SIZE,SQUARE_SIZE))
W_Rook=pygame.transform.scale(W_Rook,(SQUARE_SIZE,SQUARE_SIZE))
W_Bishop=pygame.transform.scale(W_Bishop,(SQUARE_SIZE,SQUARE_SIZE))
W_Knight=pygame.transform.scale(W_Knight,(SQUARE_SIZE,SQUARE_SIZE))
W_Queen=pygame.transform.scale(W_Queen,(SQUARE_SIZE,SQUARE_SIZE))
W_King=pygame.transform.scale(W_King,(SQUARE_SIZE,SQUARE_SIZE))

B_Pawn=pygame.transform.scale(B_Pawn,(SQUARE_SIZE,SQUARE_SIZE))
B_Rook=pygame.transform.scale(B_Rook,(SQUARE_SIZE,SQUARE_SIZE))
B_Bishop=pygame.transform.scale(B_Bishop,(SQUARE_SIZE,SQUARE_SIZE))
B_Knight=pygame.transform.scale(B_Knight,(SQUARE_SIZE,SQUARE_SIZE))
B_Queen=pygame.transform.scale(B_Queen,(SQUARE_SIZE,SQUARE_SIZE))
B_King=pygame.transform.scale(B_King,(SQUARE_SIZE,SQUARE_SIZE))

class Piece:
    def __init__(self, Name, Color, Points):
        self.name=Name
        self.color=Color
        self.points=Points

    def can_move(self, board, a, b, c_pos, d, current_player ):
        if self.name=="Pawn":
            return c.valid_Pawn(board, a, b, c_pos, d, current_player)  #it returns whatever gets returned from that fn
        
        if self.name=="Rook":
            return c.valid_Rook(board,a,b,c_pos,d,current_player)  #the function valid_rook is not defined outside the scope of this class. do i need to pass as an argument in can_move method
        
        if self.name=="Bishop":
            return c.valid_Bishop(board,a,b,c_pos,d,current_player)
        
        if self.name=="Knight":
            return c.valid_Knight(board,a,b,c_pos,d,current_player)
        
        if self.name=="Queen":
            return c.valid_Queen(board,a,b,c_pos,d,current_player)
        
        if self.name=="King":
            return c.valid_King(board,a,b,c_pos,d,current_player)

#Display board function
def display_chessboard(board, selected_x, selected_y, current_player):
    # Draw the chessboard and pieces using the disaplay board logic
    for i in range(8):
        for j in range(8):
            x_pos=j*SQUARE_SIZE
            y_pos=i*SQUARE_SIZE
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen,LIGHT_COLOR,(x_pos,y_pos,SQUARE_SIZE,SQUARE_SIZE))
            else:
                pygame.draw.rect(screen,DARK_COLOR,(x_pos,y_pos,SQUARE_SIZE,SQUARE_SIZE))

            if current_player == "Black":
                piece=board[i][j]   #i do not want to "update" the board itself. so created a new variable that points to the same board object 
            else:
                piece=board[7-i][7-j]

            if piece==0: 
                continue
            if piece.color=="White":

                if piece.name=="Rook":
                    screen.blit(W_Rook, (x_pos, y_pos))
                    # after this the board[i][j] is updated as the string

                elif piece.name=="Bishop":
                    screen.blit(W_Bishop, (x_pos, y_pos))
                
                elif piece.name=="Knight":
                    screen.blit(W_Knight, (x_pos, y_pos))
                
                elif piece.name=="Queen":
                    screen.blit(W_Queen, (x_pos, y_pos))
                
                elif piece.name=="King":
                    screen.blit(W_King, (x_pos, y_pos))
                
                elif piece.name=="Pawn":
                    screen.blit(W_Pawn, (x_pos, y_pos))
                
            elif piece.color=="Black":

                if piece.name=="Rook":
                    screen.blit(B_Rook, (x_pos, y_pos))
                
                elif piece.name=="Knight":
                    screen.blit(B_Knight, (x_pos, y_pos))
                
                elif piece.name=="Bishop":
                    screen.blit(B_Bishop, (x_pos, y_pos))
                
                elif piece.name=="Queen":
                    screen.blit(B_Queen, (x_pos, y_pos))
                
                elif piece.name=="King":
                   screen.blit(B_King, (x_pos, y_pos))
                
                elif piece.name=="Pawn":
                   screen.blit(B_Pawn, (x_pos, y_pos))
    
    if selected_x != None and selected_y != None:
        dark_surface = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
        dark_surface.set_alpha(100)
        dark_surface.fill((0,0,0))
        if current_player == "Black":
            screen.blit(dark_surface, (selected_y*SQUARE_SIZE, selected_x*SQUARE_SIZE))
        else:
            screen.blit(dark_surface, ((7-selected_y)*SQUARE_SIZE, (7-selected_x)*SQUARE_SIZE))

def move_piece(board,a,b,c_pos,d,current_player):
    if board[a][b].name == "King":
        if current_player=="White":
            global white_king_coords
            white_king_coords=(c_pos,d)
        else:
            global black_king_coords
            black_king_coords=(c_pos,d)
    
    board[c_pos][d]=board[a][b]
    board[a][b]=0

def is_in_checkmate(board, current_player):
    in_check = True

    # For every starting square on board
    for x in range(8):
        for y in range(8):
            item = board[x][y]
            # If square has this player's piece
            if item != 0 and item.color == current_player:
                # For every target square in board
                for i in range(8):
                    for j in range(8):
                        # If target square is same as current square, skip
                        if x == i and y == j:
                            continue
                        # If the target square cannot be moved to, skip
                        if not item.can_move(board, x, y, i, j, current_player):
                            continue
                        # Otherwise, move the piece, see if we're in check still, move it back. Return False (not in checkmate)
                        # if the move got us out of check.
                        item_at_target = board[i][j]
                        move_piece(game_board, x, y, i, j, current_player)
                        # If the current player's king is in check, save that information
                        if not c.check(game_board, white_king_coords, black_king_coords, current_player):
                            print(f"{current_player} moving from {x,y} to {i,j} gets us out of check")
                            in_check = False
                        # Always move the piece back. We don't want to make a move on behalf of the player, we're just testing
                        # for checkmate.
                        move_piece(game_board, i, j, x, y, current_player)
                        board[i][j] = item_at_target

                        if not in_check:
                            return False
    print("Couldnt get out of check")
    return True # We iterated through every piece and none of their moves got us out of check

def can_en_passant(board, selected_x, selected_y, x, y, current_player):
    piece = board[selected_x][selected_y]
    if piece == 0:
        return False
    if last_move[0] == 0:
        return False
    if piece.color == "White" and current_player=="White":
        if selected_x==5:
            if (y == selected_y + 1 or y == selected_y - 1) and x == selected_x + 1:
                if last_move[0].name == "Pawn" and last_move[0].color == "Black" and last_move[2][1] == y and abs(last_move[2][0]-last_move[1][0])==2:
                    return True
    elif piece.color == "Black" and current_player=="Black":
        if selected_x==3:
            if (y == selected_y + 1 or y == selected_y - 1) and x == selected_x - 1:
                if last_move[0].name == "Pawn" and last_move[0].color == "White" and last_move[2][1] == y and abs(last_move[2][0]-last_move[1][0])==2:
                    return True

def can_castle(board, selected_x, selected_y, x, y, current_player):
    piece = board[selected_x][selected_y]
    if piece == 0:
        return False
    elif piece.name != "King":
        return False
    elif piece.color != current_player:
        return False
    # If we are in check, we can't castle
    elif c.check(game_board, white_king_coords, black_king_coords, current_player):
        return False
    else:
        # If your king has moved already, it can't castle
        if current_player=="White" and white_king_has_moved:
            return False
        elif current_player=="Black" and black_king_has_moved:
            return False
    
    # If selected square isn't one you can castle to
    if abs(y-selected_y) != 2 or x != selected_x:
        return False
    
    # First check all squares between are empty
    if y-selected_y == -2:
        # Also check if the rook has moved.
        # And check if any of the open spots are in check
        if current_player == "Black":
            if black_kingside_rook_has_moved:
                return False
            if c.check(game_board, white_king_coords, (7,2), current_player):
                return False
        else:
            if white_kingside_rook_has_moved:
                return False
            if c.check(game_board, (0,2), black_king_coords, current_player):
                return False
        coords_to_check = ((x,1),(x,2))
    else:
        # Also check if the rook has moved
        if current_player == "Black":
            if black_queenside_rook_has_moved:
                return False
            if c.check(game_board, white_king_coords, (7,4), current_player):
                return False
        else:
            if white_queenside_rook_has_moved:
                return False
            if c.check(game_board, (0,4), black_king_coords, current_player):
                return False
        coords_to_check = ((x,4),(x,5),(x,6))
    
    for coord in coords_to_check:
        if board[coord[0]][coord[1]] != 0:
            return False
        
    return True

def get_castling_rook(board, y, current_player):
    if current_player == "White":
        if y == 1:
            return board[0][0]
        else:
            return game_board[0][7]
    else:
        if y == 1:
            return game_board[7][0]
        else:
            return game_board[7][7]

def get_castling_rook_start_coords(y, current_player):
    if current_player == "White":
        if y == 1:
            return (0,0)
        else:
            return (0,7)
    else:
        if y == 1:
            return (7,0)
        else:
            return (7,7)

def get_castling_rook_end_coords(y, current_player):
    if current_player == "White":
        if y == 1:
            return (0,2)
        else:
            return (0,4)
    else:
        if y == 1:
            return (7,2)
        else:
            return (7,4)
clock = pygame.time.Clock()

def mouse_click(current_player):
    mouse_x,mouse_y=pygame.mouse.get_pos()

    y_pos=mouse_y//SQUARE_SIZE
    x_pos=mouse_x//SQUARE_SIZE

    if current_player == "Black":
        return y_pos, x_pos
    else:
        return 7-y_pos, 7-x_pos
    # print(f"Clicked on square: ({row},{col})")

def display_promotion_pieces(current_player):
    dark_surface = pygame.Surface((SQUARE_SIZE*4,SQUARE_SIZE))
    dark_surface.set_alpha(255)
    if current_player == "White":
        dark_surface.fill((0,0,0))
        dark_surface.blit(W_Knight, (0, 0))
        dark_surface.blit(W_Bishop, (SQUARE_SIZE, 0))
        dark_surface.blit(W_Rook, (2*SQUARE_SIZE, 0))
        dark_surface.blit(W_Queen, (3*SQUARE_SIZE, 0))
    else:
        dark_surface.fill((255,255,255))
        dark_surface.blit(B_Knight, (0, 0))
        dark_surface.blit(B_Bishop, (SQUARE_SIZE, 0))
        dark_surface.blit(B_Rook, (2*SQUARE_SIZE, 0))
        dark_surface.blit(B_Queen, (3*SQUARE_SIZE, 0))
    screen.blit(dark_surface, (0, 3*SQUARE_SIZE))

def show_winner_text():
    # Initialize font
    pygame.font.init()
    font = pygame.font.SysFont(None, 72, bold=True)  # 72 is the font size
    
    # Render the text
    if white_won:
        text = font.render("White won!", True, (43, 138, 114))  # White color
    elif black_won:
        text = font.render("Black won!", True, (43, 138, 114))  # White color
    
    # Get the text's rectangle
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    # Blit the text to the screen
    screen.blit(text, text_rect)

# *****************
game_board=c.initial_board()  #initialise the board
current_player="White"

white_king_coords = (0,3)
white_king_has_moved = False
white_queenside_rook_has_moved = False
white_kingside_rook_has_moved = False
black_king_coords = (7,3)
black_king_has_moved = False
black_queenside_rook_has_moved = False
black_kingside_rook_has_moved = False

game_display_running=True
selected_x = None
selected_y = None
current_player_in_check=False
is_promoting=False
promoting_pawn_pos=None
promoting_color=None
last_move=[0,0,0]
white_won = False
black_won = False

while game_display_running:
    # gameRunning=True
    display_chessboard(game_board, selected_x, selected_y, current_player)   #print the board  -> it's printing the matrix with objects
    if is_promoting:
        display_promotion_pieces(current_player)
    if white_won or black_won:
        show_winner_text()
    #define another function to display board
            # RENDER YOUR GAME HERE
    pygame.display.flip()  # flip() the display to put your work on screen: update the display

    clock.tick(60)  # limits FPS to 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_display_running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if white_won or black_won:
                continue
            x,y=mouse_click(current_player)
            print(f"x,y:{x, y}")
            if is_promoting:
                # Check to see if piece in our black box was selected
                # We always put black box and piece selections over x=3 and y spanning from 0-4
                if current_player == "White":
                    # Need to account for the fact that the board flips
                    x = 7-x
                    y = 7-y
                if x == 3 and y >= 0 and y < 4:
                    if y == 0:
                        game_board[promoting_pawn_pos[0]][promoting_pawn_pos[1]] = Piece("Knight", promoting_color, 3)
                    elif y == 1:
                        game_board[promoting_pawn_pos[0]][promoting_pawn_pos[1]] = Piece("Bishop", promoting_color, 3)
                    elif y == 2:
                        game_board[promoting_pawn_pos[0]][promoting_pawn_pos[1]] = Piece("Rook", promoting_color, 5)
                    elif y == 3:
                        game_board[promoting_pawn_pos[0]][promoting_pawn_pos[1]] = Piece("Queen", promoting_color, 9)
                    is_promoting = False
                    promoting_pawn_pos = None
                    promoting_color = None

                    if current_player=="White":
                        current_player="Black"
                    else:
                        current_player="White"

                    if is_in_checkmate(game_board, current_player):
                        print(f"{current_player} is in checkmate. Game Over")
                        if current_player == "White":
                            black_won = True
                        else:
                            white_won = True
                    else:
                        print(f"{current_player}'s turn")
                else:
                    print("Please pick a promotion piece")
            # Selecting our first square
            elif selected_x == None and selected_y == None:
                if (game_board[x][y] != 0 and game_board[x][y].color == current_player):
                    selected_x, selected_y = x, y
            else: # Player is picking their second square
                # If the target square is empty or opponent piece
                if (game_board[x][y] == 0 or game_board[x][y].color != current_player):
                    # If this is a valid move
                    en_passant = False
                    castle = False
                    if can_en_passant(game_board, selected_x, selected_y, x, y, current_player):
                        en_passant=True
                    if can_castle(game_board, selected_x, selected_y, x, y, current_player):
                        castle=True
                    if castle or en_passant or (game_board[selected_x][selected_y]).can_move(game_board, selected_x,selected_y, x,y, current_player):
                        item_at_target = game_board[x][y]
                        move_piece(game_board, selected_x, selected_y, x, y, current_player)
                        if en_passant:
                            # Remove en passant'd pawn
                            stored_pawn = last_move[0]
                            game_board[last_move[2][0]][last_move[2][1]] = 0
                        if castle:
                            # Move kingside/queenside rook
                            stored_rook = get_castling_rook(game_board, y, current_player)
                            stored_rook_start_coords = get_castling_rook_start_coords(y, current_player)
                            stored_rook_end_coords = get_castling_rook_end_coords(y, current_player)
                            game_board[stored_rook_start_coords[0]][stored_rook_start_coords[1]] = 0
                            game_board[stored_rook_end_coords[0]][stored_rook_end_coords[1]] = stored_rook

                        # If the current player's king is in check, move the piece back
                        if c.check(game_board, white_king_coords, black_king_coords, current_player):
                            print("Invalid move, king in check")
                            move_piece(game_board, x, y, selected_x, selected_y, current_player)
                            game_board[x][y] = item_at_target
                            if en_passant:
                                # Restore en passant'd pawn
                                game_board[last_move[2][0]][last_move[2][1]] = stored_pawn
                            if castle:
                                # Restore moved rook
                                game_board[stored_rook_start_coords[0]][stored_rook_start_coords[1]] = stored_rook
                                game_board[stored_rook_end_coords[0]][stored_rook_end_coords[1]] = 0
                        else: # Otherwise this is a valid move. Leave the piece there and update current player
                            last_move=[game_board[x][y],(selected_x, selected_y),(x,y)]
                            # If a king has moved, save that to prevent future castling
                            if game_board[x][y].name == "King":
                                if current_player == "White":
                                    white_king_has_moved=True
                                else:
                                    black_king_has_moved=True
                            
                            # Track if player moved their rook, in which case they cannot castle on that side
                            if current_player == "Black":
                                if selected_x == 7 and selected_y == 0 and game_board[x][y].name == "Rook":
                                    black_kingside_rook_has_moved=True
                                if selected_x == 7 and selected_y == 7 and game_board[x][y].name == "Rook":
                                    black_queenside_rook_has_moved=True
                            else:
                                if selected_x == 0 and selected_y == 0 and game_board[x][y].name == "Rook":
                                    white_kingside_rook_has_moved=True
                                if selected_x == 0 and selected_y == 7 and game_board[x][y].name == "Rook":
                                    white_queenside_rook_has_moved=True
                            
                            # Track if piece is now in opposite rook space, indicating that it was captured and can no longer castle
                            if current_player == "Black" and x==0 and y==0:
                                white_kingside_rook_has_moved=True
                            elif current_player == "Black" and x==0 and y==7:
                                white_queenside_rook_has_moved=True
                            elif current_player == "White" and x==7 and y==0:
                                black_kingside_rook_has_moved=True
                            elif current_player == "White" and x==7 and y==7:
                                black_queenside_rook_has_moved=True

                            # Check if we're promoting a pawn
                            if game_board[x][y].name == "Pawn" and (x == 7 or x == 0):
                                is_promoting=True
                                promoting_pawn_pos=(x,y)
                                promoting_color=current_player
                            else:
                                if current_player=="White":
                                    current_player="Black"
                                else:
                                    current_player="White"

                                if is_in_checkmate(game_board, current_player):
                                    print(f"{current_player} is in checkmate. Game Over")
                                    if current_player == "White":
                                        black_won = True
                                    else:
                                        white_won = True
                                else:
                                    print(f"{current_player}'s turn")
                    selected_x = None
                    selected_y = None
                else:
                    selected_x, selected_y = x, y

pygame.quit()
sys.exit()

