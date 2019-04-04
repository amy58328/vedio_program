import pygame
from setting import *
import time
import random
import datetime

random.seed(datetime.datetime.now())


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

def make_zombie():
	zombie = Zombie()
	who = random.randrange(1,100)
	i = random.randrange(0,4)
	cc = random.randrange(0,3)
	if who % 2 == 1:
		zombie.x = 0
		zombie.y = i*zy_change
		zombie.who = 1
		if cc == 0:
			zombie.color = red
		elif cc == 1:
			zombie.color = yellow
		elif cc == 2:
			zombie.color = blue
		zombie.life = 1
	
	elif who % 2  == 0:
		zombie.x = weight - 60 # 1540 
		i = random.randrange(0,4)
		zombie.y = i * zy_change
		zombie.who = 2
		if cc == 0:
			zombie.color = red
		elif cc == 1:
			zombie.color = yellow
		elif cc == 2:
			zombie.color = blue
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
		bullet.x = weight - 60 # 1540 
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

# def win(win) :
# 	screen.fill(black)
# 	if win == 1:
# 		message_display("player1 is win")
# 		button("reset",225,450,200,130,red,blue,action)
# 	elif win == 2:
# 		message_display("player2 is win")
# 		button("reset",225,450,200,130,red,blue,action)
