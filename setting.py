import pygame
import time


pygame.init()

height = 700 	#改930
weight = 1000 	#改1600
bg = (0,0,0)
black = (0,0,0)

zy_change = 140 #改180
zx_change = 120 #160
bx_change = 175 #250
by_change = 135 # 200
player_size = 100 # 200
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)

green = (0,200,0)
orange = (255,176,0)

bright_red = (200,0,0)
bright_green = (0,255,0)
bright_yellow = (255,226,0)

clock_my = 0

# file = open("text.txt","a")

screen = pygame.display.set_mode((weight,height))
pygame.display.set_caption("Zombie Kolor")
clock = pygame.time.Clock()

back = pygame.image.load("back.jpg")

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

p1_red = pygame.image.load("p1_r.png") 
p1_yellow = pygame.image.load("p1_y.png")
p1_blue = pygame.image.load("p1_b.png")
p2_red = pygame.image.load("p2_r.png")
p2_yellow = pygame.image.load("p2_y.png")
p2_blue = pygame.image.load("p2_b.png")

love = pygame.image.load("love.png")
love = pygame.transform.scale(love,(30,30)) 

bullet_show = pygame.image.load("bull.png")
bullet_show = pygame.transform.scale(bullet_show,(25,25))


back = pygame.transform.scale(back,(weight,height - player_size))
blue_b1 = pygame.transform.scale(blue_b1,(zx_change,zy_change)) 
yellow_b1 = pygame.transform.scale(yellow_b1,(zx_change,zy_change))  
red_b1 = pygame.transform.scale(red_b1,(zx_change,zy_change))  
red_bullet1 = pygame.transform.scale(red_bullet1,(bx_change,by_change))  
blue_bullet1 = pygame.transform.scale(blue_bullet1,(bx_change,by_change))  
yellow_bullet1 = pygame.transform.scale(yellow_bullet1,(bx_change,by_change))  

blue_b2 = pygame.transform.scale(blue_b2,(zx_change,zy_change)) 
yellow_b2 = pygame.transform.scale(yellow_b2,(zx_change,zy_change))  
red_b2 = pygame.transform.scale(red_b2,(zx_change,zy_change))  
red_bullet2 = pygame.transform.scale(red_bullet2,(bx_change,by_change))  
blue_bullet2 = pygame.transform.scale(blue_bullet2,(bx_change,by_change))  
yellow_bullet2 = pygame.transform.scale(yellow_bullet2,(bx_change,by_change))  

p1_red = pygame.transform.scale(p1_red,(bx_change,by_change)) 
p1_yellow = pygame.transform.scale(p1_yellow,(bx_change,by_change)) 
p1_blue =pygame.transform.scale(p1_blue,(bx_change,by_change)) 
p2_red = pygame.transform.scale(p2_red,(bx_change,by_change)) 
p2_yellow = pygame.transform.scale(p2_yellow,(bx_change,by_change)) 
p2_blue =pygame.transform.scale(p2_blue,(bx_change,by_change)) 

p1win = pygame.image.load("p1win.jpg")
p2win = pygame.image.load("p2win.jpg")

p1win = pygame.transform.scale(p1win,(weight,height))
p2win = pygame.transform.scale(p2win,(weight,height))

startBackground = pygame.image.load('start.jpg')  #一開始的背景
startBackground = pygame.transform.scale(startBackground,(weight,height))
instructionBackground = pygame.image.load('instruction.jpg')  #遊戲介紹的背景
instructionBackground = pygame.transform.scale(instructionBackground,(weight,height))

second = 0
minute = 0

def text_objects(text, font,color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()
 
def message_display(text,size,color,we,he):
	largeText = pygame.font.Font('LucidaBrightDemiBold.ttf',size)
	TextSurf, TextRect = text_objects(text, largeText,color)
	TextRect.center = ((we),(he))
	screen.blit(TextSurf, TextRect)
	
# def button(msg,x,y,w,h,ic,ac,action=None):
# 	mouse = pygame.mouse.get_pos()
# 	click = pygame.mouse.get_pressed()
# 	print(click)
# 	if x+w > mouse[0] > x and y+h > mouse[1] > y:
# 		pygame.draw.rect(screen, ac,(x,y,w,h))

# 		if click[0] == 1 and action != None:
# 			action()         
# 	else:
# 		pygame.draw.rect(screen, ic,(x,y,w,h))

# 	largeText = pygame.font.Font('LucidaBrightDemiBold.ttf',80)
# 	TextSurf, TextRect = text_objects(msg, largeText)
# 	TextRect.center = ((x+w/2),(y+h/2))
# 	screen.blit(TextSurf, TextRect)


# def action():
# 	main()

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
		

class player:
	def _init_(self):
		self.x = 0
		self.y = 0
		self.seat = 0
		self.life = 0
		self.color = 0
		self.live_color = 0
		self.clock_ = 0


p1 = player()
p1.x = 0
p1.y = 0
p1.seat = 1
p1.live = 5
p1.color = red
p1.live_color = red
p1.clock_ = 200

p2 = player()
p2.x = weight - bx_change
p2.y = 0
p2.seat = 1
p2.live = 5
p2.color = red
p2.live_color = red
p2.clock_ = 200

zombie_list = []
bullet_list = []



def reset():
	global p1,p2,zombie_list,bullet_list
	p1 = player()
	p1.x = 0
	p1.y = 0
	p1.seat = 1
	p1.live = 5
	p1.color = red
	p1.live_color = red
	p1.clock_ = 200

	p2 = player()
	p2.x = weight - bx_change
	p2.y = 0
	p2.seat = 1
	p2.live = 5
	p2.color = red
	p2.live_color = red
	p2.clock_ = 200

	zombie_list = []
	bullet_list = []
	return p1,p2