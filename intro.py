import pygame
import time
import random
 
pygame.init()

#####設定####### 
 
black = (0,0,0)
white = (255,255,255)

green = (0,200,0)
orange = (255,176,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_yellow = (255,226,0)

############### 


clock = pygame.time.Clock()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(startBackground,(0,0))

        ###按鈕###

        #button("Play",725,300,200,85,green,bright_green,main)
        button("Quit",725,500,200,85,red,bright_red,quitgame)
        button("Instructions",725,400,200,85,orange,bright_yellow,ins)

        ##########

        pygame.display.update()
        clock.tick(15)    
        
def ins():
    intro = True

    while intro: 
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(instructionBackground,(0,0))
        button("Back",55,830,200,85,red,bright_red,game_intro)
        pygame.display.update()
        clock.tick(15) 

def quitgame():
    pygame.quit()
    quit()   
    

    
#遊戲主程式 def main():


game_intro()
#game_loop()
pygame.quit()
quit()