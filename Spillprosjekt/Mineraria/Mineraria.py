
#Mineraria Programmering og Modelering Spill

import pygame, time #Importerer pygame bibliotek

pygame.init()


bg = pygame.transform.smoothscale(pygame.image.load("Tex/Backgrounds/bg2.png"), (1920, 1080))
grass = pygame.image.load("Tex/Blocks/grass.png")
dirt = pygame.image.load("Tex/Blocks/dirt.png")
stone = pygame.image.load("Tex/Blocks/stone.png")

walkRight = [pygame.image.load("Tex/Animations/Main character/R000.png"), pygame.image.load("Tex/Animations/Main character/R002.png"), pygame.image.load("Tex/Animations/Main character/R003.png"), pygame.image.load("Tex/Animations/Main character/R004.png"), pygame.image.load("Tex/Animations/Main character/R005.png"), pygame.image.load("Tex/Animations/Main character/R006.png"), pygame.image.load("Tex/Animations/Main character/R007.png"), pygame.image.load("Tex/Animations/Main character/R008.png"), pygame.image.load("Tex/Animations/Main character/R009.png"), pygame.image.load("Tex/Animations/Main character/R010.png"), pygame.image.load("Tex/Animations/Main character/R011.png"), pygame.image.load("Tex/Animations/Main character/R012.png"), pygame.image.load("Tex/Animations/Main character/R013.png"), pygame.image.load("Tex/Animations/Main character/R014.png"), pygame.image.load("Tex/Animations/Main character/R015.png"), pygame.image.load("Tex/Animations/Main character/R016.png"), pygame.image.load("Tex/Animations/Main character/R017.png"), pygame.image.load("Tex/Animations/Main character/R018.png"), pygame.image.load("Tex/Animations/Main character/R019.png"), pygame.image.load("Tex/Animations/Main character/R020.png"), pygame.image.load("Tex/Animations/Main character/R021.png"), pygame.image.load("Tex/Animations/Main character/R022.png"), pygame.image.load("Tex/Animations/Main character/R023.png"), pygame.image.load("Tex/Animations/Main character/R024.png"), pygame.image.load("Tex/Animations/Main character/R025.png")]
walkLeft = [pygame.image.load("Tex/Animations/Main character/L000.png"), pygame.image.load("Tex/Animations/Main character/L002.png"), pygame.image.load("Tex/Animations/Main character/L003.png"), pygame.image.load("Tex/Animations/Main character/L004.png"), pygame.image.load("Tex/Animations/Main character/L005.png"), pygame.image.load("Tex/Animations/Main character/L006.png"), pygame.image.load("Tex/Animations/Main character/L007.png"), pygame.image.load("Tex/Animations/Main character/L008.png"), pygame.image.load("Tex/Animations/Main character/L009.png"), pygame.image.load("Tex/Animations/Main character/L010.png"), pygame.image.load("Tex/Animations/Main character/L011.png"), pygame.image.load("Tex/Animations/Main character/L012.png"), pygame.image.load("Tex/Animations/Main character/L013.png"), pygame.image.load("Tex/Animations/Main character/L014.png"), pygame.image.load("Tex/Animations/Main character/L015.png"), pygame.image.load("Tex/Animations/Main character/L016.png"), pygame.image.load("Tex/Animations/Main character/L017.png"), pygame.image.load("Tex/Animations/Main character/L018.png"), pygame.image.load("Tex/Animations/Main character/L019.png"), pygame.image.load("Tex/Animations/Main character/L020.png"), pygame.image.load("Tex/Animations/Main character/L021.png"), pygame.image.load("Tex/Animations/Main character/L022.png"), pygame.image.load("Tex/Animations/Main character/L023.png"), pygame.image.load("Tex/Animations/Main character/L024.png"), pygame.image.load("Tex/Animations/Main character/L025.png")]
runLeft = [pygame.image.load("Tex/Animations/Main character/LRun000.png"), pygame.image.load("Tex/Animations/Main character/LRun002.png"), pygame.image.load("Tex/Animations/Main character/LRun003.png"), pygame.image.load("Tex/Animations/Main character/LRun004.png"), pygame.image.load("Tex/Animations/Main character/LRun005.png"), pygame.image.load("Tex/Animations/Main character/LRun006.png"), pygame.image.load("Tex/Animations/Main character/LRun007.png"), pygame.image.load("Tex/Animations/Main character/LRun008.png"), pygame.image.load("Tex/Animations/Main character/LRun009.png"), pygame.image.load("Tex/Animations/Main character/LRun010.png"), pygame.image.load("Tex/Animations/Main character/LRun011.png"), pygame.image.load("Tex/Animations/Main character/LRun012.png"), pygame.image.load("Tex/Animations/Main character/LRun013.png"), pygame.image.load("Tex/Animations/Main character/LRun014.png"), pygame.image.load("Tex/Animations/Main character/LRun015.png"), pygame.image.load("Tex/Animations/Main character/LRun016.png"), pygame.image.load("Tex/Animations/Main character/LRun017.png"), pygame.image.load("Tex/Animations/Main character/LRun018.png"), pygame.image.load("Tex/Animations/Main character/LRun019.png"), pygame.image.load("Tex/Animations/Main character/LRun020.png"), pygame.image.load("Tex/Animations/Main character/LRun021.png"), pygame.image.load("Tex/Animations/Main character/LRun022.png"), pygame.image.load("Tex/Animations/Main character/LRun023.png"), pygame.image.load("Tex/Animations/Main character/LRun024.png"), pygame.image.load("Tex/Animations/Main character/LRun025.png")]
runRight = [pygame.image.load("Tex/Animations/Main character/RRun000.png"), pygame.image.load("Tex/Animations/Main character/RRun002.png"), pygame.image.load("Tex/Animations/Main character/RRun003.png"), pygame.image.load("Tex/Animations/Main character/RRun004.png"), pygame.image.load("Tex/Animations/Main character/RRun005.png"), pygame.image.load("Tex/Animations/Main character/RRun006.png"), pygame.image.load("Tex/Animations/Main character/RRun007.png"), pygame.image.load("Tex/Animations/Main character/RRun008.png"), pygame.image.load("Tex/Animations/Main character/RRun009.png"), pygame.image.load("Tex/Animations/Main character/RRun010.png"), pygame.image.load("Tex/Animations/Main character/RRun011.png"), pygame.image.load("Tex/Animations/Main character/RRun012.png"), pygame.image.load("Tex/Animations/Main character/RRun013.png"), pygame.image.load("Tex/Animations/Main character/RRun014.png"), pygame.image.load("Tex/Animations/Main character/RRun015.png"), pygame.image.load("Tex/Animations/Main character/RRun016.png"), pygame.image.load("Tex/Animations/Main character/RRun017.png"), pygame.image.load("Tex/Animations/Main character/RRun018.png"), pygame.image.load("Tex/Animations/Main character/RRun019.png"), pygame.image.load("Tex/Animations/Main character/RRun020.png"), pygame.image.load("Tex/Animations/Main character/RRun021.png"), pygame.image.load("Tex/Animations/Main character/RRun022.png"), pygame.image.load("Tex/Animations/Main character/RRun023.png"), pygame.image.load("Tex/Animations/Main character/RRun024.png"), pygame.image.load("Tex/Animations/Main character/RRun025.png")]
Idle = [pygame.image.load("Tex/Animations/Main character/Idle000.png"), pygame.image.load("Tex/Animations/Main character/Idle002.png"), pygame.image.load("Tex/Animations/Main character/Idle003.png"), pygame.image.load("Tex/Animations/Main character/Idle004.png"), pygame.image.load("Tex/Animations/Main character/Idle005.png"), pygame.image.load("Tex/Animations/Main character/Idle006.png"), pygame.image.load("Tex/Animations/Main character/Idle007.png"), pygame.image.load("Tex/Animations/Main character/Idle008.png"), pygame.image.load("Tex/Animations/Main character/Idle009.png"), pygame.image.load("Tex/Animations/Main character/Idle010.png"), pygame.image.load("Tex/Animations/Main character/Idle011.png"), pygame.image.load("Tex/Animations/Main character/Idle012.png"), pygame.image.load("Tex/Animations/Main character/Idle013.png"), pygame.image.load("Tex/Animations/Main character/Idle014.png"), pygame.image.load("Tex/Animations/Main character/Idle015.png"), pygame.image.load("Tex/Animations/Main character/Idle016.png"), pygame.image.load("Tex/Animations/Main character/Idle017.png"), pygame.image.load("Tex/Animations/Main character/Idle018.png"), pygame.image.load("Tex/Animations/Main character/Idle019.png"), pygame.image.load("Tex/Animations/Main character/Idle020.png"), pygame.image.load("Tex/Animations/Main character/Idle021.png"), pygame.image.load("Tex/Animations/Main character/Idle022.png"), pygame.image.load("Tex/Animations/Main character/Idle023.png"), pygame.image.load("Tex/Animations/Main character/Idle024.png"), pygame.image.load("Tex/Animations/Main character/Idle025.png")]
LoadPunchRight = [pygame.image.load("Tex/Animations/Main character/Attacks/LPR000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR016.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR017.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR018.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR019.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR020.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR021.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR022.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR023.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR024.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR025.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR026.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR027.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR028.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR029.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR030.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR031.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR032.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR033.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR034.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR035.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR036.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR037.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR038.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR039.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR040.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR041.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR042.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR043.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR044.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR045.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR046.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR047.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR048.png")]
punchRight = [pygame.image.load("Tex/Animations/Main character/Attacks/PR000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR016.png")]

width_window = 800 #Bredden på vinduet (780 pikeseler)
height_window = 500 #Høyden på vinduet (500 pikseler)


window_size = (width_window, height_window)

window = pygame.display.set_mode((window_size), pygame.RESIZABLE)

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("Mineraria") #Barnavnet
pygame.display.set_icon(grass)

clock = pygame.time.Clock()

CHUNK_SIZE = 8

#Map

def map_load(path): #Definerer en funksjon som leser av en txt. fil
    m = open(path + ".txt", "r")
    data = m.read()
    m.close()
    data = data.split("\n")
    map = []
    for row in data:
        map.append(list(row))
    return map

map = map_load("Tex/Maps/map")

tile_index = {1:dirt, 2:grass, 3:stone}

def drawGameMap():
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == "1":
                window.blit(dirt, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "2":
                window.blit(grass, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "3":
                window.blit(stone, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile != "0":
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            x += 1
        y += 1

def generate_chunk(x,y):
    chunk_data = []
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos
            tile_type = 0
            if target_y > 10:
                tile_type = 1
            elif target_y > 20:
                tile_type = 3
            elif target_y == 10:
                tile_type = 2
            if tile_type != 0:
                chunk_data.append([[target_x, target_y], tile_type])
    return chunk_data

#Character:

width_char = 40
height_char = 80
walkCount = 0
standCount = 0
runCount = 0
punchCount = 0
punchCount_2 = 0
jumpCount = 10

velocity_walk = 2
velocity_run = 5

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["right"] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types

left_walk = False
right_walk = False
right_run = False
left_run = False
Idle_stand = False
right_punch = False
right_punch_2 = False
left_punch = False
airtime = True
Fullscreen = False
Removeblock = False
impact_full = False
impact_mid = False



player_x_momentum = 0
player_y_momentum = 0
air_timer = 0

true_scroll = [0,0]

button_press_time = 0

current_time = 0

player_rect = pygame.Rect(500, 20, width_char, height_char)
run = True

while run:

    #Generelt
    clock.tick(50) #Bilder per sekund
    window.blit(bg, (0,0))
    current_time = pygame.time.get_ticks()


    #Camera
    true_scroll[0] += (player_rect.x - true_scroll[0]-(width_window)/2)/20
    true_scroll[1] += (player_rect.y - true_scroll[1]-(height_window/2))/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    #GameMap
    tile_rects = []
    drawGameMap()
    '''for y in range(2):
        for x in range(4):
            target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*40)))
            target_y = y + int(round(scroll[1]/(CHUNK_SIZE*40)))
            target_chunk = str(target_x) + ";" + str(target_y)
            if target_chunk not in map:
                map[target_chunk] = generate_chunk(target_x, target_y)
            for tile in map[target_chunk]:
                window.blit(tile_index[tile[1]], (tile[0][0]*40-scroll[0], tile[0][1]*40-scroll[1]))
                if tile[1] in [1,2]:
                    tile_rects.append(pygame.Rect(tile[0][0]*40, tile[0][1]*40, 40, 40))'''

    #Mouse
    mouse = pygame.mouse.get_pos()

    #Character Movement
    player_movement = [0, 0]
    if right_walk:
        player_movement[0] += velocity_walk
    if left_walk:
        player_movement[0] -= velocity_walk
    if right_run:
        player_movement[0] += velocity_run
    if left_run:
        player_movement[0] -= velocity_run

    if right_punch == True:
        button_press_time += 1
        print(button_press_time)
        if button_press_time > 35:
            impact_full = True
            punchCount_2 = 0
        elif button_press_time > 20:
            impact_mid = True
            punchCount_2 = 0
    elif right_punch == False:
        width_window = 800
        height_window = 500
        button_press_time = 0
        punchCount = 0



    if impact_mid and right_punch == False:
        right_punch_2 = True
        player_movement[0] += player_x_momentum
        player_x_momentum += 2
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 20:
            player_x_momentum = 0
            impact_mid = False


    if impact_full and right_punch == False:
        right_punch_2 = True
        player_movement[0] += player_x_momentum
        player_x_momentum += 10
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 50:
            player_x_momentum = 0
            impact_full = False

    if left_run == True or left_walk == True or right_walk == True or right_run == True:
        right_punch_2 = False

    player_movement[1] += player_y_momentum
    if airtime:
        player_y_momentum += 0.9

    if player_y_momentum > 3:
        player_y_momentum += 0.1

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions["bottom"] == True:
        player_y_momentum = 0
        air_timer = 0
    elif collisions["top"] == True:
        player_y_momentum += 2
        air_timer += 1
    else:
        air_timer += 1

    #Sprite Animation
    if walkCount + 1 >= 25:
        walkCount = 0
    if runCount + 1 >= 25:
        runCount = 0
    if standCount + 1 >= 25:
        standCount = 0
    if punchCount + 1 >= 48:
        punchCount = 48
    if punchCount_2 + 1 >= 16:
        punchCount_2 = 16

    if left_walk:
        window.blit(walkLeft[walkCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        walkCount += 1
    elif right_walk:
        window.blit(walkRight[walkCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        walkCount += 1
    elif left_run:
        window.blit(runLeft[runCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        runCount += 1
    elif right_run:
        window.blit(runRight[runCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        runCount += 1
    elif right_punch:
        window.blit(LoadPunchRight[punchCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount += 1
    elif right_punch_2:
        window.blit(punchRight[punchCount_2//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount_2 += 1
    elif Idle_stand:
        window.blit(Idle[standCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        standCount += 1

    #General Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width_window = pygame.display.Info().current_w
            height_window = pygame.display.Info().current_h
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False



    #Pygame Keys/buttons
    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    if keys[pygame.K_SPACE]:
        airtime = True
        if air_timer < 6:
            player_y_momentum = -7

    if mouse_buttons[0]:
        right_punch = True
        left_run = left_walk = right_walk = right_run = False

    elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        left_run = True
        right_run = left_walk = right_walk = right_punch = False

    elif keys[pygame.K_a]:
        left_walk = True
        right_walk = left_run = right_run = right_punch = False

    elif keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
        right_run = True
        left_run = left_walk = right_walk = right_punch = False

    elif keys[pygame.K_d]:
        right_walk = True
        left_run = right_run = left_walk = right_punch =False

    else:
        Idle_stand = True
        right_walk = left_walk = right_run = left_run = right_punch = False
        walkCount = runCount = 0


    pygame.display.update()

pygame.quit()