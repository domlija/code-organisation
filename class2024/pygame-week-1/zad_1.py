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
    (height - square_size) // 2,
    square_size,
    square_size
)

square_speed = 5


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        square_rect.y -= square_speed
    if keys[pygame.K_s]:
        square_rect.y += square_speed
    if keys[pygame.K_a]:
        square_rect.x -= square_speed
    if keys[pygame.K_d]:
        square_rect.x += square_speed

    square_rect.clamp_ip(screen.get_rect())

    # isto
    # square_rect = square_rect.clamp(screen.get_rect())



    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, square_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)