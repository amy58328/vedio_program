import pygame

height = 700 	#改850
weight = 1000 	#改1600
bg = (0,0,0)
black = (0,0,0)

zy_change = 170 #改240
zx_change = 120 #160
bx_change = 230 #250
by_change = 175 # 200

screen = pygame.display.set_mode((weight,height))
pygame.display.set_caption("vedio_program")
clock = pygame.time.Clock()


# background = pygame.image.load("background.jpg")
blue_b1 = pygame.image.load("blue_b1.png")
yellow_b1 = pygame.image.load("yellow_b1.png")
red_b1 = pygame.image.load("red_b1.png")

blue_bullet1 = pygame.image.load("blue_bullet1.png")
yellow_bullet1 = pygame.image.load("yellow_bullet1.png")
red_bullet1 = pygame.image.load("red_bullet1.png")

blue_b2 = pygame.image.load("blue_b2.png")
yellow_b2 = pygame.image.load("yellow_b2.png")
red_b2 = pygame.image.load("red_b2.png")

blue_bullet2 = pygame.image.load("blue_bullet2.png")
yellow_bullet2 = pygame.image.load("yellow_bullet2.png")
red_bullet2 = pygame.image.load("red_bullet2.png")


blue_b1 = pygame.transform.scale(blue_b1,(zx_change,zy_change)) #(160,240)
yellow_b1 = pygame.transform.scale(yellow_b1,(zx_change,zy_change))  #(160,240)
red_b1 = pygame.transform.scale(red_b1,(zx_change,zy_change))  #(160,240)
red_bullet1 = pygame.transform.scale(red_bullet1,(bx_change,by_change))  #(250,200)
blue_bullet1 = pygame.transform.scale(blue_bullet1,(bx_change,by_change))  #(250,200)
yellow_bullet1 = pygame.transform.scale(yellow_bullet1,(bx_change,by_change))  #(250,200)

blue_b2 = pygame.transform.scale(blue_b2,(zx_change,zy_change)) #(160,240)
yellow_b2 = pygame.transform.scale(yellow_b2,(zx_change,zy_change))  #(160,240)
red_b2 = pygame.transform.scale(red_b2,(zx_change,zy_change))  #(160,240)
red_bullet2 = pygame.transform.scale(red_bullet2,(bx_change,by_change))  #(250,200)
blue_bullet2 = pygame.transform.scale(blue_bullet2,(bx_change,by_change))  #(250,200)
yellow_bullet2 = pygame.transform.scale(yellow_bullet2,(bx_change,by_change))  #(250,200)



p1_x = 0
p1_y = 0
p1_color = (255,0,0)


p2_x = 950
p2_y = 0
p2_color = (255,255,0)

pygame.draw.rect(screen, p1_color, [p1_x,p1_y,50,zy_change],0)
pygame.draw.rect(screen, p2_color, [p2_x,p2_y,50,zy_change],0)




class Zombie :
	def __init__(self):
		self.x = 0
		self.y = 0
		self.who = 1
		self.color = (0,0,0)
		self.life = 0

class Bullet:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.who = 1
		self.color = (0,0,0)
		self.life = 0