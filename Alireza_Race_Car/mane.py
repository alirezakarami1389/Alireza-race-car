import pygame
import time
import random

pygame.init()
dsasa = pygame.mixer.Sound("music.OGG")

def gameLoop():
    # ! = !
    display_wide = 800

    display_hight = 600

    white = (255,255,255)
    black = (0,0,0)
    red = (125,125,125)
    blue = (0,0,255)
    green = (0,255,0)

    x = (display_wide * 0.41)
    y = (display_hight * 0.8)

    f = (display_wide * 0.3)
    g = (0)
    
    w = 0
    e = 0


    
    stuff_startx = random.randrange(0,display_wide - 100)
    stuff_starty = -600
    stuff_speed = 5
    stuff_wide = 100
    stuff_hight = 100

    y_change = 0
    x_change = 0
    car_wide = 68


    scoree = 0
    #display

    GameDisplay = pygame.display.set_mode((display_wide, display_hight))

    #caption
    pygame.display.set_caption('Alireza Race Car')
    # speed * game
    Clock = pygame.time.Clock()
    #load_image
    gadeimg = pygame.image.load('tt.png')
    Carimg = pygame.image.load('ali.png')
    AryaKarami = pygame.image.load("AKAKAK.png")
    asqwd = pygame.image.load("ila.png")
    # my car
    def car(x ,y):
        GameDisplay.blit(Carimg,(x, y)) 
    # my gade      
    def gade(f ,g):
        GameDisplay.blit(gadeimg,(f ,g))

 
    #defs#
    #crashed
    def crashed():
        time.sleep(2)
        gameLoop()
    def stuff_doged(cuont):
        font = pygame.font.SysFont(None, 25)
        text = font.render("score : " +str(cuont)  ,  True , green)
        GameDisplay.blit(text,(0,0))

    gameExit = False
    # while not gameExit _ * game

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            #event type
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
            #key down(S)
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        #go to left and right
        x += x_change
        y += y_change
        # if(s)    
        if x > display_wide - car_wide or x < 0:
            crashed()
        if y > display_hight - 106 or y < 0:
            crashed()

        if stuff_starty > display_hight:
            stuff_starty =  0 - stuff_hight
            stuff_startx = random.randrange(0 ,display_wide - 100)
            scoree += 1

            if (scoree % 5 == 0):
                stuff_speed += 2
                asqwd = AryaKarami
        
        if y <stuff_starty + stuff_hight:
            if x > stuff_startx and x < stuff_startx + stuff_wide or x + car_wide >stuff_startx and x + car_wide < stuff_startx + stuff_wide:
                crashed()


        #color and car display
        GameDisplay.fill(red)
        pygame.mixer.Sound.play(dsasa)
        gade(f, g)
        GameDisplay.blit(asqwd,(stuff_startx ,stuff_starty))
        stuff_starty += stuff_speed
        stuff_doged(scoree)
        car(x ,y)

        #speed * ALL GAME2  
        pygame.display.update()

        Clock.tick(60)
#finish
gameLoop()
pygame.quit()
quit()
