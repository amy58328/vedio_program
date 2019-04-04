import pygame
import time
import random
from setting import *
from show import *
from make import *

pygame.init()

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
		button("Quit",weight/2-75,height-430,200,85,red,bright_red,quitgame)
		button("Instructions",weight/2-75,height-330,200,85,orange,bright_yellow,ins)

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
		button("Back",55,height - 100,200,85,red,bright_red,game_intro)
		button("start game",weight - 155,height - 100,200,85,red,bright_red,main)
		pygame.display.update()
		clock.tick(15) 

def quitgame():
	pygame.quit()
	quit()   
	

def win(win) :
	if win == 1:
		screen.blit(p1win,(0,0))
		button("reset",420,600,200,130,(153,204,204),(204,255,204),action)
	elif win == 2:
		screen.blit(p2win,(0,0))
		button("reset",420,600,200,130,(153,204,204),(204,255,204),action)
def action():
	cc = False
	n=0
	while not cc :
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				c = True
		screen.fill(blue)
		message_display("reseting ... ")
		n += 1
		if n >200 :
			cc = True
		pygame.display.update()
	main()

def main():
	global p1,p2,clock_z,zombie_list,bullet_list

	crashed = False
	
	coco = 0
	clock_z = 0 
	p1,p2 = reset()
	zombie_list.clear()
	bullet_list.clear()
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				crashed = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					p1.y += zy_change

				if event.key == pygame.K_w:
					p1.y -= zy_change

				if event.key == pygame.K_UP:
					p2.y -= zy_change

				if event.key == pygame.K_DOWN:
					p2.y += zy_change

				if event.key == pygame.K_d:
					p1.color ,p1.seat= color_set(p1.color,p1.seat,0)

				if event.key == pygame.K_a:
					p1.color,p1.seat = color_set(p1.color,p1.seat,1)

				if event.key == pygame.K_RIGHT:
					p2.color,p2.seat = color_set(p2.color,p2.seat,0)

				if event.key == pygame.K_LEFT:
					p2.color,p2.seat = color_set(p2.color,p2.seat,1)

				if event.key == pygame.K_x:   #p1 bullet
					if p1.clock_ >= 100 :
						bullet = make_bullet(p1.y,p1.color,1)
						bullet_list.append(bullet)
						p1.clock_ -= 100

				if event.key == pygame.K_m:   #p2 bullet
					if p2.clock_ >= 100 :
						bullet = make_bullet(p2.y,p2.color,2)
						bullet_list.append(bullet)
						p2.clock_ -= 100

			if p1.y <= 0:
				p1.y = 0
			elif p1.y >= 3*zy_change:
				p1.y = 3*zy_change
			
			if p2.y <=0 :
				p2.y = 0
			elif p2.y >= 3*zy_change:
				p2.y = 3*zy_change

		if clock_z == 45 :
			zombie = make_zombie()
			zombie_list.append(zombie)
			clock_z = 0
		else: 
			clock_z += 1

		p1.clock_ += 1
		p2.clock_ += 1
		if p1.clock_ >= 500:
			p1.clock_ = 500
		if p2.clock_ >= 500:
			p2.clock_ = 500

		coco += 1

		second = int(coco/30)
		minute = int(second/60)
		if second >=  60:
			second = second % 60
		
		show_player(p1,p2,)
		zombie_list,bullet_list,p1,p2 = crash(zombie_list,bullet_list,p1,p2)
		show_zombie(zombie_list)
		show_bullet(bullet_list)
		time_show(minute,second)

		if p1.live == 0 :
			win(2)
		elif p2.live == 0:
			win(1)



		pygame.display.update()
		clock.tick(60)

	pygame.quit()
		

game_intro()
#game_loop()
# if __name__ == "__main__":
#   main()
pygame.quit()
quit()