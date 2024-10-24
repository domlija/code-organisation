import pygame
import sys

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

WHITE = 255, 255, 255
BLUE = 0, 0, 255

square_size = 50
square_rect = pygame.Rect(
    (width - square_size) // 2,
    height - square_size,
    square_size,
    square_size
)

gravity = 1500
jump_speed = -500
velocity = 0
on_ground = True


while True:

    delta_time = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]: # and on_ground:
        velocity = jump_speed
        on_ground = False

    velocity += gravity *  delta_time

    square_rect.y += velocity * delta_time # gravity * delta * delta


    if square_rect.y > height - square_size:
        square_rect.y = height - square_size
        velocity = 0
        on_ground = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, square_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60) 