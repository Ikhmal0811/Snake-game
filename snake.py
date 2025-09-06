import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

exit_game = False

#initial coordinate
x = 100
y = 100

#speed for the player
velocity = 12

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True        
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
