import pygame
import numpy as np
import edge_detection as ed
import background_subtraction as bs
import cv2
import time
import threading
import wall

bs_class = bs.BackSub()
ed_class = ed.EdgeDetect()
space_held = False
game_screen = 0
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BLACK = (0,0,0)
WHITE = (255,255,255)
frame_no = 0
frame_limit = 60
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
'''
pos_changex = 9.2
pos_changey = 5.2
scale_changex = 18.8
scale_changey = 10.4
'''
pos_changex = 2.8/5
pos_changey = 1.6/5
scale_changex = 5.5/5
scale_changey = 3.2/5
obs_changed = False
num_obs_hit = 0
obs_hit = False
obs_avoided = 0
obstacle_number = 0
speed_multiplier = 1
time_limit = 2500
line_x = 197
line_y = 930
line_w = 1531
line_h = 46

# initalizes pygame so we can call pygame methods
pygame.init()

# (0, 0) means it has the same resolution as the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Window label (the name of the window)
pygame.display.set_caption('Obstacle Course simulator 2018')
# Maybe this isn't needed
#pygame.display.toggle_fullscreen()

# Loading the background image -
# .convert() creates a new copy of the surface with the pixel format changed (it boosts FPS)
background = pygame.image.load("background.jpg").convert()
wall = pygame.image.load("Obstacle.png").convert()
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


# Main loop
while True:
    # The event loop - An open loop that makes the game continuously run (it's a necessity)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            break

    # Setting the max FPS
    dt = clock.tick(30)
    # The blit function is called on the screen object
    # (first parameter - what we want blited, second parameter - pixel pos)
    # Blitting is putting something on the screen - in this case we are visualizing the background
    # (0, 0) is the top left of the screen and position (0, 0) of images are usually their top left
    screen.blit(background, [0, 0])
    screen.blit(line, [line_x, line_y])
    # Returns the time in milliseconds since pygame was initialized
    '''
    start = pygame.time.get_ticks()
    # Calculating delta time
    delta_time = (start - last_frame) / 1000
    # Changing last frame to the actual last frame, so we can calculate again in the next frame
    last_frame = start
    # if statement that makes the walls disappearing after they reach a certain position
    '''

    if obstacle_number == 0 and not obs_changed:
        # Left
        walls[obstacle_number].x -= 70
        scale_changex /= 2
        obs_changed = True
        first_obstacle = pygame.time.get_ticks() + 500
    elif obstacle_number == 1 and not obs_changed:
        # Right
        walls[obstacle_number].new_wall_pos_x += 70
        walls[obstacle_number].x -= 70
        pos_changex = - 0.07
        scale_changex /= 2
        obs_changed = True
    elif obstacle_number == 2 and not obs_changed:
        # Crouch
        walls[obstacle_number].y -= 70
        scale_changey /= 3.5
        obs_changed = True
    elif obstacle_number == 3 and not obs_changed:
        # Jump
        walls[obstacle_number].new_wall_pos_y += 80
        walls[obstacle_number].y -= 80
        pos_changey -= 0.5
        pos_changex += 0.01
        scale_changex += 0.05
        scale_changey /= 5
        obs_changed = True
    elif obstacle_number == 4 and not obs_changed:
        # Crouch
        walls[obstacle_number].y -= 70
        scale_changey /= 3.5
        obs_changed = True
    elif obstacle_number == 5 and not obs_changed:
        # Right
        walls[obstacle_number].new_wall_pos_x += 70
        walls[obstacle_number].x -= 70
        pos_changex = - 0.07
        scale_changex /= 2
        obs_changed = True
    elif obstacle_number == 6 and not obs_changed:
        # Jump
        walls[obstacle_number].new_wall_pos_y += 80
        walls[obstacle_number].y -= 80
        pos_changey = -0.3
        pos_changex += 0.3
        scale_changex += 0.6
        scale_changey /= 3
        obs_changed = True
    elif obstacle_number == 7 and not obs_changed:
        # Left
        walls[obstacle_number].x -= 70
        scale_changex /= 2
        obs_changed = True
    elif obstacle_number == 8 and not obs_changed:
        # Crouch
        walls[obstacle_number].y -= 70
        scale_changey /= 3.5
        obs_changed = True
    elif obstacle_number == 9 and not obs_changed:
        # Right
        walls[obstacle_number].new_wall_pos_x += 70
        walls[obstacle_number].x -= 70
        pos_changex = - 0.07
        scale_changex /= 2
        obs_changed = True

    #new_obstacle = pygame.time.get_ticks() - first_obstacle

    if frame_no - frame_limit <= 0:
        screen.blit(wall, (walls[obstacle_number].new_wall_pos_x, walls[obstacle_number].new_wall_pos_y))
        wall = pygame.transform.scale(wall, (int(walls[obstacle_number].x), int(walls[obstacle_number].y)))
        walls[obstacle_number].new_wall_pos_x -= int((pos_changex * speed_multiplier))
        walls[obstacle_number].new_wall_pos_y -= int((pos_changey * speed_multiplier))
        walls[obstacle_number].x += int((scale_changex * speed_multiplier))
        walls[obstacle_number].y += int((scale_changey * speed_multiplier))
        speed_multiplier += 1
        if walls[obstacle_number].new_wall_pos_y + walls[obstacle_number].y > line_y:
            '''
            wall_rect = wall.get_rect(center=(0, 0))
            frame_rect = frame.get_rect(center=(0, 0))
            wall_mask = pygame.mask.from_surface(wall)
            offset_x = wall_rect.x - frame_rect.x
            offset_y = wall_rect.y - frame_rect.y
            hit = mask_ed.overlap(wall_mask, (offset_x, offset_y))
            #hit = pygame.sprite.spritecollide(mask_ed, wall, False)
            print(hit)
            if hit:
                obs_hit = True
                print("hit")
                '''
    else:
        obstacle_number += 1
        speed_multiplier = 1
        frame_limit += 60
        obs_changed = False
        pos_changex = 2.7 / 5
        pos_changey = 1.4 / 5
        scale_changex = 5.5 / 5
        scale_changey = 3 / 5
        if obs_hit:
            num_obs_hit += 1
            obs_hit = False
        else:
            obs_avoided += 1

    frame_no += 1


    frame = bs_class.main()
    frame = pygame.surfarray.make_surface(frame)
    frame.convert_alpha()
    #frame = pygame.transform.smoothscale(frame, (1500, 1100))
    frame_x = frame.get_width()
    frame_y = frame.get_height()
    frame.set_colorkey((0, 0, 0))
    mask_ed = pygame.mask.from_surface(frame)
    screen.blit(frame, ((SCREEN_WIDTH - frame_x) / 2, (SCREEN_HEIGHT - frame_y) / 2 + 50))


    # Rendering the FPS text
    fps = font.render(str(int(clock.get_fps())), False, pygame.Color('white'))
    screen.blit(fps, (50, 50))
    pygame.display.update()

#pygame.quit()
