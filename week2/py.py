
from turtle import bgcolor
import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PONG!")


# ===================================================================== #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    clock.tick(60)

# ====================================================================== #

    ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

    player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

    opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

    bg_color = pygame.Color('grey12')
    light_grey = (200, 200, 200)

    pygame.draw.rect(screen, light_grey, player)

    pygame.draw.rect(screen, light_grey, opponent)

    # ================================================================== #
