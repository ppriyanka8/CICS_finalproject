# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
WIDTH, HEIGHT= 800,800
SQUARE_SIZE=WIDTH//8
WHITE=(255,255,255) #RGB for white
BLACK=(0,0,0) #RGB for black
WHITE_PAWN=pygame.image.load('white_pawn.png')
BLACK_PAWN=pygame.image.load('black_pawn.png')
WHITE_PAWN=pygame.transform.scale(WHITE_PAWN,(SQUARE_SIZE,SQUARE_SIZE))
BLACK_PAWN=pygame.transform.scale(BLACK_PAWN,(SQUARE_SIZE,SQUARE_SIZE))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

def visual_chessboard():
    for row in range(8):
        for col in range(8):
            x_pos=col*SQUARE_SIZE
            y_pos=row*SQUARE_SIZE
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen,WHITE,(x_pos,y_pos,SQUARE_SIZE,SQUARE_SIZE))
            else:
                pygame.draw.rect(screen,BLACK,(x_pos,y_pos,SQUARE_SIZE,SQUARE_SIZE))

def mouse_click():
    mouse_x,mouse_y=pygame.mouse.get_pos()

    row=mouse_y//SQUARE_SIZE
    col=mouse_x//SQUARE_SIZE
    print(f"Clicked on square: ({row},{col})")

def render_pieces():
    screen.blit(WHITE_PAWN,(0*SQUARE_SIZE, 1*SQUARE_SIZE))
    screen.blit(BLACK_PAWN,(0*SQUARE_SIZE, 6*SQUARE_SIZE))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_click()
    visual_chessboard()
    render_pieces()
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()