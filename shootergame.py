import pygame  
import os 
pygame.font.init()
pygame.mixer.init()
os.chdir("G:\\GitHub\COM4008-PR1-EH\Shooter_Game_Assets")
#os.chdir("C:\\Users\\hasna\\OneDrive\\Documents\\GitHub\\COM4008-PR1-EH\\Shooter_Game_Assets")
#os.chdir(r'c:\Users\craft\OneDrive\Documents\GitHub\COM4008-PR1-EH\Shooter_Game_Assets')
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Army Shooter")

# SOUNDS
BULLET_HIT_SOUND = pygame.mixer.Sound('grenadesound.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('shotgunsound.mp3')
POWER_UP_SOUND = pygame.mixer.Sound('powerupsound.mp3')

# CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
VEL = 8
BULLET_VEL = 10
MAX_BULLETS = 4
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
BORDER = pygame.Rect(WIDTH//2 - 3, 0, 6, HEIGHT)
ARMY_MAN = pygame.image.load("armymanv2.png")
ARMY_MAN_LEFT = pygame.transform.scale(ARMY_MAN, (100, 125))
ARMY_MAN_RIGHT = pygame.transform.flip(pygame.transform.scale(ARMY_MAN, (100, 125)), True, False)
ARMY_MAN_WIDTH = 100
ARMY_MAN_HEIGHT = 125
POWER_UP_ICON = pygame.image.load("powerupicon.png")
BACKGROUND = pygame.image.load("grassybackground.jpeg")
BACKGROUND = pygame.transform.scale(BACKGROUND,(900, 500))
LEFT_HIT = pygame.USEREVENT + 1
RIGHT_HIT = pygame.USEREVENT + 2


def draw_window(right, left, right_bullets, left_bullets, right_health, left_health):
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

     # HEALTH TEXT NUMBER 
    right_health_text = HEALTH_FONT.render("Health: " + str(right_health), 1, WHITE)  
    left_health_text = HEALTH_FONT.render("Health: " + str(left_health), 1, WHITE)
    WIN.blit(right_health_text, (WIDTH - right_health_text.get_width() - 10, 10))
    WIN.blit(left_health_text, (10, 10))

    WIN.blit(ARMY_MAN_LEFT, (left.x, left.y))
    WIN.blit(ARMY_MAN_RIGHT, (right.x, right.y)) 


    for bullet in right_bullets: 
        pygame.draw.rect(WIN, (RED), bullet)      # RIGHT BULLETS

    for bullet in left_bullets:                   # LEFT BULLETS
        pygame.draw.rect(WIN, (WHITE), bullet)

    pygame.display.update()



# KEY CONTROLS & BORDERS 
def left_movement(keys_pressed, left):
        if keys_pressed[pygame.K_a] and left.x - VEL > 0:
            left.x -= VEL
        if keys_pressed[pygame.K_d] and left.x + VEL < BORDER.x:
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



# MOVE, COLLISION & REMOVAL OF BULLETS
def handle_bullets(left_bullets, right_bullets, left, right): 
    for bullet in left_bullets:
        bullet.x += BULLET_VEL
        if right.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RIGHT_HIT))
            left_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            left_bullets.remove(bullet)

    for bullet in right_bullets:
        bullet.x -= BULLET_VEL
        if left.colliderect(bullet):
            pygame.event.post(pygame.event.Event(LEFT_HIT))
            right_bullets.remove(bullet)
        elif bullet.x < 0:
            right_bullets.remove(bullet)


# WINNING PLAYER TEXT
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(4000)
     

# GAME LOOP
def main():
    right = pygame.Rect(700, 150, ARMY_MAN_WIDTH, ARMY_MAN_HEIGHT)
    left = pygame.Rect(150, 150, ARMY_MAN_WIDTH, ARMY_MAN_HEIGHT)

# BULLETS
    right_bullets = []
    left_bullets = []


    right_health = 5
    left_health = 5


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(left_bullets) < MAX_BULLETS:     # ASSIGN LEFT BULLET KEY 
                    bullet = pygame.Rect(left.x + left.width, left.y + left.height//2, 10, 5)
                    left_bullets.append(bullet)            
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_SPACE and len(right_bullets) < MAX_BULLETS:     # ASSIGN RIGHT BULLET KEY
                    bullet = pygame.Rect(right.x, right.y + right.height//2, 10, 5)
                    right_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
# HEALTH
            if event.type == RIGHT_HIT:
                right_health -= 1
                BULLET_HIT_SOUND.play()


            if event.type == LEFT_HIT:
                left_health -= 1
                BULLET_HIT_SOUND.play()
                

# ASSIGNING WINNING TEXT TO PLAYER
        winner_text = ""
        if right_health <= 0:
            winner_text = "Left Player wins!"            

        if left_health <= 0:
            winner_text = "Right Player wins!"                   

        if winner_text != "":
            draw_winner(winner_text)
            break

   
        keys_pressed = pygame.key.get_pressed()      
        left_movement(keys_pressed, left)
        right_movement(keys_pressed, right)
        handle_bullets(left_bullets, right_bullets, left, right)


        draw_window(right, left, right_bullets, left_bullets, right_health, left_health)

if __name__ == "__main__":
    main()