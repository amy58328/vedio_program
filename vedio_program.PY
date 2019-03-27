import pygame
import time
import random
from setting import *
from show import *
from make import *

pygame.init()

def main():
	global p1_x,p1_y,p2_y,p2_x,p1_color,p2_color
	crashed = False

	zombie_list = []
	bullet_list = []

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				crashed = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					p1_y += zy_change

				if event.key == pygame.K_w:
					p1_y -= zy_change

				if event.key == pygame.K_UP:
					p2_y -= zy_change

				if event.key == pygame.K_DOWN:
					p2_y += zy_change

				if event.key == pygame.K_d:
					p1_color = color_set(p1_color)

				if event.key == pygame.K_a:
					p1_color = color_set(p1_color)

				if event.key == pygame.K_RIGHT:
					p2_color = color_set(p2_color)

				if event.key == pygame.K_LEFT:
					p2_color = color_set(p2_color)

				if event.key == pygame.K_z:   #p1 zombie
					zombie = make_zombie(p1_y,p1_color,1)
					zombie_list.append(zombie)

				if event.key == pygame.K_n:   #p1 zombie
					zombie = make_zombie(p2_y,p2_color,2)
					zombie_list.append(zombie)

				if event.key == pygame.K_x:   #p1 bullet
					bullet = make_bullet(p1_y,p1_color,1)
					bullet_list.append(bullet)

				if event.key == pygame.K_m:   #p1 bullet
					bullet = make_bullet(p2_y,p2_color,2)
					bullet_list.append(bullet)

			# if event.type == pygame.KEYUP:

			if p1_y <= 0:
				p1_y = 0
			elif p1_y >= 3*zy_change:
				p1_y = 3*zy_change
			
			if p2_y <=0 :
				p2_y = 0
			elif p2_y >= 3*zy_change:
				p2_y = 3*zy_change

		show_player(p1_x,p1_y,p2_x,p2_y,p1_color,p2_color)
		zombie_list,bullet_list = crash(zombie_list,bullet_list)
		show_zombie(zombie_list)
		show_bullet(bullet_list)


		pygame.display.update()
		clock.tick(60)

	pygame.quit()
		


if __name__ == "__main__":
	main()

quit()