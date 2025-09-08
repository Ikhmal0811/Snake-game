import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

exit_game = False

#initial coordinate
x = 100
y = 100

oldx = x
oldy = y

#direction 
direction = "RIGHT"

#speed for the player
velocity = 12
clock = pygame.time.Clock()

def snake_move(x, y, oldx, oldy): 
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(oldx, oldy, 30, 30))
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 30, 30))

while not exit_game:
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 30, 30))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            if event.key == pygame.K_DOWN:
                direction = "DOWN"
            if event.key == pygame.K_UP:
                direction = "UP"
    if direction == "LEFT":
        oldx = x
        oldy = y
        x-=velocity
    if direction == "RIGHT":
        oldx = x
        oldy = y
        x+=velocity
    if direction == "DOWN":
        oldx = x
        oldy = y
        y+=velocity
    if direction == "UP":
        oldx = x
        oldy = y
        y-=velocity

    snake_move(x, y, oldx, oldy)
    pygame.display.update()
    clock.tick(10)
