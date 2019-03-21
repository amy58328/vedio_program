import pygame
import time
import random
from setting import *

pygame.init()

def main():
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				crashed = True
				
		screen.blit(red_b,(50,50))
		screen.blit(blue_b,(150,150))
		screen.blit(yellow_b,(250,250))
		pygame.display.update()


if __name__ == "__main__":
	main()

pygame.quit()
quit()