
from turtle import bgcolor
import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

# ========= SCREEN DIMENSIONS ========= #

screen_width = 800
screen_height = 600


def get_rand_colour():
    colour_r = random.randint(0, 255)
    colour_g = random.randint(0, 255)
    colour_b = random.randint(0, 255)
    return (colour_r, colour_g, colour_b)


pygame.display.set_caption("Rainbow!")
done = False
counter = 0
colour = get_rand_colour()


screen = pygame.display.set_mode(
    (screen_width, screen_height))

# ========== WINDOW NAME ============= #

pygame.display.set_caption("PONG!")


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():

    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # ---------------------

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# ========================= COLOURS ========================== #


bg_color = (203, 102, 0)
light_grey = (200, 200, 200)

# =================== BALL MOVEMENT =========================== #

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# =========== CREATING ELEMSENTS ========= #

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)

player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


# =================== STARTS LOOP =========================== #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ball_animation()
    player.y += player_speed
    counter += 1
    if counter > 3:
        colour = get_rand_colour()
        counter = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_speed += 7
        if event.key == pygame.K_UP:
            player_speed -= 7

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            player_speed -= 7
        if event.key == pygame.K_UP:
            player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()
    # =================== SHAPES ========================== #
    screen.fill(bg_color)

    pygame.draw.rect(screen, light_grey, player)

    pygame.draw.rect(screen, light_grey, opponent)

    pygame.draw.ellipse(screen, colour, ball)

    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                                            0), (screen_width/2, screen_height))

    # ==================== BALL MOVEMENT ================ #

    pygame.display.flip()

    clock.tick(30)
