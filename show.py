from setting import * 


def show_player(p1_x,p1_y,p2_x,p2_y,p1_color,p2_color):
	screen.fill(black)


	pygame.draw.rect(screen, p1_color, [p1_x,p1_y,50,zy_change],0)
	pygame.draw.rect(screen, p2_color, [p2_x,p2_y,50,zy_change],0)

def show_zombie(zombie_list):
	for zombie in zombie_list:
		if zombie.life == 1:
			if zombie.who == 1:
				if zombie.color == (255,0,0):
					screen.blit(red_b1,(zombie.x, zombie.y))
				elif zombie.color == (255,255,0):
					screen.blit(yellow_b1,(zombie.x, zombie.y))

				elif zombie.color == (0,0,255):
					screen.blit(blue_b1,(zombie.x, zombie.y))
				zombie.x += 2

			elif zombie.who == 2 :
				if zombie.color == (255,0,0):
					screen.blit(red_b2,(zombie.x, zombie.y))

				elif zombie.color == (255,255,0):
					screen.blit(yellow_b2,(zombie.x, zombie.y))

				elif zombie.color == (0,0,255):
					screen.blit(blue_b2,(zombie.x, zombie.y))	

				zombie.x -= 2

def show_bullet(bullet_list):
	for bullet in bullet_list:
		if bullet.life == 1:
			if bullet.who == 1:
				if bullet.color == (255,0,0):
					screen.blit(red_bullet1,(bullet.x, bullet.y))
				elif bullet.color == (255,255,0):
					screen.blit(yellow_bullet1,(bullet.x, bullet.y))

				elif bullet.color == (0,0,255):
					screen.blit(blue_bullet1,(bullet.x, bullet.y))
				bullet.x += 2

			elif bullet.who == 2 :
				if bullet.color == (255,0,0):
					screen.blit(red_bullet2,(bullet.x, bullet.y))

				elif bullet.color == (255,255,0):
					screen.blit(yellow_bullet2,(bullet.x, bullet.y))

				elif bullet.color == (0,0,255):
					screen.blit(blue_bullet2,(bullet.x, bullet.y))	

				bullet.x -= 2