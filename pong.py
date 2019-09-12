import pygame
import numpy as np
import random
from time import sleep
import sys

class Ball:
	def __init__(self):
		self.x=0
		self.y=0
		self.angle=0
		self.speed=1
	def move(self):
		if self.angle==0:
			self.y-=1
		elif self.angle==1:
			self.y-=1
			self.x+=1
			if self.x==24:
				self.angle=7
		elif self.angle==2:
			self.x+=1
		elif self.angle==3:
			self.y+=1
			self.x+=1
			if self.x==24:
				self.angle=5
		elif self.angle==4:
			self.y+=1
		elif self.angle==5:
			self.y+=1
			self.x-=1
			if self.x==0:
				self.angle=3
		elif self.angle==6:
			self.x-=1
		else:
			self.y-=1
			self.x-=1
			if self.x==0:
				self.angle=1
		
		
class Table:
	def __init__(self):
		self.x=0
		self.y=0
	def left(self):
		self.x-=1
	def right(self):
		self.x+=1

class Game_Control:
	def __init__(self):
		self.ball=Ball()
		self.table=(Table(),Table())
		self.res=False
		self.reset()
		self.count=6
		self.res=False
	def move(self):
		for _ in range(self.ball.speed):
			self.ball.move()
			self.check()
			if self.res: break
		if self.res: self.res=False
	def check(self):
		if self.ball.y==2:
			if self.ball.x==self.table[1].x:
				if self.ball.angle==0: self.ball.angle=4
				elif self.ball.angle==1: self.ball.angle=3
				elif self.ball.angle==7: self.ball.angle=5
				self.count-=1
			elif self.ball.x==self.table[1].x+1:
				if self.ball.angle==0: self.ball.angle=3
				elif self.ball.angle==1: self.ball.angle=3
				elif self.ball.angle==7: self.ball.angle=4
				self.count-=1
			elif self.ball.x==self.table[1].x-1:
				if self.ball.angle==0: self.ball.angle=5
				elif self.ball.angle==1: self.ball.angle=4
				elif self.ball.angle==7: self.ball.angle=5
				self.count-=1
			if self.count==0:
				self.count=6
				self.ball.speed+=1
		elif self.ball.y==48:
			if self.ball.x==self.table[0].x:
				if self.ball.angle==4: self.ball.angle=0
				elif self.ball.angle==3: self.ball.angle=1
				elif self.ball.angle==5: self.ball.angle=7
				self.count-=1
			elif self.ball.x==self.table[0].x+1:
				if self.ball.angle==4: self.ball.angle=1
				elif self.ball.angle==3: self.ball.angle=1
				elif self.ball.angle==5: self.ball.angle=0
				self.count-=1
			elif self.ball.x==self.table[0].x-1:
				if self.ball.angle==4: self.ball.angle=7
				elif self.ball.angle==3: self.ball.angle=0
				elif self.ball.angle==5: self.ball.angle=7
				self.count-=1
			if self.count==0:
				self.count=6
				self.ball.speed+=1
		elif self.ball.y==0:
			self.reset()
			print('2 lost')
		elif self.ball.y==50:
			self.reset()
			print('1 lost')
	def reset(self):
		self.table[0].x=13
		self.table[0].y=49
		self.table[1].x=13
		self.table[1].y=1
		self.ball.y=25+random.randint(0,1)
		self.ball.x=13
		self.count=10
		self.ball.speed=1
		if random.randint(0,1)==0: self.ball.angle=0
		else: self.ball.angle=4
		self.res=True
		
		
class Game:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((250, 500))
		pygame.display.set_caption(('Pong'))
		self.clock = pygame.time.Clock()
		self.game=Game_Control()
	def show(self):
		self.window.fill((255,255,255))
		#draw
		pygame.draw.rect(self.window,(0,0,0),pygame.Rect(10*self.game.ball.x,10*self.game.ball.y,10,10))
		pygame.draw.rect(self.window,(0,0,0),pygame.Rect(10*self.game.table[0].x-10,10*self.game.table[0].y,30,10))
		pygame.draw.rect(self.window,(0,0,0),pygame.Rect(10*self.game.table[1].x-10,10*self.game.table[1].y,30,10))
		
		pygame.display.flip()
		self.clock.tick(60)
	def loop(self):
		loss=[[],[]]
		show=False
		slow=False
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.game.table[0].right()
					if event.key == pygame.K_LEFT:
						self.game.table[0].left()
					if event.key == pygame.K_d:
						self.game.table[1].right()
					if event.key == pygame.K_a:
						self.game.table[1].left()
			sleep(0.15)
			self.game.move()
			self.show()

game=Game()
game.loop()
		