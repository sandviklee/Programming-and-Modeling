
#Mineraria Programmering og Modelering Spill

import pygame #Importerer pygame bibliotek

pygame.init()

width = 1000 #Bredden på vinduet (500 pikeseler)
height = 500 #Høyden på vinduet (500 pikseler)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Mineraria") #Barnavnet

clock = pygame.time.Clock()

#Character
width_rect = 100
height_rect = 100
Pos_rect_x = 0
Pos_rect_y = 400

#Speed
velocity_run = 15
velocity_walk = 3

#Jumping
isJump = False
jumpCount =  7

#Movement x
left_walk = False
right_walk = False
left_run = False
right_run = False

walkCount = 0
standCount = 0
runCount = 0

bg = pygame.image.load("bg.png")
walkRight = [pygame.image.load("R000.png"), pygame.image.load("R002.png"), pygame.image.load("R003.png"), pygame.image.load("R004.png"), pygame.image.load("R005.png"), pygame.image.load("R006.png"), pygame.image.load("R007.png"), pygame.image.load("R008.png"), pygame.image.load("R009.png"), pygame.image.load("R010.png"), pygame.image.load("R011.png"), pygame.image.load("R012.png"), pygame.image.load("R013.png"), pygame.image.load("R014.png"), pygame.image.load("R015.png"), pygame.image.load("R016.png"), pygame.image.load("R017.png"), pygame.image.load("R018.png"), pygame.image.load("R019.png"), pygame.image.load("R020.png"), pygame.image.load("R021.png"), pygame.image.load("R022.png"), pygame.image.load("R023.png"), pygame.image.load("R024.png"), pygame.image.load("R025.png")]
walkLeft = [pygame.image.load("L000.png"), pygame.image.load("L002.png"), pygame.image.load("L003.png"), pygame.image.load("L004.png"), pygame.image.load("L005.png"), pygame.image.load("L006.png"), pygame.image.load("L007.png"), pygame.image.load("L008.png"), pygame.image.load("L009.png"), pygame.image.load("L010.png"), pygame.image.load("L011.png"), pygame.image.load("L012.png"), pygame.image.load("L013.png"), pygame.image.load("L014.png"), pygame.image.load("L015.png"), pygame.image.load("L016.png"), pygame.image.load("L017.png"), pygame.image.load("L018.png"), pygame.image.load("L019.png"), pygame.image.load("L020.png"), pygame.image.load("L021.png"), pygame.image.load("L022.png"), pygame.image.load("L023.png"), pygame.image.load("L024.png"), pygame.image.load("L025.png")]
runLeft = [pygame.image.load("LRun000.png"), pygame.image.load("LRun002.png"), pygame.image.load("LRun003.png"), pygame.image.load("LRun004.png"), pygame.image.load("LRun005.png"), pygame.image.load("LRun006.png"), pygame.image.load("LRun007.png"), pygame.image.load("LRun008.png"), pygame.image.load("LRun009.png"), pygame.image.load("LRun010.png"), pygame.image.load("LRun011.png"), pygame.image.load("LRun012.png"), pygame.image.load("LRun013.png"), pygame.image.load("LRun014.png"), pygame.image.load("LRun015.png"), pygame.image.load("LRun016.png"), pygame.image.load("LRun017.png"), pygame.image.load("LRun018.png"), pygame.image.load("LRun019.png"), pygame.image.load("LRun020.png"), pygame.image.load("LRun021.png"), pygame.image.load("LRun022.png"), pygame.image.load("LRun023.png"), pygame.image.load("LRun024.png"), pygame.image.load("LRun025.png")]
runRight = [pygame.image.load("RRun000.png"), pygame.image.load("RRun002.png"), pygame.image.load("RRun003.png"), pygame.image.load("RRun004.png"), pygame.image.load("RRun005.png"), pygame.image.load("RRun006.png"), pygame.image.load("RRun007.png"), pygame.image.load("RRun008.png"), pygame.image.load("RRun009.png"), pygame.image.load("RRun010.png"), pygame.image.load("RRun011.png"), pygame.image.load("RRun012.png"), pygame.image.load("RRun013.png"), pygame.image.load("RRun014.png"), pygame.image.load("RRun015.png"), pygame.image.load("RRun016.png"), pygame.image.load("RRun017.png"), pygame.image.load("RRun018.png"), pygame.image.load("RRun019.png"), pygame.image.load("RRun020.png"), pygame.image.load("RRun021.png"), pygame.image.load("RRun022.png"), pygame.image.load("RRun023.png"), pygame.image.load("RRun024.png"), pygame.image.load("RRun025.png")]
Idle = [pygame.image.load("Idle000.png"), pygame.image.load("Idle002.png"), pygame.image.load("Idle003.png"), pygame.image.load("Idle004.png"), pygame.image.load("Idle005.png"), pygame.image.load("Idle006.png"), pygame.image.load("Idle007.png"), pygame.image.load("Idle008.png"), pygame.image.load("Idle009.png"), pygame.image.load("Idle010.png"), pygame.image.load("Idle011.png"), pygame.image.load("Idle012.png"), pygame.image.load("Idle013.png"), pygame.image.load("Idle014.png"), pygame.image.load("Idle015.png"), pygame.image.load("Idle016.png"), pygame.image.load("Idle017.png"), pygame.image.load("Idle018.png"), pygame.image.load("Idle019.png"), pygame.image.load("Idle020.png"), pygame.image.load("Idle021.png"), pygame.image.load("Idle022.png"), pygame.image.load("Idle023.png"), pygame.image.load("Idle024.png"), pygame.image.load("Idle025.png")]




def redrawGameWindow():
    global runCount
    global walkCount
    global standCount
    window.blit(bg, (0,0))

    if walkCount + 1 >= 25:
        walkCount = 0
    if standCount + 1 >= 25:
        standCount = 0
    if runCount + 1 >= 25:
        runCount = 0

    if left_walk:
        window.blit(walkLeft[walkCount//1], (Pos_rect_x, Pos_rect_y))
        walkCount += 1

    elif right_walk:
        window.blit(walkRight[walkCount//1], (Pos_rect_x, Pos_rect_y))
        walkCount += 1

    elif left_run:
        window.blit(runLeft[runCount//1], (Pos_rect_x, Pos_rect_y))
        runCount += 1

    elif right_run:
        window.blit(runRight[runCount//1], (Pos_rect_x, Pos_rect_y))
        runCount += 1

    else:
        window.blit(Idle[standCount//1], (Pos_rect_x, Pos_rect_y))
        standCount += 1


    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and Pos_rect_x >= velocity_walk:
        Pos_rect_x -= velocity_walk
        left_walk = True
        right_walk = False

    elif keys[pygame.K_d] and Pos_rect_x < width - width_rect:
        Pos_rect_x += velocity_walk
        left_walk = False
        right_walk = True

    elif keys[pygame.K_q] and Pos_rect_x >= velocity_run:
        Pos_rect_x -= velocity_run
        left_run = True
        right_run = False

    elif keys[pygame.K_LSHIFT] and keys[pygame.K_e] and  Pos_rect_x < width - width_rect:
        Pos_rect_x += velocity_run
        left_run = False
        right_run = True

    else:
        right_walk = False
        left_walk = False
        right_run = False
        left_run = False
        walkCount = 0
        runCount = 0

    if not(isJump):
        if keys[pygame.K_w] and Pos_rect_y >= velocity_walk:
            isJump = True
            right = False
            left = False
    else:
        if jumpCount >= -7:
            neg = 1
            if jumpCount < 0:
                neg = -1
            Pos_rect_y -= (jumpCount ** 2)*0.5*neg
            jumpCount  -= 1
        else:
            isJump = False
            jumpCount = 7
    redrawGameWindow()


pygame.quit()