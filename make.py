import pygame
from setting import *
import time
import random
import datetime
from vedio_program import *

random.seed(datetime.datetime.now())
 
def button(msg,x,y,w,h,ic,ac,sizer):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen, ac,(x,y,w,h))

		if click[0] == 1 and action != None:
			# action()
			return 1         
	else:
		pygame.draw.rect(screen, ic,(x,y,w,h))

	message_display(msg,sizer,red,(x+w/2),(y+h/2))
	return 0 


def color_set(color,seat,where):
	if where == 0:
		if color == red:
			color = yellow
			seat = 2
		elif color == yellow:
			color = blue
			seat = 3
		elif color == blue:
			color = red
			seat = 1
	elif where == 1:
		if color == red:
			color = blue
			seat = 3
		elif color == blue:
			color = yellow
			seat = 2
		elif color == yellow:
			color = red
			seat = 1
	return color,seat

def make_zombie(who):
	zombie = Zombie()
	i = random.randrange(0,4)
	cc = random.randrange(0,3)
	if who == 1:
		zombie.x = 0
		zombie.y = i*zy_change
		zombie.who = 1
		if cc == 0:
			zombie.color = red
			zombie.speed = 2 # 3
		elif cc == 1:
			zombie.color = yellow
			zombie.speed = 2.5 # 3.5
		elif cc == 2:
			zombie.color = blue
			zombie.speed = 3.5 # 5
		zombie.life = 1
	
	elif who  == 2:
		zombie.x = weight - 60 # 1540 
		i = random.randrange(0,4)
		zombie.y = i * zy_change
		zombie.who = 2
		if cc == 0:
			zombie.color = red
			zombie.speed = 2
		elif cc == 1:
			zombie.color = yellow
			zombie.speed = 2.5
		elif cc == 2:
			zombie.color = blue
			zombie.speed = 3.5
		zombie.life = 1

	return zombie

def make_bullet(y,color,who):
	bullet = Bullet()

	if who == 1:
		bullet.x = 0
		bullet.y = y
		bullet.who = who
		bullet.color = color
		bullet.life = 1
	
	elif who == 2:
		bullet.x = weight - bx_change # 1540 
		bullet.y = y
		bullet.who = who
		bullet.color = color
		bullet.life = 1

	return bullet


def crash(zombie_list,bullet_list,p1,p2):
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


	for bullet in bullet_list:
		if bullet.life == 1 and (p1.live !=0  and p2.live != 0) :
			if bullet.who == 1 and bullet.color == p2.live_color and bullet.x > weight - bx_change-bx_change and bullet.y == p2.y:
				time.sleep(0.1)
				p2.live -= 1
				bullet.life = 0
			if bullet.who == 2 and bullet.color == p1.live_color and bullet.x < bx_change and bullet.y == p1.y:
				time.sleep(0.1)
				p1.live -= 1
				bullet.life = 0

	for zombie in zombie_list:
		if zombie.life == 1 and (p1.live != 0 and  p2.live != 0 ):
			if zombie.who == 1 and zombie.x > weight - bx_change - zx_change :
				time.sleep(0.1)
				p2.live -= 1
				zombie.life = 0
			elif zombie.who == 2 and zombie.x <bx_change :
				time.sleep(0.1)
				p1.live -= 1
				zombie.life = 0

	return zombie_list,bullet_list,p1,p2
