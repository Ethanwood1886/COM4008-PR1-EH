import pygame  
import os 
os.chdir("G:\\GitHub\COM4008-PR1-EH\Shooter_Game_Assets")

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Army Shooter")

# CONSTANTS
FPS = 60


ARMY_MAN = pygame.image.load("armymanv2.png")
POWER_UP_ICON = pygame.image.load("powerupicon.png")
BACKGROUND = pygame.image.load("grassybackground.jpeg")
BACKGROUND = pygame.transform.scale(BACKGROUND,(900, 500))
def draw_images():
    WIN.blit(ARMY_MAN, (300, 100))
    pygame.display.update()
# GAME LOOP
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
       
       
       
        draw_images()
  
  
  
  
    pygame.quit()

if __name__ == "__main__":
    main()