

import pygame

height = 700 	#改850
weight = 1000 	#改1600
bg = (0,0,0)

screen = pygame.display.set_mode((weight,height))
pygame.display.set_caption("vedio_program")
clock = pygame.time.Clock()


# background = pygame.image.load("background.jpg")
blue_b = pygame.image.load("blue_b.png")
yellow_b = pygame.image.load("yellow_b.png")
red_b = pygame.image.load("red_b.png")
blue_bullet = pygame.image.load("blue_bullet.png")
yellow_bullet = pygame.image.load("yellow_bullet.png")
red_bullet = pygame.image.load("red_bullet.png")
zombie = []

blue_b = pygame.transform.scale(blue_b,(500,500)) #改變大小


class zombie :
	def __init__(self):
		self.x = 0
		self.y = 0
		self.r = 0
		self.g = 0
		self.b = 0
		self.live = 0

class bullet:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.r = 0
		self.g = 0
		self.b = 0
		self.live = 0