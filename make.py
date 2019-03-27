import pygame
from setting import *

def color_set(color):
	if color == (255,0,0):
		color = (255,255,0)
	elif color == (255,255,0):
		color = (0,0,255)
	elif color == (0,0,255):
		color = (255,0,0)
	return color

def make_zombie(y,color,who):
	zombie = Zombie()

	if who == 1:
		zombie.x = 0
		zombie.y = y
		zombie.who = who
		zombie.color = color
		# print(zombie.color)
		zombie.life = 1
	
	elif who == 2:
		zombie.x = 880 # 1540 
		zombie.y = y
		zombie.who = who
		zombie.color = color
		# print(zombie.color)
		zombie.life = 1

	return zombie


def make_bullet(y,color,who):
	bullet = Bullet()

	if who == 1:
		bullet.x = 0
		bullet.y = y
		bullet.who = who
		bullet.color = color
		# print(bullet.color)
		bullet.life = 1
	
	elif who == 2:
		bullet.x = 880 # 1540 
		bullet.y = y
		bullet.who = who
		bullet.color = color
		# print(bullet.color)
		bullet.life = 1

	return bullet


def crash(zombie_list,bullet_list):
	for zombie in zombie_list:
		for bullet in bullet_list:
			if zombie.life == 1 and bullet.life == 1:
				if zombie.who == 1 and bullet.who == 2:
					if zombie.y == bullet.y: 
						if zombie.color == bullet.color:
							if zombie.x > bullet.x :
								zombie.life = 0
								bullet.life = 0 


				elif zombie.who == 2 and bullet.who == 1:
					if zombie.y == bullet.y: 
						if zombie.color == bullet.color:
							if zombie.x < bullet.x :
								zombie.life = 0
								bullet.life = 0 

				if zombie.life == 0 :
					zombie_list.remove(zombie)
				if bullet.life == 0 :
					bullet_list.remove(bullet)