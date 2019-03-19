import pygame
import time
import random

pygame.init()

height = 650
weight = 1000
bg = (0,0,0)

screen = pygame.display.set_mode((weight,height))
pygame.display.set_caption("vedio_program")
clock = pygame.time.Clock()

###setting#############################
background = pygame.image.load("background.jpg")
blue_b = pygame.image.load("blue_b.png")
yellow_b = pygame.image.load("yellow_b.png")
red_b = pygame.image.load("red_b.png")
zombie = []
###subroutine##########################


###main function#######################
def main():
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				crashed = True

		# screen.blit(background,(0,0))
		screen.blit(red_b,(50,50))
		screen.blit(blue_b,(150,150))
		screen.blit(yellow_b,(250,250))
		pygame.display.update()


main()
pygame.quit()
quit()