
#Mineraria Programmering og Modelering Spill


pygame.init() 

width = 500 #Bredden på vinduet (500 pikeseler)
height = 500 #Høyden på vinduet (500 pikseler) 

window = pygame.display.set_mode((width, height)) 

pygame.display.set_caption("Mineraria") #Barnavnet

width_rect = 40
height_rect = 60
Pos_rect_x = 0
Pos_rect_y = 440

velocity = 5

isJump = False
jumpCount =  10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and Pos_rect_x >= velocity:
        Pos_rect_x -= velocity

    if keys[pygame.K_d] and Pos_rect_x < width - width_rect:
        Pos_rect_x += velocity
    if not(isJump):
        if keys[pygame.K_s] and Pos_rect_y < height - height_rect:
            Pos_rect_y += velocity

        if keys[pygame.K_w] and Pos_rect_y >= velocity:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1 
            if jumpCount < 0:
                neg = -1
            Pos_rect_y -= (jumpCount ** 2)*0.5*neg
            jumpCount  -= 1 
        else:
            isJump = False
            jumpCount = 10


    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (Pos_rect_x, Pos_rect_y, width_rect, height_rect))
    pygame.display.update()

pygame.quit()