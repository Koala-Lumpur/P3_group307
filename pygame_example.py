import pygame
import numpy as np
import edge_detection as ed
import background_subtraction as bs
import cv2
import time
import threading
import wall

bs_class = bs.BackSub()
space_held = False
game_screen = 0
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BLACK = (0,0,0)
WHITE = (255,255,255)
walls = [wall.Wall() for i in range(10)]
pygame.font.init()
initial_font = pygame.font.Font(None, 100)

font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
last_frame = pygame.time.get_ticks()
speed_multiplier = 1
line_x = 197
line_y = 930
line_w = 1531
line_h = 46

pygame.init()

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption('WHat is thiis')
pygame.display.toggle_fullscreen()

background = pygame.image.load("background.jpg").convert()
wall = pygame.image.load("wall.jpeg").convert()
line = pygame.image.load("line.png").convert_alpha()
wall_mask = pygame.mask.from_surface(wall)
#wall = pygame.transform.scale(wall, (wall.get_width()/3, wall.get_height()/3))


def start_game(text, cap_frame):
        screen.fill(BLACK)
        initial_text = initial_font.render(text, False, pygame.Color('white'))
        initial_text_rect = initial_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(initial_text, initial_text_rect)
        pygame.display.update()
        if cap_frame:
            bs_class.main()


def sub(u, v):
    return [u[i]-v[i] for i in range(len(u))]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and not space_held:
            game_screen += 1
            space_held = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            space_held = False

    if game_screen == 0:
        start_game("Press space to capture the first frame", False)
    elif game_screen == 1:
        start_game("Press space to continue to the game", True)
    else:
        clock.tick(60)
        start = pygame.time.get_ticks()
        screen.blit(background, [0, 0])
        screen.blit(line, [line_x, line_y])

        delta_time = (start - last_frame) / 1000
        last_frame = start
        if not walls[0].x > 5000:
            screen.blit(wall, (walls[0].new_wall_pos_x * 1.5, walls[0].new_wall_pos_y))
            wall = pygame.transform.smoothscale(wall, (int(walls[0].x), int(walls[0].y)))
            walls[0].new_wall_pos_x -= int(8.8 * delta_time * speed_multiplier)
            walls[0].new_wall_pos_y -= int(4.7 * delta_time * speed_multiplier)
            walls[0].x += int(18.5 * delta_time * speed_multiplier)
            walls[0].y += int(10 * delta_time * speed_multiplier)
            speed_multiplier += 1
            if walls[0].new_wall_pos_y + walls[0].y > line_y:
                wall_rect = wall.get_rect(center=(0, 0))
                frame_rect = frame.get_rect(center=(0, 0))
                wall_mask = pygame.mask.from_surface(wall)
                offset_x = wall_rect.x - frame_rect.x
                offset_y = wall_rect.y - frame_rect.y
                hit = mask_ed.overlap(wall_mask, (offset_x, offset_y))
                print(hit)
                if hit:
                    print("hit")

        frame = bs_class.main()
        frame = pygame.surfarray.make_surface(frame)
        frame.convert_alpha()
        frame_x = frame.get_width()
        frame_y = frame.get_height()
        frame.set_colorkey((0, 0, 0))
        mask_ed = pygame.mask.from_surface(frame)
        screen.blit(frame, (SCREEN_WIDTH / 2 - frame_x / 2, SCREEN_HEIGHT / 2))

        fps = font.render(str(int(clock.get_fps())), False, pygame.Color('white'))
        screen.blit(fps, (50, 50))
        pygame.display.update()

#pygame.quit()
