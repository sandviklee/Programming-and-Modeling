
#Mineraria Programmering og Modelering Spill

import pygame #Importerer pygame bibliotek

pygame.init() 

width = 500 #Bredden på vinduet (500 pikeseler)
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
velocity = 10

#Jumping 
isJump = False
jumpCount =  7

#Walk
left = False
right = False
walkCount = 0 
walkRight = [pygame.image.load("R000.png"), pygame.image.load("R002.png"), pygame.image.load("R003.png"), pygame.image.load("R004.png"), pygame.image.load("R005.png"), pygame.image.load("R006.png"), pygame.image.load("R007.png"), pygame.image.load("R008.png"), pygame.image.load("R009.png"), pygame.image.load("R010.png"), pygame.image.load("R011.png"), pygame.image.load("R012.png"), pygame.image.load("R013.png"), pygame.image.load("R014.png"), pygame.image.load("R015.png"), pygame.image.load("R016.png"), pygame.image.load("R017.png"), pygame.image.load("R018.png"), pygame.image.load("R019.png"), pygame.image.load("R020.png"), pygame.image.load("R021.png"), pygame.image.load("R022.png"), pygame.image.load("R023.png"), pygame.image.load("R024.png"), pygame.image.load("R025.png")]
walkLeft = [pygame.image.load("L000.png"), pygame.image.load("L002.png"), pygame.image.load("L003.png"), pygame.image.load("L004.png"), pygame.image.load("L005.png"), pygame.image.load("L006.png"), pygame.image.load("L007.png"), pygame.image.load("L008.png"), pygame.image.load("L009.png"), pygame.image.load("L010.png"), pygame.image.load("L011.png"), pygame.image.load("L012.png"), pygame.image.load("L013.png"), pygame.image.load("L014.png"), pygame.image.load("L015.png"), pygame.image.load("L016.png"), pygame.image.load("L017.png"), pygame.image.load("L018.png"), pygame.image.load("L019.png"), pygame.image.load("L020.png"), pygame.image.load("L021.png"), pygame.image.load("L022.png"), pygame.image.load("L023.png"), pygame.image.load("L024.png"), pygame.image.load("L025.png")]
bg = pygame.image.load("bg.png")
Idle = [pygame.image.load("Idle000.png"), pygame.image.load("Idle002.png"), pygame.image.load("Idle003.png"), pygame.image.load("Idle004.png"), pygame.image.load("Idle005.png"), pygame.image.load("Idle006.png"), pygame.image.load("Idle007.png"), pygame.image.load("Idle008.png"), pygame.image.load("Idle009.png"), pygame.image.load("Idle010.png"), pygame.image.load("Idle011.png"), pygame.image.load("Idle012.png"), pygame.image.load("Idle013.png"), pygame.image.load("Idle014.png"), pygame.image.load("Idle015.png"), pygame.image.load("Idle016.png"), pygame.image.load("Idle017.png"), pygame.image.load("Idle018.png"), pygame.image.load("Idle019.png"), pygame.image.load("Idle020.png"), pygame.image.load("Idle021.png"), pygame.image.load("Idle022.png"), pygame.image.load("Idle023.png"), pygame.image.load("Idle024.png"), pygame.image.load("Idle025.png")]


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))

    if walkCount + 1 >= 75:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount//1], (Pos_rect_x, Pos_rect_y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//1], (Pos_rect_x, Pos_rect_y))
        walkCount += 1 
    else:
        window.blit(Idle[walkCount//1], (Pos_rect_x, Pos_rect_y))
        walkCount += 1 

    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and Pos_rect_x >= velocity:
        Pos_rect_x -= velocity
        left = True
        right = False

    elif keys[pygame.K_d] and Pos_rect_x < width - width_rect:
        Pos_rect_x += velocity
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0 

    if not(isJump):
        if keys[pygame.K_w] and Pos_rect_y >= velocity:
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