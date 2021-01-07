
#Mineraria Programmering og Modelering Spill


import pygame #Importerer pygame bibliotek

pygame.init()

map = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","2","2","2","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","2","1","1","1","2","0","0","0","0","0","0","0"],
       ["2","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["1","2","2","2","2","2","0","0","0","0","0","0","0","0","0","0","0","0","2"],
       ["1","1","1","1","1","1","0","0","0","0","0","0","0","0","2","2","2","2","1"],
       ["1","1","1","1","1","1","2","2","2","2","2","2","2","2","1","1","1","1","1"],
       ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
       ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]


bg = pygame.image.load("bg2.png")
grass = pygame.image.load("grass.png")
dirt = pygame.image.load("dirt.png")

walkRight = [pygame.image.load("R000.png"), pygame.image.load("R002.png"), pygame.image.load("R003.png"), pygame.image.load("R004.png"), pygame.image.load("R005.png"), pygame.image.load("R006.png"), pygame.image.load("R007.png"), pygame.image.load("R008.png"), pygame.image.load("R009.png"), pygame.image.load("R010.png"), pygame.image.load("R011.png"), pygame.image.load("R012.png"), pygame.image.load("R013.png"), pygame.image.load("R014.png"), pygame.image.load("R015.png"), pygame.image.load("R016.png"), pygame.image.load("R017.png"), pygame.image.load("R018.png"), pygame.image.load("R019.png"), pygame.image.load("R020.png"), pygame.image.load("R021.png"), pygame.image.load("R022.png"), pygame.image.load("R023.png"), pygame.image.load("R024.png"), pygame.image.load("R025.png")]
walkLeft = [pygame.image.load("L000.png"), pygame.image.load("L002.png"), pygame.image.load("L003.png"), pygame.image.load("L004.png"), pygame.image.load("L005.png"), pygame.image.load("L006.png"), pygame.image.load("L007.png"), pygame.image.load("L008.png"), pygame.image.load("L009.png"), pygame.image.load("L010.png"), pygame.image.load("L011.png"), pygame.image.load("L012.png"), pygame.image.load("L013.png"), pygame.image.load("L014.png"), pygame.image.load("L015.png"), pygame.image.load("L016.png"), pygame.image.load("L017.png"), pygame.image.load("L018.png"), pygame.image.load("L019.png"), pygame.image.load("L020.png"), pygame.image.load("L021.png"), pygame.image.load("L022.png"), pygame.image.load("L023.png"), pygame.image.load("L024.png"), pygame.image.load("L025.png")]
runLeft = [pygame.image.load("LRun000.png"), pygame.image.load("LRun002.png"), pygame.image.load("LRun003.png"), pygame.image.load("LRun004.png"), pygame.image.load("LRun005.png"), pygame.image.load("LRun006.png"), pygame.image.load("LRun007.png"), pygame.image.load("LRun008.png"), pygame.image.load("LRun009.png"), pygame.image.load("LRun010.png"), pygame.image.load("LRun011.png"), pygame.image.load("LRun012.png"), pygame.image.load("LRun013.png"), pygame.image.load("LRun014.png"), pygame.image.load("LRun015.png"), pygame.image.load("LRun016.png"), pygame.image.load("LRun017.png"), pygame.image.load("LRun018.png"), pygame.image.load("LRun019.png"), pygame.image.load("LRun020.png"), pygame.image.load("LRun021.png"), pygame.image.load("LRun022.png"), pygame.image.load("LRun023.png"), pygame.image.load("LRun024.png"), pygame.image.load("LRun025.png")]
runRight = [pygame.image.load("RRun000.png"), pygame.image.load("RRun002.png"), pygame.image.load("RRun003.png"), pygame.image.load("RRun004.png"), pygame.image.load("RRun005.png"), pygame.image.load("RRun006.png"), pygame.image.load("RRun007.png"), pygame.image.load("RRun008.png"), pygame.image.load("RRun009.png"), pygame.image.load("RRun010.png"), pygame.image.load("RRun011.png"), pygame.image.load("RRun012.png"), pygame.image.load("RRun013.png"), pygame.image.load("RRun014.png"), pygame.image.load("RRun015.png"), pygame.image.load("RRun016.png"), pygame.image.load("RRun017.png"), pygame.image.load("RRun018.png"), pygame.image.load("RRun019.png"), pygame.image.load("RRun020.png"), pygame.image.load("RRun021.png"), pygame.image.load("RRun022.png"), pygame.image.load("RRun023.png"), pygame.image.load("RRun024.png"), pygame.image.load("RRun025.png")]
Idle = [pygame.image.load("Idle000.png"), pygame.image.load("Idle002.png"), pygame.image.load("Idle003.png"), pygame.image.load("Idle004.png"), pygame.image.load("Idle005.png"), pygame.image.load("Idle006.png"), pygame.image.load("Idle007.png"), pygame.image.load("Idle008.png"), pygame.image.load("Idle009.png"), pygame.image.load("Idle010.png"), pygame.image.load("Idle011.png"), pygame.image.load("Idle012.png"), pygame.image.load("Idle013.png"), pygame.image.load("Idle014.png"), pygame.image.load("Idle015.png"), pygame.image.load("Idle016.png"), pygame.image.load("Idle017.png"), pygame.image.load("Idle018.png"), pygame.image.load("Idle019.png"), pygame.image.load("Idle020.png"), pygame.image.load("Idle021.png"), pygame.image.load("Idle022.png"), pygame.image.load("Idle023.png"), pygame.image.load("Idle024.png"), pygame.image.load("Idle025.png")]

width_window = 760 #Bredden på vinduet (500 pikeseler)
height_window = 500 #Høyden på vinduet (500 pikseler)

window_size = (width_window, height_window)

window = pygame.display.set_mode((window_size))

pygame.display.set_caption("Mineraria") #Barnavnet

clock = pygame.time.Clock()

#Character:

width_char = 100
height_char = 95
walkCount = 0
standCount = 0
runCount = 0


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
Jump = False

player_y_momentum = 0
air_timer = 0

def drawGameMap():
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == '1':
                window.blit(dirt, (x * 40, y * 40))
            if tile == '2':
                window.blit(grass, (x * 40, y * 40))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            x += 1
        y += 1


player_rect = pygame.Rect(50, 50, width_char-40, height_char)

run = True

while run:

    clock.tick(30) #Bilder per sekund
    window.blit(bg, (0,0))
    tile_rects = []
    drawGameMap()

    player_movement = [0, 0]
    if right_walk:
        player_movement[0] += 3
    if left_walk:
        player_movement[0] -= 3
    if right_run:
        player_movement[0] += 7
    if left_run:
        player_movement[0] -= 7
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.9
    if player_y_momentum > 3:
        player_y_momentum = 9

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions["bottom"]:
        player_y_momentum = 0
        air_timer = 0
    elif collisions["top"]:
        player_y_momentum += 0.9
    else:
        air_timer += 1

    if walkCount + 1 >= 25:
        walkCount = 0
    if runCount + 1 >= 25:
        runCount = 0
    if standCount + 1 >= 25:
        standCount = 0

    if left_walk:
        window.blit(walkLeft[walkCount//1], (player_rect.x, player_rect.y))
        walkCount += 1
    elif right_walk:
        window.blit(walkRight[walkCount//1], (player_rect.x, player_rect.y))
        walkCount += 1
    elif left_run:
        window.blit(runLeft[runCount//1], (player_rect.x, player_rect.y))
        runCount += 1
    elif right_run:
        window.blit(runRight[runCount//1], (player_rect.x, player_rect.y))
        runCount += 1
    elif Idle_stand:
        window.blit(Idle[standCount//1], (player_rect.x, player_rect.y))
        standCount += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if air_timer < 8:
            player_y_momentum = -8

    elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        left_run = True
        right_run = False
        left_walk = False
        right_walk = False
    elif keys[pygame.K_a]:
        left_walk = True
        right_walk = False
        left_run = False
        right_run = False
    elif keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
        left_run = False
        right_run = True
        left_walk = False
        right_walk = False
    elif keys[pygame.K_d]:
        left_walk = False
        right_walk = True
        left_run = False
        right_run = False
    else:
        right_walk = False
        left_walk = False
        right_run = False
        left_run = False
        Idle_stand = True
        walkCount = 0
        runCount = 0
    pygame.display.update()

pygame.quit()