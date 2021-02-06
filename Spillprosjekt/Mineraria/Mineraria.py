#Mineraria Programmering og Modellering Spill

import pygame, random #Importerer pygame bibliotek

pygame.init()

#Sprites world
bg = pygame.image.load("Tex/Backgrounds/bg3.png")
grass = pygame.image.load("Tex/Blocks/grass.png")
dirt = pygame.image.load("Tex/Blocks/dirt.png")
stone = pygame.image.load("Tex/Blocks/stone.png")
oak_wood = pygame.transform.scale(pygame.image.load("Tex/Blocks/oak_planks.png"), (40, 40))
oak_log = pygame.transform.scale(pygame.image.load("Tex/Blocks/oak_log.png"), (40, 40))
glass = pygame.transform.scale(pygame.image.load("Tex/Blocks/glass.png"), (40, 40))
furnace = pygame.transform.scale(pygame.image.load("Tex/Blocks/furnace_front.png"), (40, 40))
craftingtable = pygame.transform.scale(pygame.image.load("Tex/Blocks/crafting_table_front.png"), (40, 40))
#diamondanimation = [pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds00.png"), (32, 32)), pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds01.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds02.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds03.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds04.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds05.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds06.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds07.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds08.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds09.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds10.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds11.png"), (32, 32)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds12.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds13.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds14.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds15.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds16.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds17.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds18.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds19.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds20.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds21.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds22.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds23.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds24.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds25.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds24.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds23.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds22.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds21.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds20.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds19.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds18.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds17.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds16.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds15.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds14.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds13.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds12.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds11.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds10.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds09.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds08.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds07.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds06.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds05.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds04.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds03.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds02.png"), (24, 24)),pygame.transform.scale(pygame.image.load("Tex/Blocks/diamonds/Diamonds01.png"), (24, 24))]
diamond = pygame.transform.scale(pygame.image.load("Tex/Blocks/diamond.png"), (24, 24))
sign = pygame.transform.scale(pygame.image.load("Tex/Blocks/oak_sign.png"), (40, 40))

#GUI
HeartB = pygame.transform.scale(pygame.image.load("Tex/GUI/HeartB.png"), (27, 27))
HeartR = pygame.transform.scale(pygame.image.load("Tex/GUI/HeartR.png"), (27, 27))
Itembar = [pygame.transform.scale(pygame.image.load("Tex/GUI/Itembar1.png"), (180, 60)), pygame.transform.scale(pygame.image.load("Tex/GUI/Itembar2.png"), (180, 60))]
txt_background = pygame.transform.scale(pygame.image.load("Tex/GUI/Txt_background.png"), (124, 32))
tutImage1 = pygame.image.load("Tex/GUI/tutImage1.png")
tutImage2 = pygame.image.load("Tex/GUI/tutImage2.png")
tutImage3 = pygame.image.load("Tex/GUI/tutImage3.png")
tutImage4 = pygame.image.load("Tex/GUI/tutImage4.png")
E_button = pygame.transform.scale(pygame.image.load("Tex/GUI/E_Button.png"), (20, 22))

#Sprites Player
walkRight = [pygame.image.load("Tex/Animations/Main character/R000.png"), pygame.image.load("Tex/Animations/Main character/R002.png"), pygame.image.load("Tex/Animations/Main character/R003.png"), pygame.image.load("Tex/Animations/Main character/R004.png"), pygame.image.load("Tex/Animations/Main character/R005.png"), pygame.image.load("Tex/Animations/Main character/R006.png"), pygame.image.load("Tex/Animations/Main character/R007.png"), pygame.image.load("Tex/Animations/Main character/R008.png"), pygame.image.load("Tex/Animations/Main character/R009.png"), pygame.image.load("Tex/Animations/Main character/R010.png"), pygame.image.load("Tex/Animations/Main character/R011.png"), pygame.image.load("Tex/Animations/Main character/R012.png"), pygame.image.load("Tex/Animations/Main character/R013.png"), pygame.image.load("Tex/Animations/Main character/R014.png"), pygame.image.load("Tex/Animations/Main character/R015.png"), pygame.image.load("Tex/Animations/Main character/R016.png"), pygame.image.load("Tex/Animations/Main character/R017.png"), pygame.image.load("Tex/Animations/Main character/R018.png"), pygame.image.load("Tex/Animations/Main character/R019.png"), pygame.image.load("Tex/Animations/Main character/R020.png"), pygame.image.load("Tex/Animations/Main character/R021.png"), pygame.image.load("Tex/Animations/Main character/R022.png"), pygame.image.load("Tex/Animations/Main character/R023.png"), pygame.image.load("Tex/Animations/Main character/R024.png"), pygame.image.load("Tex/Animations/Main character/R025.png")]
walkLeft = [pygame.image.load("Tex/Animations/Main character/L000.png"), pygame.image.load("Tex/Animations/Main character/L002.png"), pygame.image.load("Tex/Animations/Main character/L003.png"), pygame.image.load("Tex/Animations/Main character/L004.png"), pygame.image.load("Tex/Animations/Main character/L005.png"), pygame.image.load("Tex/Animations/Main character/L006.png"), pygame.image.load("Tex/Animations/Main character/L007.png"), pygame.image.load("Tex/Animations/Main character/L008.png"), pygame.image.load("Tex/Animations/Main character/L009.png"), pygame.image.load("Tex/Animations/Main character/L010.png"), pygame.image.load("Tex/Animations/Main character/L011.png"), pygame.image.load("Tex/Animations/Main character/L012.png"), pygame.image.load("Tex/Animations/Main character/L013.png"), pygame.image.load("Tex/Animations/Main character/L014.png"), pygame.image.load("Tex/Animations/Main character/L015.png"), pygame.image.load("Tex/Animations/Main character/L016.png"), pygame.image.load("Tex/Animations/Main character/L017.png"), pygame.image.load("Tex/Animations/Main character/L018.png"), pygame.image.load("Tex/Animations/Main character/L019.png"), pygame.image.load("Tex/Animations/Main character/L020.png"), pygame.image.load("Tex/Animations/Main character/L021.png"), pygame.image.load("Tex/Animations/Main character/L022.png"), pygame.image.load("Tex/Animations/Main character/L023.png"), pygame.image.load("Tex/Animations/Main character/L024.png"), pygame.image.load("Tex/Animations/Main character/L025.png")]
runLeft = [pygame.image.load("Tex/Animations/Main character/LRun000.png"), pygame.image.load("Tex/Animations/Main character/LRun002.png"), pygame.image.load("Tex/Animations/Main character/LRun003.png"), pygame.image.load("Tex/Animations/Main character/LRun004.png"), pygame.image.load("Tex/Animations/Main character/LRun005.png"), pygame.image.load("Tex/Animations/Main character/LRun006.png"), pygame.image.load("Tex/Animations/Main character/LRun007.png"), pygame.image.load("Tex/Animations/Main character/LRun008.png"), pygame.image.load("Tex/Animations/Main character/LRun009.png"), pygame.image.load("Tex/Animations/Main character/LRun010.png"), pygame.image.load("Tex/Animations/Main character/LRun011.png"), pygame.image.load("Tex/Animations/Main character/LRun012.png"), pygame.image.load("Tex/Animations/Main character/LRun013.png"), pygame.image.load("Tex/Animations/Main character/LRun014.png"), pygame.image.load("Tex/Animations/Main character/LRun015.png"), pygame.image.load("Tex/Animations/Main character/LRun016.png"), pygame.image.load("Tex/Animations/Main character/LRun017.png"), pygame.image.load("Tex/Animations/Main character/LRun018.png"), pygame.image.load("Tex/Animations/Main character/LRun019.png"), pygame.image.load("Tex/Animations/Main character/LRun020.png"), pygame.image.load("Tex/Animations/Main character/LRun021.png"), pygame.image.load("Tex/Animations/Main character/LRun022.png"), pygame.image.load("Tex/Animations/Main character/LRun023.png"), pygame.image.load("Tex/Animations/Main character/LRun024.png"), pygame.image.load("Tex/Animations/Main character/LRun025.png")]
runRight = [pygame.image.load("Tex/Animations/Main character/RRun000.png"), pygame.image.load("Tex/Animations/Main character/RRun002.png"), pygame.image.load("Tex/Animations/Main character/RRun003.png"), pygame.image.load("Tex/Animations/Main character/RRun004.png"), pygame.image.load("Tex/Animations/Main character/RRun005.png"), pygame.image.load("Tex/Animations/Main character/RRun006.png"), pygame.image.load("Tex/Animations/Main character/RRun007.png"), pygame.image.load("Tex/Animations/Main character/RRun008.png"), pygame.image.load("Tex/Animations/Main character/RRun009.png"), pygame.image.load("Tex/Animations/Main character/RRun010.png"), pygame.image.load("Tex/Animations/Main character/RRun011.png"), pygame.image.load("Tex/Animations/Main character/RRun012.png"), pygame.image.load("Tex/Animations/Main character/RRun013.png"), pygame.image.load("Tex/Animations/Main character/RRun014.png"), pygame.image.load("Tex/Animations/Main character/RRun015.png"), pygame.image.load("Tex/Animations/Main character/RRun016.png"), pygame.image.load("Tex/Animations/Main character/RRun017.png"), pygame.image.load("Tex/Animations/Main character/RRun018.png"), pygame.image.load("Tex/Animations/Main character/RRun019.png"), pygame.image.load("Tex/Animations/Main character/RRun020.png"), pygame.image.load("Tex/Animations/Main character/RRun021.png"), pygame.image.load("Tex/Animations/Main character/RRun022.png"), pygame.image.load("Tex/Animations/Main character/RRun023.png"), pygame.image.load("Tex/Animations/Main character/RRun024.png"), pygame.image.load("Tex/Animations/Main character/RRun025.png")]
Idle = [pygame.image.load("Tex/Animations/Main character/Idle000.png"), pygame.image.load("Tex/Animations/Main character/Idle002.png"), pygame.image.load("Tex/Animations/Main character/Idle003.png"), pygame.image.load("Tex/Animations/Main character/Idle004.png"), pygame.image.load("Tex/Animations/Main character/Idle005.png"), pygame.image.load("Tex/Animations/Main character/Idle006.png"), pygame.image.load("Tex/Animations/Main character/Idle007.png"), pygame.image.load("Tex/Animations/Main character/Idle008.png"), pygame.image.load("Tex/Animations/Main character/Idle009.png"), pygame.image.load("Tex/Animations/Main character/Idle010.png"), pygame.image.load("Tex/Animations/Main character/Idle011.png"), pygame.image.load("Tex/Animations/Main character/Idle012.png"), pygame.image.load("Tex/Animations/Main character/Idle013.png"), pygame.image.load("Tex/Animations/Main character/Idle014.png"), pygame.image.load("Tex/Animations/Main character/Idle015.png"), pygame.image.load("Tex/Animations/Main character/Idle016.png"), pygame.image.load("Tex/Animations/Main character/Idle017.png"), pygame.image.load("Tex/Animations/Main character/Idle018.png"), pygame.image.load("Tex/Animations/Main character/Idle019.png"), pygame.image.load("Tex/Animations/Main character/Idle020.png"), pygame.image.load("Tex/Animations/Main character/Idle021.png"), pygame.image.load("Tex/Animations/Main character/Idle022.png"), pygame.image.load("Tex/Animations/Main character/Idle023.png"), pygame.image.load("Tex/Animations/Main character/Idle024.png"), pygame.image.load("Tex/Animations/Main character/Idle025.png")]
LoadPunchRight = [pygame.image.load("Tex/Animations/Main character/Attacks/LPR000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR016.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR017.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR018.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR019.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR020.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR021.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR022.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR023.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR024.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR025.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR026.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR027.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR028.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR029.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR030.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR031.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR032.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR033.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR034.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR035.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR036.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR037.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR038.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR039.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR040.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR041.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR042.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR043.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR044.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR045.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR046.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR047.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPR048.png")]
punchRight = [pygame.image.load("Tex/Animations/Main character/Attacks/PR000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PR016.png")]
LoadPunchLeft = [pygame.image.load("Tex/Animations/Main character/Attacks/LPL000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL016.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL017.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL018.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL019.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL020.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL021.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL022.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL023.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL024.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL025.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL026.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL027.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL028.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL029.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL030.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL031.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL032.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL033.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL034.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL035.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL036.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL037.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL038.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL039.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL040.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL041.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL042.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL043.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL044.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL045.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL046.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL047.png"), pygame.image.load("Tex/Animations/Main character/Attacks/LPL048.png")]
punchLeft = [pygame.image.load("Tex/Animations/Main character/Attacks/PL000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/PL016.png")]
arrowRight = [pygame.image.load("Tex/Animations/Main character/Attacks/BR000.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR001.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR002.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR003.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR004.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR005.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR006.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR007.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR008.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR009.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR010.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR011.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR012.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR013.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR014.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR015.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR016.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR017.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR018.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR019.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR020.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR021.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR022.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR023.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR024.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR025.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR026.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR027.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR028.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR029.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR030.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR031.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR032.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR033.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR034.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR035.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR036.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR037.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR038.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR039.png"), pygame.image.load("Tex/Animations/Main character/Attacks/BR040.png")]

#screen size
width_window = 800 #Bredden på vinduet (800 pikeseler)
height_window = 500 #Høyden på vinduet (500 pikseler)

window_size = (width_window, height_window)

window = pygame.display.set_mode((window_size), pygame.RESIZABLE)

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("Mineraria") #Barnavnet
pygame.display.set_icon(grass)

clock = pygame.time.Clock()

Score = 0
font = pygame.font.Font("Tex/Fonts/Minecraft.ttf", 24)
font2 = pygame.font.Font("Tex/Fonts/Minecraft.ttf", 25)
font_arrow = pygame.font.Font("Tex/Fonts/Minecraft.ttf", 18)


#Enemy
class Zombie(object):
    Zombie_Right = [pygame.image.load("Tex/Animations/Zombie/ZR000.png"),pygame.image.load("Tex/Animations/Zombie/ZR001.png"),pygame.image.load("Tex/Animations/Zombie/ZR002.png"),pygame.image.load("Tex/Animations/Zombie/ZR003.png"),pygame.image.load("Tex/Animations/Zombie/ZR004.png"),pygame.image.load("Tex/Animations/Zombie/ZR005.png"),pygame.image.load("Tex/Animations/Zombie/ZR006.png"),pygame.image.load("Tex/Animations/Zombie/ZR007.png"),pygame.image.load("Tex/Animations/Zombie/ZR008.png"),pygame.image.load("Tex/Animations/Zombie/ZR009.png"),pygame.image.load("Tex/Animations/Zombie/ZR010.png"),pygame.image.load("Tex/Animations/Zombie/ZR011.png"),pygame.image.load("Tex/Animations/Zombie/ZR012.png"),pygame.image.load("Tex/Animations/Zombie/ZR013.png"),pygame.image.load("Tex/Animations/Zombie/ZR014.png"),pygame.image.load("Tex/Animations/Zombie/ZR015.png"),pygame.image.load("Tex/Animations/Zombie/ZR016.png"),pygame.image.load("Tex/Animations/Zombie/ZR017.png"),pygame.image.load("Tex/Animations/Zombie/ZR018.png"),pygame.image.load("Tex/Animations/Zombie/ZR019.png"),pygame.image.load("Tex/Animations/Zombie/ZR020.png"),pygame.image.load("Tex/Animations/Zombie/ZR021.png"),pygame.image.load("Tex/Animations/Zombie/ZR022.png"),pygame.image.load("Tex/Animations/Zombie/ZR023.png"),pygame.image.load("Tex/Animations/Zombie/ZR024.png"),pygame.image.load("Tex/Animations/Zombie/ZR025.png"),pygame.image.load("Tex/Animations/Zombie/ZR026.png"),pygame.image.load("Tex/Animations/Zombie/ZR027.png"),pygame.image.load("Tex/Animations/Zombie/ZR028.png"),pygame.image.load("Tex/Animations/Zombie/ZR029.png"),pygame.image.load("Tex/Animations/Zombie/ZR030.png"),pygame.image.load("Tex/Animations/Zombie/ZR031.png"),pygame.image.load("Tex/Animations/Zombie/ZR032.png"),pygame.image.load("Tex/Animations/Zombie/ZR033.png"),pygame.image.load("Tex/Animations/Zombie/ZR034.png"),pygame.image.load("Tex/Animations/Zombie/ZR035.png"),pygame.image.load("Tex/Animations/Zombie/ZR036.png"),pygame.image.load("Tex/Animations/Zombie/ZR037.png"),pygame.image.load("Tex/Animations/Zombie/ZR038.png"),pygame.image.load("Tex/Animations/Zombie/ZR039.png"),pygame.image.load("Tex/Animations/Zombie/ZR040.png"),pygame.image.load("Tex/Animations/Zombie/ZR041.png"),pygame.image.load("Tex/Animations/Zombie/ZR042.png"),pygame.image.load("Tex/Animations/Zombie/ZR043.png"),pygame.image.load("Tex/Animations/Zombie/ZR044.png")]
    Zombie_Left = [pygame.image.load("Tex/Animations/Zombie/ZL000.png"),pygame.image.load("Tex/Animations/Zombie/ZL001.png"),pygame.image.load("Tex/Animations/Zombie/ZL002.png"),pygame.image.load("Tex/Animations/Zombie/ZL003.png"),pygame.image.load("Tex/Animations/Zombie/ZL004.png"),pygame.image.load("Tex/Animations/Zombie/ZL005.png"),pygame.image.load("Tex/Animations/Zombie/ZL006.png"),pygame.image.load("Tex/Animations/Zombie/ZL007.png"),pygame.image.load("Tex/Animations/Zombie/ZL008.png"),pygame.image.load("Tex/Animations/Zombie/ZL009.png"),pygame.image.load("Tex/Animations/Zombie/ZL010.png"),pygame.image.load("Tex/Animations/Zombie/ZL011.png"),pygame.image.load("Tex/Animations/Zombie/ZL012.png"),pygame.image.load("Tex/Animations/Zombie/ZL013.png"),pygame.image.load("Tex/Animations/Zombie/ZL014.png"),pygame.image.load("Tex/Animations/Zombie/ZL015.png"),pygame.image.load("Tex/Animations/Zombie/ZL016.png"),pygame.image.load("Tex/Animations/Zombie/ZL017.png"),pygame.image.load("Tex/Animations/Zombie/ZL018.png"),pygame.image.load("Tex/Animations/Zombie/ZL019.png"),pygame.image.load("Tex/Animations/Zombie/ZL020.png"),pygame.image.load("Tex/Animations/Zombie/ZL021.png"),pygame.image.load("Tex/Animations/Zombie/ZL022.png"),pygame.image.load("Tex/Animations/Zombie/ZL023.png"),pygame.image.load("Tex/Animations/Zombie/ZL024.png"),pygame.image.load("Tex/Animations/Zombie/ZL025.png"),pygame.image.load("Tex/Animations/Zombie/ZL026.png"),pygame.image.load("Tex/Animations/Zombie/ZL027.png"),pygame.image.load("Tex/Animations/Zombie/ZL028.png"),pygame.image.load("Tex/Animations/Zombie/ZL029.png"),pygame.image.load("Tex/Animations/Zombie/ZL030.png"),pygame.image.load("Tex/Animations/Zombie/ZL031.png"),pygame.image.load("Tex/Animations/Zombie/ZL032.png"),pygame.image.load("Tex/Animations/Zombie/ZL033.png"),pygame.image.load("Tex/Animations/Zombie/ZL034.png"),pygame.image.load("Tex/Animations/Zombie/ZL035.png"),pygame.image.load("Tex/Animations/Zombie/ZL036.png"),pygame.image.load("Tex/Animations/Zombie/ZL037.png"),pygame.image.load("Tex/Animations/Zombie/ZL038.png"),pygame.image.load("Tex/Animations/Zombie/ZL039.png"),pygame.image.load("Tex/Animations/Zombie/ZL040.png"),pygame.image.load("Tex/Animations/Zombie/ZL041.png"),pygame.image.load("Tex/Animations/Zombie/ZL042.png"),pygame.image.load("Tex/Animations/Zombie/ZL043.png"),pygame.image.load("Tex/Animations/Zombie/ZL044.png")]
    Zombie_damage_left = [pygame.image.load("Tex/Animations/Zombie/ZLD000.png"),pygame.image.load("Tex/Animations/Zombie/ZLD001.png"),pygame.image.load("Tex/Animations/Zombie/ZLD002.png"),pygame.image.load("Tex/Animations/Zombie/ZLD003.png"),pygame.image.load("Tex/Animations/Zombie/ZLD004.png"),pygame.image.load("Tex/Animations/Zombie/ZLD005.png"),pygame.image.load("Tex/Animations/Zombie/ZLD006.png"),pygame.image.load("Tex/Animations/Zombie/ZLD007.png"),pygame.image.load("Tex/Animations/Zombie/ZLD008.png"),pygame.image.load("Tex/Animations/Zombie/ZLD009.png"),pygame.image.load("Tex/Animations/Zombie/ZLD010.png"),pygame.image.load("Tex/Animations/Zombie/ZLD011.png"),pygame.image.load("Tex/Animations/Zombie/ZLD012.png"),pygame.image.load("Tex/Animations/Zombie/ZLD013.png"),pygame.image.load("Tex/Animations/Zombie/ZLD014.png"),pygame.image.load("Tex/Animations/Zombie/ZLD015.png"),pygame.image.load("Tex/Animations/Zombie/ZLD016.png"),pygame.image.load("Tex/Animations/Zombie/ZLD017.png"),pygame.image.load("Tex/Animations/Zombie/ZLD018.png"),pygame.image.load("Tex/Animations/Zombie/ZLD019.png"),pygame.image.load("Tex/Animations/Zombie/ZLD020.png"),pygame.image.load("Tex/Animations/Zombie/ZLD021.png"),pygame.image.load("Tex/Animations/Zombie/ZLD022.png"),pygame.image.load("Tex/Animations/Zombie/ZLD023.png"),pygame.image.load("Tex/Animations/Zombie/ZLD024.png")]
    Zombie_damage_right = [pygame.image.load("Tex/Animations/Zombie/ZRD000.png"),pygame.image.load("Tex/Animations/Zombie/ZRD001.png"),pygame.image.load("Tex/Animations/Zombie/ZRD002.png"),pygame.image.load("Tex/Animations/Zombie/ZRD003.png"),pygame.image.load("Tex/Animations/Zombie/ZRD004.png"),pygame.image.load("Tex/Animations/Zombie/ZRD005.png"),pygame.image.load("Tex/Animations/Zombie/ZRD006.png"),pygame.image.load("Tex/Animations/Zombie/ZRD007.png"),pygame.image.load("Tex/Animations/Zombie/ZRD008.png"),pygame.image.load("Tex/Animations/Zombie/ZRD009.png"),pygame.image.load("Tex/Animations/Zombie/ZRD010.png"),pygame.image.load("Tex/Animations/Zombie/ZRD011.png"),pygame.image.load("Tex/Animations/Zombie/ZRD012.png"),pygame.image.load("Tex/Animations/Zombie/ZRD013.png"),pygame.image.load("Tex/Animations/Zombie/ZRD014.png"),pygame.image.load("Tex/Animations/Zombie/ZRD015.png"),pygame.image.load("Tex/Animations/Zombie/ZRD016.png"),pygame.image.load("Tex/Animations/Zombie/ZRD017.png"),pygame.image.load("Tex/Animations/Zombie/ZRD018.png"),pygame.image.load("Tex/Animations/Zombie/ZRD019.png"),pygame.image.load("Tex/Animations/Zombie/ZRD020.png"),pygame.image.load("Tex/Animations/Zombie/ZRD021.png"),pygame.image.load("Tex/Animations/Zombie/ZRD022.png"),pygame.image.load("Tex/Animations/Zombie/ZRD023.png"),pygame.image.load("Tex/Animations/Zombie/ZRD024.png")]
    def __init__(self, x, y, width, height, velocity, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = start
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.damageCount_l = 0
        self.damageCount_r = 0
        self.tookDamage = 0
        self.vel = 2
        self.velocity = velocity
        self.hitbox = pygame.Rect(self.x, self.y, 40, 85)
        self.health = 10
        self.visible = True
        self.Damage_left = False
        self.Damage_right = False
        self.atEnd = False
        self.atStart = False
        self.dead = []

    def draw(self, window):
        if self.visible == True:
            self.move()
            if self.walkCount + 1 >= 44:
                self.walkCount = 21
            if self.damageCount_l + 1 >= 23:
                self.damageCount_l = 0
            if self.damageCount_r + 1 >= 23:
                self.damageCount_r = 0

            if self.vel > 0 and self.Damage_right == False and self.Damage_left == False:
                window.blit(self.Zombie_Right[self.walkCount//1], (self.x - scroll[0], self.y - scroll[1]))
                self.walkCount += 1
            elif self.vel < 0 and self.Damage_right == False and self.Damage_left == False:
                window.blit(self.Zombie_Left[self.walkCount//1], (self.x - scroll[0], self.y - scroll[1]))
                self.walkCount += 1
            elif self.Damage_right == True:
                window.blit(self.Zombie_damage_left[self.damageCount_l//1], (self.x - scroll[0], self.y - scroll[1]))
                self.damageCount_l += 1
            elif self.Damage_left == True:
                window.blit(self.Zombie_damage_right[self.damageCount_r//1], (self.x - scroll[0], self.y - scroll[1]))
                self.damageCount_r += 1

            self.hitbox = pygame.Rect((self.x - scroll[0]) + 5, self.y - scroll[1], 45, 85)
            pygame.draw.rect(window, (200,0,0), ((self.x - scroll[0]) + 4, (self.y - scroll[1]) - 10, 50, 5))
            pygame.draw.rect(window, (0,175,0), ((self.x - scroll[0]) + 4, (self.y - scroll[1]) - 10, 50 - (5 * (10 - self.health)), 5))
            #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
    def move(self):
        if self.y < player_rect.y:
            if self.x + self.vel < player_rect.x and self.Damage_left == False and self.Damage_right == False:
                self.vel = self.velocity + 1.5
                self.x += self.vel
            elif self.x + self.vel > player_rect.x and self.Damage_left == False and self.Damage_right == False:
                self.vel = -(self.velocity + 1.5)
                self.x += self.vel
            elif self.Damage_left == True:
                self.Damage_right = False
                self.vel = 0
                self.tookDamage += 1
                if self.tookDamage == 23:
                    self.tookDamage = 0
                    self.damageCount_l = 0
                    self.damageCount_r = 0
                    self.walkCount = 0
                    self.Damage_left = False

            elif self.Damage_right == True:
                self.Damage_left = False
                self.vel = 0
                self.tookDamage += 1
                if self.tookDamage == 23:
                    self.tookDamage = 0
                    self.damageCount_l = 0
                    self.damageCount_r = 0
                    self.walkCount = 0
                    self.Damage_right = False
            else:
                self.walkCount = 21
                self.damageCount_r = 0
                self.damageCount_l = 0
                self.Damage_left = False
                self.Damage_right = False
        else:
            if self.x + self.vel < self.end and self.atEnd == False and self.atStart == True:
                self.vel = self.velocity
                self.x += self.vel
                if self.x > self.end - 5:
                    self.atEnd = True
                    self.atStart = False
            elif self.x + self.vel > self.start and self.atEnd == True and self.atStart == False:
                self.vel = -self.velocity
                self.x += self.vel
                if self.x + self.vel == self.start:
                    self.atStart = True
                    self.atEnd = False
            else:
                self.atEnd = False
                self.atStart = True
                self.walkCount = 21
    def hit(self):
        if self.x + self.vel < player_rect.x:
            self.Damage_left = False
            self.Damage_right = True
        elif self.x + self.vel > player_rect.x:
            self.Damage_right = False
            self.Damage_left = True


def HitZombie(Zombie, Damage):
    if player_hitbox.colliderect(Zombie.hitbox) == 1:
        if Zombie.health > 0:
            Zombie.health -= Damage
        else:
            Zombie.visible = False
        Zombie.hit()
    return Zombie.health


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

tile_index = {1:dirt, 2:grass, 3:stone, 4:oak_log, 5:oak_wood, 6:glass, 7:craftingtable, 8:diamond, 9:sign}

def drawGameMap():
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == "1":
                window.blit(dirt, (x * 40 - scroll[0], y * 40 - scroll[1]))
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            if tile == "2":
                window.blit(grass, (x * 40 - scroll[0], y * 40 - scroll[1]))
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            if tile == "3":
                window.blit(stone, (x * 40 - scroll[0], y * 40 - scroll[1]))
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            if tile == "4":
                window.blit(oak_log, (x * 40 - scroll[0], y * 40 - scroll[1]))
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            if tile == "5":
                window.blit(oak_wood, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "6":
                window.blit(glass, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "7":
                window.blit(craftingtable, (x * 40 - scroll[0], y * 40 - scroll[1]))
                tile_rects.append(pygame.Rect(x * 40, y * 40, 40, 40))
            if tile == "8":
                window.blit(dirt, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "9":
                window.blit(sign, (x * 40 - scroll[0], y * 40 - scroll[1]))
            if tile == "0":
                pass
            x += 1
        y += 1

#Player:
width_player = 40
height_player = 80
walkCount = 0
standCount = 0
runCount = 0
punchCount_r = 0
punchCount_2_r = 0
punchCount_l = 0
punchCount_2_l = 0
arrowCount_r = 0

player_x_momentum = 0
player_y_momentum = 0
true_scroll = [0, 0]
button_press_time_r = 0
button_press_time_l = 0
current_time = 0

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

player_health = 3

#Moving
left_walk = False
right_walk = False
right_run = False
left_run = False
Idle_stand = False
moving_right = False
moving_left = False
sneak = False

#Attacks
#punch
right_punch = False
right_punch_2 = False
left_punch = False
left_punch_2 = False
impact_full_r = False
impact_mid_r = False
impact_full_l = False
impact_mid_l = False
#arrow
right_arrow = False
left_arrow = False
right_arrow_2 = False
left_arrow_2 = False
Arrows = 0

#Jump
airtime = True
follow_player = False
air_timer = 0

#Score
diamonds = [
    pygame.Rect(246, 410, 16, 16),
    pygame.Rect(295, 650, 16, 16),
    pygame.Rect(335, 650, 40, 40),
    pygame.Rect(128, 252, 16, 16),
    pygame.Rect(88, 252, 16, 16),
    pygame.Rect(48, 252, 16, 16),
    #Hard to get
    pygame.Rect(847, -35, 16, 16),
    pygame.Rect(887, -35, 16, 16),
    pygame.Rect(927, -35, 16, 16),
    pygame.Rect(967, -35, 16, 16),
    pygame.Rect(1007, -35, 16, 16),
    pygame.Rect(1047, -35, 16, 16),
    pygame.Rect(1087, -35, 16, 16),
    pygame.Rect(1127, -35, 16, 16),
    pygame.Rect(1287, -35, 16, 16),
    pygame.Rect(1327, -35, 16, 16),

]

diamondCount = 0
remove_diamond = False
diamondFloat = True
z = 0

#Signs - Tutorials
signs = [
    pygame.Rect(520, 400, 40, 40),
    pygame.Rect(202, 400, 40, 40),
    pygame.Rect(242, 640, 40, 40),
    pygame.Rect(1190, 560, 40, 40),

]
showTut1 = False
showTut1Image = False
showTut2 = False
showTut2Image = False
showTut3 = False
showTut3Image = False
showTut4 = False
showTut4Image = False



#Screen
Fullscreen = False
run = True
screenshake = 0

#Draw
player_rect = pygame.Rect(740, 340, width_player, height_player)
Zombie_1 = Zombie(360, 638, 45, 85, 2, 360, 880)
Zombie_2 = Zombie(1557, 600, 45, 85, 4, 1557, 1650)

while run:
    #Generelt
    clock.tick(50) #Bilder per sekund
    window.blit(bg, (0,0))
    current_time = int(pygame.time.get_ticks()*1E-3)

    #Camera
    if follow_player:
        true_scroll[0] += (player_rect.x - true_scroll[0] - (width_window))
        true_scroll[1] += (player_rect.y - true_scroll[1] - (height_window))
    else:
        true_scroll[0] += (player_rect.x - true_scroll[0] - (width_window) / 2) / 20
        true_scroll[1] += (player_rect.y - true_scroll[1] - (height_window / 2)) / 20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

    if sneak:
        true_scroll[1] = player_rect.y + 50

    if player_rect.x < 565:
        true_scroll[0] = 10

    if screenshake > 0:
        screenshake -= 1
    if screenshake:
        true_scroll[0] += random.randint(0, 2) - 1
        true_scroll[1] += random.randint(0, 2) - 1

    #GameMap
    tile_rects = []
    tile_rects_diamond = []
    drawGameMap()

    #Draw
    Zombie_1.draw(window)
    if Zombie_1.visible == False:
        for i in range(1):
            z += 1
            if z == 1:
                diamonds.append(pygame.Rect(Zombie_1.x + 35, Zombie_1.y + 50, 16, 16))
                diamonds.append(pygame.Rect(Zombie_1.x - 35, Zombie_1.y + 50, 16, 16))
                diamonds.append(pygame.Rect(Zombie_1.x, Zombie_1.y + 50, 16, 16))
            else:
                pass

    Zombie_2.draw(window)
    # print("Start", {Zombie.atStart}, "Slutt" ,{Zombie.atEnd})

    # print(Zombie_1.health)

    player_hitbox = pygame.Rect((player_rect.x - scroll[0]) - 4, player_rect.y - scroll[1], 45, 85)
    print(player_rect.x, player_rect.y)
    #pygame.draw.rect(window, (255, 0, 0), player_hitbox, 2)

    #Diamonds - Score
    for d in diamonds:
        window.blit(diamond, (d[0] - scroll[0], d[1] - scroll[1]))

    #Sign - Tutorial
    for s in signs:
        window.blit(sign, (s[0] - scroll[0], s[1] - scroll[1]))

    #Mouse
    mouse = pygame.mouse.get_pos()

    #Player Movement
    player_movement = [0, 0]
    if right_walk:
        player_movement[0] += velocity_walk
    if left_walk:
        player_movement[0] -= velocity_walk
    if right_run:
        player_movement[0] += velocity_run
    if left_run:
        player_movement[0] -= velocity_run

    #Player Attacks
    #Punch
    if right_punch == True:
        button_press_time_r += 1
        screenshake = 5
        if button_press_time_r > 35:
            left_run = left_walk = right_walk = right_run = False
            impact_full_r = True
            punchCount_2_r = 0

        elif button_press_time_r > 20:
            left_run = left_walk = right_walk = right_run = False
            impact_mid_r = True
            punchCount_2_r = 0

    elif right_punch == False:
        button_press_time_r = 0
        punchCount_r = 0

    if impact_mid_r and right_punch == False:
        HitZombie(Zombie_1, 0.5)
        right_punch_2 = True
        player_movement[0] += player_x_momentum
        player_x_momentum += 2
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 20:
            player_x_momentum = 0
            impact_mid_r = False

    if impact_full_r and right_punch == False:
        HitZombie(Zombie_1, 1)
        right_punch_2 = True
        player_movement[0] += player_x_momentum
        player_x_momentum += 10
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 40:
            player_x_momentum = 0
            impact_full_r = False

    if left_punch == True:
        button_press_time_l += 1
        screenshake = 5
        if button_press_time_l > 35:
            left_run = left_walk = right_walk = right_run = False
            impact_full_l = True
            punchCount_2_l = 0

        elif button_press_time_l > 20:
            left_run = left_walk = right_walk = right_run = False
            impact_mid_l = True
            punchCount_2_l = 0

    elif left_punch == False:
        button_press_time_l = 0
        punchCount_l = 0

    if impact_mid_l and left_punch == False:
        HitZombie(Zombie_1, 0.5)
        left_punch_2 = True
        player_movement[0] -= player_x_momentum
        player_x_momentum += 2
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 20:
            player_x_momentum = 0
            impact_mid_l = False

    if impact_full_l and left_punch == False:
        HitZombie(Zombie_1, 1)
        left_punch_2 = True
        player_movement[0] -= player_x_momentum
        player_x_momentum += 10
        left_run = left_walk = right_walk = right_run = False
        if player_x_momentum > 40:
            player_x_momentum = 0
            impact_full_l = False

    if left_run == True or left_walk == True or right_walk == True or right_run == True:
        right_punch_2 = left_punch_2 = False

    #Arrow
    if left_run == True or left_walk == True or right_walk == True or right_run == True:
        right_arrow = left_arrow = False
        arrowCount_r = 0


    player_movement[1] += player_y_momentum
    if airtime:
        player_y_momentum += 0.9

    if player_y_momentum > 3:
        player_y_momentum += 0.1


    #Collisions Player
    player_rect, player_collisions = move(player_rect, player_movement, tile_rects)


    if player_collisions["bottom"] == True:
        player_y_momentum = 0
        air_timer = 0
    elif player_collisions["top"] == True:
        player_y_momentum += 2
        air_timer += 1
    else:
        air_timer += 1

    #Diamonds Collision

    for d in diamonds:
        if d.colliderect(player_rect):
            diamonds.remove(d)
            Score += 1
            if player_health < 3:
                player_health += 1
            elif player_health >= 3:
                pass

    #Zombie Collision
    if player_hitbox.colliderect(Zombie_1.hitbox) and player_x_momentum < 10 and Zombie_1.visible and not Zombie_1.tookDamage:
        player_health -= 0.02

    #Signs Collision
    for s in signs:
        if signs[0].colliderect(player_rect):
            showTut1 = True
        elif signs[1].colliderect(player_rect):
            showTut2 = True
        elif signs[2].colliderect(player_rect):
            showTut3 = True
        elif signs[3].colliderect(player_rect):
            showTut4 = True
        else:
            showTut1 = False
            showTut2 = False
            showTut3 = False
            showTut4 = False


    #Sprite Animation Main Player
    if walkCount + 1 >= 25:
        walkCount = 0
    if runCount + 1 >= 25:
        runCount = 0
    if standCount + 1 >= 25:
        standCount = 0
    if punchCount_r + 1 >= 48:
        punchCount_r = 48
    if punchCount_2_r + 1 >= 16:
        punchCount_2_r = 16
    if punchCount_l + 1 >= 48:
        punchCount_l = 48
    if punchCount_2_l + 1 >= 16:
        punchCount_2_l = 16
    if arrowCount_r + 1 > 40:
        arrowCount_r = 0

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
        window.blit(LoadPunchRight[punchCount_r//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount_r += 1
    elif left_punch:
        window.blit(LoadPunchLeft[punchCount_l//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount_l += 1
    elif right_punch_2:
        window.blit(punchRight[punchCount_2_r//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount_2_r += 1
    elif left_punch_2:
        window.blit(punchLeft[punchCount_2_l//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        punchCount_2_l += 1
    elif right_arrow:
        window.blit(arrowRight[arrowCount_r//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        arrowCount_r += 1
    elif Idle_stand:
        window.blit(Idle[standCount//1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        standCount += 1

    #General Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((width_window, height_window))

    #Pygame Keys/buttons
    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    if keys[pygame.K_SPACE]:
        airtime = True
        if air_timer < 6:
            player_y_momentum = -7

    if keys[pygame.K_e] and showTut1:
        showTut1Image = True

    if keys[pygame.K_e] and showTut2:
        showTut2Image = True

    if keys[pygame.K_e] and showTut3:
        showTut3Image = True

    if keys[pygame.K_e] and showTut4:
        showTut4Image = True

    if mouse_buttons[0] and moving_right == True:
        right_punch = True
        left_run = left_walk = right_walk = right_run = left_punch = sneak = False

    elif mouse_buttons[0] and moving_left == True:
        left_punch = True
        left_run = left_walk = right_walk = right_run = right_punch = sneak = False

    elif mouse_buttons[2] and moving_right == True:
        right_arrow = True
        left_run = left_walk = right_walk = right_run = left_arrow = sneak = False

    elif mouse_buttons[2] and moving_left == True:
        left_arrow = True
        left_run = left_walk = right_walk = right_run = right_arrow = sneak = False

    elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        left_run = moving_left = True
        right_run = left_walk = right_walk = right_punch = moving_right = sneak = False

    elif keys[pygame.K_a]:
        left_walk = moving_left = True
        right_walk = left_run = right_run = right_punch = moving_right = sneak = False

    elif keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
        right_run = moving_right = True
        left_run = left_walk = right_walk = right_punch = moving_left = sneak = False

    elif keys[pygame.K_d]:
        right_walk = moving_right = True
        left_run = right_run = left_walk = right_punch = moving_left = sneak = False
    elif keys[pygame.K_s]:
        sneak = True
        left_run = right_run = left_walk = right_punch = moving_left = moving_right = showTut1Image = showTut2Image = showTut3Image = False
    else:
        Idle_stand = True
        right_walk = left_walk = right_run = left_run = right_punch = left_punch = sneak = follow_player = False
        walkCount = runCount = 0

    #Misc/GUI
    window.blit(txt_background, (4, 4))
    window.blit(txt_background, (670, 4))


    #Player Health
    window.blit(HeartB, (180, 440))
    window.blit(HeartB, (220, 440))
    window.blit(HeartB, (260, 440))

    if player_health >= 3:
        window.blit(HeartR, (260, 440))
    if player_health >= 2:
        window.blit(HeartR, (220, 440))
    if player_health >= 1:
        window.blit(HeartR, (180, 440))


    #Signs
    if showTut1:
        window.blit(E_button, (500 - scroll[0], 405 - scroll[1]))
    if showTut2:
        window.blit(E_button, (180 - scroll[0], 405 - scroll[1]))
    if showTut3:
        window.blit(E_button, (220 - scroll[0], 645 - scroll[1]))
    if showTut4:
        window.blit(E_button, (1165 - scroll[0], 565 - scroll[1]))


    if showTut1 and showTut1Image:
        window.blit(tutImage1, (220 - scroll[0], 230 - scroll[1]))
    elif showTut2 and showTut2Image:
        window.blit(tutImage2, (220 - scroll[0], 230 - scroll[1]))
    elif showTut3 and showTut3Image:
        window.blit(tutImage3, (220 - scroll[0], 430 - scroll[1]))
    elif showTut4 and showTut4Image:
        window.blit(tutImage4, (1000 - scroll[0], 290 - scroll[1]))
    else:
        showTut3Image = False
        showTut2Image = False
        showTut1Image = False
        showTut4Image = False


    if right_arrow or left_arrow:
        x = 1
        window.blit(Itembar[x], (320, 420))
    else:
        x = 0
        window.blit(Itembar[x], (320, 420))

    Load_txt2 = font2.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (255, 255, 255))

    if button_press_time_r < 20:
        Load_txt = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (0,0,0))
    elif button_press_time_r > 20 and button_press_time_r < 35:
        Load_txt = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (125, 0, 0))
    elif button_press_time_r > 35:
        Load_txt = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (255, 0, 0))
    if button_press_time_l < 20:
        Load_txt_2 = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (0,0,0))
    elif button_press_time_l > 20 and button_press_time_l < 35:
        Load_txt_2 = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (125, 0, 0))
    elif button_press_time_l > 35:
        Load_txt_2 = font.render("LoadPunch: " + str(button_press_time_l or button_press_time_r), 1, (255, 0, 0))

    Score_txt = font.render("Score: " + str(Score), 1, (255, 255, 255))
    Arrow_txt = font_arrow.render(str(Arrows), 1, (255, 255, 255))
    Time_txt = font.render("Time: " + str(current_time), 1, (255,255,255))
    window.blit(Arrow_txt, (481, 456))
    window.blit(Score_txt, (680, 10))
    window.blit(Load_txt2, (519, 440))
    window.blit(Load_txt, (520, 440))
    window.blit(Time_txt, (10, 10))
    if moving_right:
        window.blit(Load_txt, (520, 440))
        moving_left = False
    if moving_left:
        window.blit(Load_txt_2, (520, 440))
        moving_right = False
    pygame.display.update()


pygame.quit()