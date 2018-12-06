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
# An array - inside the [] we call the wall constructor in the Wall class (x, y pos and x, y scale for each wall)
# The for loop makes it called 11 times and adds it to the array
walls = [wall.Wall() for i in range(10)]
# Initializing pygame's font, so we can display the FPS (necessary for displaying any text)
pygame.font.init()
# Defining a new font object (first constructor the font type, None = pygame default font, second is the font size = 100)
initial_font = pygame.font.Font(None, 100)
font = pygame.font.Font(None, 30)
# Used for limiting and getting the FPS
clock = pygame.time.Clock()
# Returns the number (in miliseconds) since pygame.init was called (before it's initialized it is zero)
last_frame = pygame.time.get_ticks()
speed_multiplier = 1
line_x = 197
line_y = 930
line_w = 1531
line_h = 46

# initalizes pygame so we can call pygame methods
pygame.init()

# (0, 0) means it has the same resolution as the screen
screen = pygame.display.set_mode((0, 0))
# Window label (the name of the window)
pygame.display.set_caption('Obstacle Course simulator 2018')
# Maybe this isn't needed
pygame.display.toggle_fullscreen()

# Loading the background image -
# .convert() creates a new copy of the surface with the pixel format changed (it boosts FPS)
background = pygame.image.load("background.jpg").convert()
wall = pygame.image.load("wall.jpeg").convert()
line = pygame.image.load("line.png").convert_alpha()
# mask.from_surface is a pygame method - sorts out all the transparent pixels
# We can use collision that ignores transparent pixels
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


# Main loop
while True:
    # The event loop - An open loop that makes the game continuously run (it's a necessity)
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
        # Setting the max FPS
        clock.tick(30)
        # Returns the time in milliseconds since pygame was initialized
        start = pygame.time.get_ticks()
        # The blit function is called on the screen object
        # (first parameter - what we want blited, second parameter - pixel pos)
        # Blitting is putting something on the screen - in this case we are visualizing the background
        # (0, 0) is the anchor point of an image
        screen.blit(background, [0, 0])
        screen.blit(line, [line_x, line_y])

        # Calculating delta time
        delta_time = (start - last_frame) / 1000
        # Changing last frame to the actual last frame, so we can calculate again in the next frame
        last_frame = start
        # if statement that makes the walls disappearing after they reach a certain position
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
        screen.blit(frame, ((SCREEN_WIDTH - frame_x) / 2, SCREEN_HEIGHT / 2))

        # Rendering the FPS text
        fps = font.render(str(int(clock.get_fps())), False, pygame.Color('white'))
        screen.blit(fps, (50, 50))
        pygame.display.update()

#pygame.quit()
