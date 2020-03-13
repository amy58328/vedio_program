import pygame
import time
import random
from setting import *
from show import *
from make import *
from read_name import * 

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

		into = button("Play",500,250,175,85,green,bright_green,50)
		if into == 1:
			main()
		into = button("Quit",500,550,175,85,pink,bright_pink,50)
		if into == 1:
			quitgame()		
		into = button("Instructions",500,350,175,85,orange,bright_yellow,30)		
		if into == 1:
			ins()
		into = button("Rank",500,450,175,85,dark_blue,blue,50)		
		if into == 1:
			show_board()

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
		into = button("Back",55,550,200,85,pink,bright_pink,50)
		if into == 1:
			game_intro()
		into = button("Start",900,550,200,85,green,bright_green,50)
		if into == 1:
			main()
		pygame.display.update()
		clock.tick(15) 

def quitgame():
	pygame.quit()
	quit()   
	

def win(mm,ss,win) :
	if win == 1:
		screen.blit(p1win,(0,0))
		into = button("Again",100,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			main()
		into = button("Enter",700,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			enter_name(mm,ss)
			rank()
		into = button("Quite",1000,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			quitgame()
		into = button("Reset",400,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			action()
			game_intro()

	elif win == 2:
		screen.blit(p2win,(0,0))
		into = button("Again",100,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			main()
		into = button("Enter",700,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			enter_name(mm,ss)
			rank()
		into = button("Quite",1000,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			quitgame()
		into = button("Reset",400,550,100,85,(153,204,204),(204,255,204),50)
		if into == 1:
			action()
			game_intro()


def main():
	global p1,p2,clock_z,zombie_list,bullet_list,second,minute

	crashed = False
	
	coco = 0
	clock_z = 0 
	ww = 0 
	p1_reduce = 0
	p2_reduce = 0
	zombie_reduce = 0
	p1,p2 = reset()
	zombie_list.clear()
	bullet_list.clear()
	while not crashed:
		coco += 1

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

				if event.key == pygame.K_v:   #p1 bullet
					p1_reduce = 0
					if coco % 900 == 0 and coco != 0 :
						p1_reduce += 10
					if p1.clock_ >= 80 - p1_reduce:
						bullet = make_bullet(p1.y,p1.color,1)
						bullet_list.append(bullet)
						p1.clock_ -= 80 + p1_reduce

				if event.key == pygame.K_m:   #p2 bullet
					p2_reduce = 0
					if coco % 900 == 0 and coco != 0:
						p2_reduce += 10
					if p2.clock_ >= 80 - p2_reduce:
						bullet = make_bullet(p2.y,p2.color,2)
						bullet_list.append(bullet)
						p2.clock_ -= 80 + p2_reduce

			if p1.y <= 0:
				p1.y = 0
			elif p1.y >= 3*zy_change:
				p1.y = 3*zy_change
			
			if p2.y <=0 :
				p2.y = 0
			elif p2.y >= 3*zy_change:
				p2.y = 3*zy_change

		if clock_z == 75 :
			zombie = make_zombie(1)
			zombie_list.append(zombie)
			zombie = make_zombie(2)
			zombie_list.append(zombie)
			clock_z = 0
		else: 
			clock_z += 1

		p1.clock_ += 1
		p2.clock_ += 1
		if p1.clock_ >= 450:
			p1.clock_ = 450
		if p2.clock_ >= 500:
			p2.clock_ = 500

		

		second = int(coco/30)
		minute = int(second/60)
		if second >=  60:
			second = second % 60
		
		show_player(p1,p2)
		zombie_list,bullet_list,p1,p2 = crash(zombie_list,bullet_list,p1,p2)
		zombie_reduce = show_zombie(zombie_list,coco,zombie_reduce)
		show_bullet(bullet_list)
		time_show(minute,second)

		if p1.live == 0 :	
			if ww == 0:
				mm = minute
				ss = second
				ww = 1
			win(mm,ss,2)
		elif p2.live == 0 :	
			if ww == 0:
				mm = minute
				ss = second
				ww = 1
			win(mm,ss,1)



		pygame.display.update()
		clock.tick(60)

	pygame.quit()
	
def show_board():
	heofs = height
	intro = True
	file = open("text.txt","r")
	mes = file.readlines()
	#print(mes)
	name = []
	minute = []
	second = []
	for i in range(0,len(mes)):
		name.append(mes[i].split("/"))
		#minute.append(mes[i].split("/"))
		#second.append(mes[i].split("/"))
	message_display(name[0][0].encode('UTF-8'),55,black,(weight/2-250),(heofs/2-100))
	while intro:
		heofs = height
		for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit() 

		screen.blit(startBackground,(0,0))

		#print(name[0][0])
		if (len(mes)>=10):
			for i in range(0,10):
				#print(name[i][0])
				line=name[i][2].strip('\n')
				message_display(name[i][0].encode('UTF-8'),30,black,200,(heofs/2-100))
				message_display(name[i][1].encode('UTF-8'),30,black,600,(heofs/2-100))
				message_display(line.encode('UTF-8'),30,black,1000,(heofs/2-100))
				heofs+=110

		if (len(mes)<10):
			for i in range(0,len(mes)):
				#print(name[i][0])
				line=name[i][2].strip('\n')
				message_display(name[i][0].encode('UTF-8'),30,black,400,(heofs/2-100))
				message_display(name[i][1].encode('UTF-8'),30,black,800,(heofs/2-100))
				message_display(line.encode('UTF-8'),30,black,1200,(heofs/2-100))
				heofs+=110
			#flg=False


		into = button("Back",30,100,200,85,pink,bright_pink,50)
		if into == 1:
			game_intro()

		pygame.display.update()
		clock.tick(15)
		

#game_loop()
if __name__ == "__main__":
	game_intro()
	pygame.quit()
	quit()