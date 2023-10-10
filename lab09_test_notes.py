#Thomas King, ETGG1801-01, lab09
import pygame
import random
import time
#Initialize pygame
pygame.display.init()
pygame.font.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
column_width = 96
row_height = 96
#Load Assets
floor = pygame.image.load("images\\wood_floor.png") 
princess = pygame.image.load("images\\princess_walking.png")
#Font Assets 
font_obj = pygame.font.Font("fonts\\Pixeltype.ttf", 16)     #has to be multiples of 16
over_screen = pygame.font.Font("fonts\\doomed.ttf", 88)     #has to be multiples of 11
#Loading
princessx = 350
princessy = 350
princess_direction = 0
princess_frame = 0
num_steps = 0
max_steps = 10
on_screen = 800
frame = 96
framex = 0
framey = 0

#Call Loop
while princessy < on_screen:
    #modify the princess position 
    #change direction when reaching a certain number of steps
    if princess_direction == 0:
        princessx += 5
    elif princess_direction == 1:
        princessx += 5
        princessy -= 5
        framey = 1
    elif princess_direction == 2:
        princessy -= 5
        framey = 2
    elif princess_direction == 3:
        princessx -= 5
        princessy -= 5
        framey = 3
    elif princess_direction == 4:
        princessx -= 5
        framey = 4
    elif princess_direction == 5:
        princessx -= 5
        princessy += 5
        framey = 5
    elif princess_direction == 6:
        princessy += 5
        framey = 6
    elif  princess_direction == 7:
        princessx += 5
        princessy += 5
        framey = 7
    #draw the princess and trail on the screen 
    window.blit(floor, (0,0))
    pygame.draw.rect(window, (0, 255, 0), (princessx + 48, princessy + 48, 8, 8))
    pygame.draw.rect(floor, (0, 255, 0), (princessx + 48, princessy + 48, 8, 8))
    window.blit(princess, (princessx, princessy), (frame * framex, frame * framey,column_width,row_height))
    #draw text
    princess_x = font_obj.render(f"Player x: {princessx}", True, (0,255,0))
    princess_y = font_obj.render(f"Player y: {princessy}", True, (0,255,0))
    steps = font_obj.render(f"Steps: {num_steps}/70", True, (0,255,0))
    animation = font_obj.render(f"Animation Frame: {framex + framey}", True, (0,255,0))
    direction = font_obj.render(f"Direction: {princess_direction}", True, (0,255,0))
    game_over = over_screen.render("Game_Over", True, (255,0,0))
    #blit text
    window.blit(princess_x, (0,0))
    window.blit(princess_y, (0,20))
    window.blit(steps, (0,40))
    window.blit(animation, (0,60))
    window.blit(direction, (0,80))

    framex += 1
    if framex > 7:
        framex = 0
    
    num_steps += 1
    if num_steps == max_steps: 
        princess_direction += 1
        max_steps += 2
        num_steps = 0
        if princess_direction == 8:
            princess_direction = 0
            framey = 0
    #draw game over screen 
    if princessx == -170:
        pygame.draw.rect(floor, (0, 0, 0), (0,0,800,600))
        window.blit(game_over, (200,180))
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit
""" if control_mode == "keyboard":
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        player_horizontal_speed += player_speed
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        player_horizontal_speed -= player_speed
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        player_vertical_speed -= player_speed
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
        player_vertical_speed += player_speed   
        #       window, (color), (x-coordinate, y-coordinate, width, height)
pygame.draw.rect(window, rect_color_black, (149, 49, 100,100))   
pygame.draw.ellipse(window, (30, 138, 70), ((690, 455, 30,47)))
coin_horizontal_rate = coin_speed
coins_collected = 0
coin_x = random.randint(0, win_width)
coin_y = random.randint(0, win_height)
coin_frame = 0
coin_teleport_delay = 2.0
coin_teleport_time = time.time()
coin_animation_rate = 10"""