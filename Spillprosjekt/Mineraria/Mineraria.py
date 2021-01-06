
#Mineraria Programmering og Modelering Spill

import pygame #Importerer pygame bibliotek

pygame.init()

map = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","1","1","1","1","1","0","0","0","0","0","0","0"],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["2","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
       ["1","2","2","2","0","0","0","0","0","0","0","0","0","0","0","0","0","0","2"],
       ["1","1","1","1","2","2","0","0","0","0","0","0","0","0","2","2","2","2","1"],
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

class player(object):
    def __init__(self, Pos_x, Pos_y, width_char, height_char):
        self.Pos_x = Pos_x
        self.Pos_y = Pos_y
        self.width_char = width_char
        self.height_char = height_char
        self.velocity_run = 10
        self.velocity_walk = 3
        self.isJump = False
        self.jumpCount = 7
        self.left_walk = False
        self.right_walk = False
        self.right_run = False
        self.left_run = False
        self.walkCount = 0
        self.standCount = 0
        self.runCount = 0
        self.y_momentum = 0
        self.movement = [0,0]
    def draw(self, window):
        if self.walkCount + 1 >= 25:
            self.walkCount = 0
        if self.standCount + 1 >= 25:
            self.standCount = 0
        if self.runCount + 1 >= 25:
            self.runCount = 0
        if self.left_walk:
            window.blit(walkLeft[self.walkCount//1], (self.Pos_x, self.Pos_y))
            self.walkCount += 1
        elif self.right_walk:
            window.blit(walkRight[self.walkCount//1], (self.Pos_x, self.Pos_y))
            self.walkCount += 1
        elif self.left_run:
            window.blit(runLeft[self.runCount//1], (self.Pos_x, self.Pos_y))
            self.runCount += 1
        elif self.right_run:
            window.blit(runRight[self.runCount//1], (self.Pos_x, self.Pos_y))
            self.runCount += 1
        else:
            window.blit(Idle[self.standCount//1], (self.Pos_x, self.Pos_y))
            self.standCount += 1

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += Steve.Pos_x
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if Steve.Pos_x > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif Steve.Pos_x < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += Steve.Pos_y
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if Steve.Pos_y > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif Steve.Pos_y < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


#mainloop
Steve = player(50, 20, 100, 100)
Char_rect = pygame.Rect(Steve.Pos_x, Steve.Pos_y, Steve.width_char, Steve.height_char)

run = True

while run:
    clock.tick(25)
    window.blit(bg, (0,0))
    tile_rects = []
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == "1":
                window.blit(dirt, (x * 40, y * 40))
            if tile == "2":
                window.blit(grass, (x * 40, y * 40))
            if tile != "0":
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            x += 1
        y += 1

    movement = [0, 0]
    if Steve.left_walk:
        movement[0] -= Steve.velocity_walk
        Steve.Pos_x -= Steve.velocity_walk
    if Steve.right_walk:
        movement[0] += Steve.velocity_walk
        Steve.Pos_x += Steve.velocity_walk
    if Steve.left_run:
        movement[0] -= Steve.velocity_run
        Steve.Pos_x -= Steve.velocity_run
    if Steve.right_run:
        movement[0] += Steve.velocity_run
        Steve.Pos_x += Steve.velocity_run

    Steve.Pos_y += Steve.y_momentum
    movement[1] += Steve.y_momentum
    if Steve.y_momentum > 3:
        Steve.y_momentum = 9

    if Steve.Pos_y > window_size[1] - Steve.height_char:
        Steve.y_momentum = -Steve.y_momentum
    else:
        Steve.y_momentum += 0.9
    Steve.Pos_y += Steve.y_momentum

    Char_rect, collision = move(Char_rect, movement, tile_rects)

    Steve.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and keys[pygame.K_LSHIFT] and Steve.Pos_x >= Steve.velocity_run:
        Steve.left_run = True
        Steve.right_run = False
        Steve.left_walk = False
        Steve.right_walk = False

    elif keys[pygame.K_a] and Steve.Pos_x >= Steve.velocity_walk:
        Steve.left_walk = True
        Steve.right_walk = False
        Steve.left_run = False
        Steve.right_run = False

    elif keys[pygame.K_LSHIFT] and keys[pygame.K_d] and  Steve.Pos_x < width_window - Steve.width_char:
        Steve.left_run = False
        Steve.right_run = True
        Steve.left_walk = False
        Steve.right_walk = False

    elif keys[pygame.K_d] and Steve.Pos_x < width_window - Steve.width_char:
        Steve.left_walk = False
        Steve.right_walk = True
        Steve.left_run = False
        Steve.right_run = False

    else:
        Steve.right_walk = False
        Steve.left_walk = False
        Steve.right_run = False
        Steve.left_run = False
        Steve.walkCount = 0
        Steve.runCount = 0

    pygame.display.update()


pygame.quit()