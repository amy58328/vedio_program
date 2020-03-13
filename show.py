from setting import * 

def time_show(minute,second):
	minute = str(minute)
	second = str(second)

	message_display(minute,50,red,(weight/2 - 45),(height - player_size + 50))
	message_display(":",50,red,(weight/2 - 15),(height - player_size + 50))
	message_display(second,50,red,(weight/2 + 15),(height - player_size + 50))



def show_player(p1,p2):
	screen.fill(black)

	screen.blit(back,(0,0))
	screen.blit(p1_red,(p1.x,p1.y))
	screen.blit(p2_red,(p2.x,p2.y))
	
	#pygame.draw.rect(screen,(218,112,214),[bx_change -5,0,5,600],0)
	#pygame.draw.rect(screen,(218,112,214),[weight - bx_change ,0,5,600],0)

	# p1 #########
	pygame.draw.rect(screen, (200,200,200), [0,550,1600,130],0)
	pygame.draw.rect(screen,red,[25,565,75,75],0)  #25 620 75 75
	pygame.draw.rect(screen,yellow,[125,565,75,75],0) #125 620 75 75
	pygame.draw.rect(screen,blue,[225,565,75,75],0) #225 620 75 75

	n = int(p1.clock_ / 100)

	for i in range(0,n):
		screen.blit(bullet_show,(330+ i*30,565))

	if p1.seat == 1:
		pygame.draw.rect(screen,(255,255,255),[25,565,75,75],20)
	elif p1.seat == 2:
		pygame.draw.rect(screen,(255,255,255),[125,565,75,75],20)
	elif p1.seat == 3:
		pygame.draw.rect(screen,(255,255,255),[225,565,75,75],20)

	for i in range(0,p1.live):
			screen.blit(love,(50+i*50,535))

	# p2 ################
	pygame.draw.rect(screen,red,[900,565,75,75],0)
	pygame.draw.rect(screen,yellow,[1000,565,75,75],0)
	pygame.draw.rect(screen,blue,[1100,565,75,75],0)	

	if p2.seat == 3:
		pygame.draw.rect(screen,(255,255,255),[1100,565,75,75],20)
	elif p2.seat == 2:
		pygame.draw.rect(screen,(255,255,255),[1000,565,75,75],20)
	elif p2.seat == 1:
		pygame.draw.rect(screen,(255,255,255),[900,565,75,75],20)

	n = int(p2.clock_ / 100)

	for i in range(0,n):
		screen.blit(bullet_show,(850 - i*30,565))

	for i in range(0,p2.live):
		screen.blit(love,(1150-i*50,535))

def show_zombie(zombie_list,coco,zombie_reduce):
	if coco % 900  == 0 and coco !=0 :
		zombie_reduce += 2
	for zombie in zombie_list:
		if zombie.life == 1:
			if zombie.who == 1:
				if zombie.color == red:
					screen.blit(red_b1,(zombie.x, zombie.y))
				elif zombie.color == yellow:
					screen.blit(yellow_b1,(zombie.x, zombie.y))

				elif zombie.color == blue:
					screen.blit(blue_b1,(zombie.x, zombie.y))

				zombie.x += zombie.speed + zombie_reduce

			elif zombie.who == 2 :
				if zombie.color == red:
					screen.blit(red_b2,(zombie.x, zombie.y))

				elif zombie.color == yellow:
					screen.blit(yellow_b2,(zombie.x, zombie.y))

				elif zombie.color == blue:
					screen.blit(blue_b2,(zombie.x, zombie.y))	

				zombie.x -= zombie.speed + zombie_reduce
	return zombie_reduce

def show_bullet(bullet_list):
	for bullet in bullet_list:
		if bullet.life == 1:
			if bullet.who == 1:
				if bullet.color == red:
					screen.blit(red_bullet1,(bullet.x, bullet.y))
				elif bullet.color == yellow:
					screen.blit(yellow_bullet1,(bullet.x, bullet.y))

				elif bullet.color == blue:
					screen.blit(blue_bullet1,(bullet.x, bullet.y))
				bullet.x += 4

			elif bullet.who == 2 :
				if bullet.color == red:
					screen.blit(red_bullet2,(bullet.x, bullet.y))

				elif bullet.color == yellow:
					screen.blit(yellow_bullet2,(bullet.x, bullet.y))

				elif bullet.color == blue:
					screen.blit(blue_bullet2,(bullet.x, bullet.y))	

				bullet.x -= 4


