import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

exit_game = False

#initial coordinate
x = 100
y = 100

oldx = x
oldy = y

#speed for the player
velocity = 12

def snake_move(x, y, oldx, oldy): 
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(oldx, oldy, 60, 60))
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 60, 60))

while not exit_game:
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 60, 60))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                oldx = x
                x -= velocity
                snake_move(x, y, oldx, oldy)
            if event.key == pygame.K_RIGHT:
                oldx = x
                x += velocity
                snake_move(x, y, oldx, oldy)
            if event.key == pygame.K_DOWN:
                oldy = y
                y += velocity
                snake_move(x, y, oldx, oldy)
            if event.key == pygame.K_UP:
                oldy = y
                y -= velocity
                snake_move(x, y, oldx, oldy)

