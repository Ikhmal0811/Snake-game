import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

exit_game = False


#initial coordinate
x = 90
y = 90

oldx = x
oldy = y

foodx = random.randrange(0, 1280, 30)
foody = random.randrange(0, 720, 30)

#scoring 
score = 0
font = pygame.font.SysFont("Arial", 30)


#direction 
direction = "RIGHT"

#speed for the player
velocity = 15
clock = pygame.time.Clock()


def snake_move(x, y, oldx, oldy): 
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(oldx, oldy, 30, 30))
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 30, 30))

while not exit_game:
    pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(x, y, 30, 30))#initial snake position and size
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(foodx, foody, 30, 30))# the snake food position

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

    if x == foodx and y == foody:
        foodx = random.randrange(0, 1280, 30)
        foody = random.randrange(0, 720, 30)
        score+=1
        screen.fill((0, 0, 0), (10, 10, 200, 40)) #refresh the position of score
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10,10))

    snake_move(x, y, oldx, oldy)
    pygame.display.update()
    clock.tick(20)
