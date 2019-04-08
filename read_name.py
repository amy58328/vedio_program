import pygame
from setting import *
from make import *
import time
import random
import datetime
from vedio_program import *


def action():
	cc = False
	n=0
	while not cc :
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				c = True
		screen.fill(blue)
		message_display("reseting ... ",115,red,weight/2,height/2)
		n += 1
		if n >200 :
			cc = True
		pygame.display.update()
	

def enter_name(minute,second):
	enter = False
	screen.fill(black)
	sstring = []
	while not enter:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sstring.append("q")
				if event.key == pygame.K_a:
					sstring.append("a")
				if event.key == pygame.K_s:
					sstring.append("s")
				if event.key == pygame.K_d:
					sstring.append("d")
				if event.key == pygame.K_w:
					sstring.append("w")
				if event.key == pygame.K_e:
					sstring.append("e")
				if event.key == pygame.K_r:
					sstring.append("r")
				if event.key == pygame.K_t:
					sstring.append("t")
				if event.key == pygame.K_y:
					sstring.append("y")
				if event.key == pygame.K_u:
					sstring.append("u")
				if event.key == pygame.K_i:
					sstring.append("i")
				if event.key == pygame.K_o:
					sstring.append("o")	
				if event.key == pygame.K_p:
					sstring.append("p")	
				if event.key == pygame.K_f:
					sstring.append("f")	
				if event.key == pygame.K_g:
					sstring.append("g")	
				if event.key == pygame.K_h:
					sstring.append("h")	
				if event.key == pygame.K_j:
					sstring.append("j")	
				if event.key == pygame.K_k:
					sstring.append("k")	
				if event.key == pygame.K_l:
					sstring.append("l")	
				if event.key == pygame.K_z:
					sstring.append("z")	
				if event.key == pygame.K_x:
					sstring.append("x")	
				if event.key == pygame.K_c:
					sstring.append("c")	
				if event.key == pygame.K_v:
					sstring.append("v")	
				if event.key == pygame.K_b:
					sstring.append("b")	
				if event.key == pygame.K_n:
					sstring.append("n")	
				if event.key == pygame.K_m:
					sstring.append("m")	
				if event.key == pygame.K_SPACE:
					sstring.append(" ")		
				if event.key == pygame.K_BACKSPACE:
					if len(sstring) != 0:
						sstring.pop()
				if event.key == pygame.K_RETURN:
					enter = True

		output = ','.join(sstring)
		output = output.replace(',','')
		output_m = str(minute)
		output_s = str(second)

		screen.fill(black)

		message_display("you cost",50,red,(weight/2-250),(height/2-200))
		message_display(output_m,50,red,(weight/2-80),(height/2-200))
		message_display(":",50,red,(weight/2-25),(height/2-200))
		message_display(output_s,50,red,(weight/2+25),(height/2-200))
		message_display("to win",50,red,(weight/2+200),(height/2-200))
		
		message_display("enter your name",50,red,(weight/2),(height/2-100))
		message_display(output,50,red,(weight/2),(height/2))
	
		pygame.display.update()
		clock.tick(15) 

	file = open("text.txt","a")
	file.write(output+ "/" + output_m +"/" + output_s + "\n" )


def rank():
	file = open("text.txt","r")
	mes = file.readlines()

	name = []
	minute = []
	second = []

	for i in range(0,len(mes)):
		name.append(mes[i].split("/")[0])
		minute.append(mes[i].split("/")[1])
		second.append(mes[i].split("/")[2])

		
	for i in range(0,len(second)-1):
		for j in range(i+1,len(second)):
			if minute[i] == minute[j]:
				if second[i] > second[j]:
					name[i] ,name[j] = name[j] , name[i]
					minute[i] , minute[j] = minute[j] , minute[i]
					second[i] , second[j] = second[j] , second[i]
			if minute[i] > minute[j]:
				name[i] ,name[j] = name[j] , name[i]
				minute[i] , minute[j] = minute[j] , minute[i]
				second[i] , second[j] = second[j] , second[i]

	file = open("text.txt","w")

	for i in range(0,len(minute)):
		if i < 10:
			print(name[i] + " " +minute[i] +":" + second[i],end= "")
		file.write(name[i] + "/" +minute[i] +"/" + second[i])

		
	name.clear()
	minute.clear()
	second.clear()