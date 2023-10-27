import pygame  
import os 
os.chdir("G:\\GitHub\COM4008-PR1-EH\Shooter_Game_Assets")

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Army Shooter")

# CONSTANTS
BLACK = (0, 0, 0)
FPS = 60
VEL = 8
BORDER = pygame.Rect(WIDTH/2 - 3, 0, 6, HEIGHT)
ARMY_MAN = pygame.image.load("armymanv2.png")
ARMY_MAN_LEFT = pygame.transform.scale(ARMY_MAN, (100, 125))
ARMY_MAN_RIGHT = pygame.transform.flip(pygame.transform.scale(ARMY_MAN, (100, 125)), True, False)
POWER_UP_ICON = pygame.image.load("powerupicon.png")
BACKGROUND = pygame.image.load("grassybackground.jpeg")
BACKGROUND = pygame.transform.scale(BACKGROUND,(900, 500))


def left_movement(keys_pressed, left):
        if keys_pressed[pygame.K_a] and left.x - VEL > 0:
            left.x -= VEL
        if keys_pressed[pygame.K_d] and left.x + VEL < BORDER.x - 100:
            left.x += VEL
        if keys_pressed[pygame.K_w] and left.y - VEL > 0:
            left.y -= VEL
        if keys_pressed[pygame.K_s] and left.y + VEL < HEIGHT - 125:
            left.y += VEL

def right_movement(keys_pressed, right):
        if keys_pressed[pygame.K_LEFT] and right.x - VEL > BORDER.x:
            right.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and right.x + VEL < WIDTH - 100:
            right.x += VEL
        if keys_pressed[pygame.K_UP] and right.y - VEL > 0:
            right.y -= VEL
        if keys_pressed[pygame.K_DOWN] and right.y + VEL < HEIGHT - 125:
            right.y += VEL

def draw_window(right, left):
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(ARMY_MAN_LEFT, (left.x, left.y))
    WIN.blit(ARMY_MAN_RIGHT, (right.x, right.y))    
    pygame.display.update()

# GAME LOOP
def main():
    right = pygame.Rect(700, 150, WIDTH, HEIGHT)
    left = pygame.Rect(150, 150, WIDTH, HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()      
        left_movement(keys_pressed, left)
        right_movement(keys_pressed, right)
        draw_window(right, left)
    pygame.quit()

if __name__ == "__main__":
    main()