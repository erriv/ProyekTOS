# -*- coding: utf-8 -*-
import pygame
import sqlite3
from random import randint

#connect to our mini database, not will be modified too much, only read it, so it is a very viable option
db=sqlite3.connect('All.db', check_same_thread=False)
cursor=db.cursor()

#start the pygame and set some things needed here
pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()
gameDisplay = pygame.display.set_mode((800,540))
pygame.display.set_caption('JeBaited Monopoly')
clock=pygame.time.Clock()

class spritesheet(object):
	def __init__(self, filename):
		self.sheet = pygame.image.load(filename).convert()
	def image_at(self, rectangle):
		image = pygame.Surface([32,32], pygame.SRCALPHA, 32).convert_alpha()
		image.blit(self.sheet, (0, 0), rectangle)
		return image	
class forImage(object):
	def __init__(self,namafile,pos):
		self.bg=pygame.image.load(namafile)
		self.bgPos=pos
		self.bgSize=self.bg.get_rect().size
	def draw(self):
		gameDisplay.blit(self.bg,self.bgPos)
class button(forImage):
	def __init__(self,namafile,pos,text,s):
		forImage.__init__(self,namafile,pos)
		self.font=pygame.font.Font('attackofthecucumbers.ttf',s)
		self.textSurface=self.font.render(text,True,(0,0,0))
		#get the reference to the text position
		self.rect=self.textSurface.get_rect()
		self.rect.center=((self.bgPos[0]+(self.bgSize[0]*0.5)),self.bgPos[1]+(self.bgSize[1]*0.5))	
	def draw(self):
		forImage.draw(self)
		gameDisplay.blit(self.textSurface,self.rect)
	def isPressed(self,pos):
		if (pos[0]>= self.bgPos[0] and pos[0] <= self.bgPos[0] + self.bgSize[0] and pos[1]>= self.bgPos[1] and pos[1] <= self.bgPos[1] + self.bgSize[1]):
			return True
		return False
class player(object):
	def __init__(self,namafile,pos,id):
		self.Stat=None
		self.uang=2000
		self.id=id
		self.bgPos=pos
		self.x=0
		self.y=2
		self.ss = spritesheet(namafile)
		self.image = self.ss.image_at((self.x*32,self.y*32, 32, 32))#starting sprite
		self.countsprite=0
	def draw(self):
		gameDisplay.blit(self.image,self.bgPos)
	def update(self):
		self.countsprite+=1
		if(self.countsprite>60):self.countsprite=0
		self.x=int(self.countsprite/30)
		self.image = self.ss.image_at((self.x*32,self.y*32, 32, 32))
	def moveto(self,beg,dest):#is used when get card for change place or go to jail
		e=beg
		while True:
			if e.placename==dest:
				self.bgPos=(e.bgPos[0]+29,e.bgPos[1]+29)
				return e
			e=e.next
class tile(forImage):
	def __init__(self,namafile,pos,harga,placename):
		forImage.__init__(self,namafile,pos)
		self.ownedBy=None
		self.status=0
		self.harga=harga
		self.placename=placename
		next=None
	def updateStatus(self):
		self.status+=1
	def draw(self):
		gameDisplay.blit(self.bg,self.bgPos)		
class path(object):
	def __init__(self):
		self.head = None
		self.tail = None
		cursor.execute('select * from place;')
		data=cursor.fetchall()
		for i in data:
			self.Add(i[3],(i[4],i[5]),i[2],i[1])
	def Add(self,namafile,pos,harga,placename):
		a=tile(namafile,pos,harga,placename)
		if(self.head is None):
			self.head=a
			self.tail=a
			self.head.next=self.tail
			self.tail.next=self.head
		else:
			self.tail.next = a
			a.next = self.head
			self.tail = a
	def draw(self):
		self.head.draw()
		e=self.head.next
		while(e!=self.head):
			e.draw()
			e=e.next
	def reset(self):
		self.head.ownedBy=None
		self.head.status=0
		e=self.head.next
		while(e!=self.head):
			e.ownedBy=None
			e.status=0
			e=e.next
	def writeAsset(self,num):
		atas=50
		e=self.head.next
		if self.head.ownedBy==num:
			if self.head.status==1:
				makeWriting('start: House',(400,atas),(255,255,255))
			elif self.head.status==2:
				makeWriting('start: Hotel',(400,atas),(255,255,255))
			atas+=50
		while e!=self.head:
			if e.ownedBy==num:
				if e.status==1:
					makeWriting(e.placename+': House',(400,atas),(255,255,255))
				elif e.status==2:
					makeWriting(e.placename+': Hotel',(400,atas),(255,255,255))
				atas+=50
			e=e.next
class kartu(object):
	"""tipe kartu:
	1->masuk penjara
	2->dapet uang
	3->hilang uang
	4->pindah tile
	5->move n tile"""
	def __init__(self,type,val):
		self.tipe=type
		self.value=val
		next=None
class deck(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.card=[]
		
		cursor.execute('select * from kartu;')
		hasilquery=cursor.fetchall()
		
		for i in hasilquery:
			if i[1]==1:
				self.card.append((1,i[2]))#the [1] is just for decorators, as we don't need it
			elif i[1]==2:
				self.card.append((2,i[2]))
			elif i[1]==3:
				self.card.append((3,i[2]))
			elif i[1]==4:
				self.card.append((4,i[2]))
			elif i[1]==5:
				self.card.append((5,i[2]))
		
		#shuffle the card
		for i in range(len(self.card)):
			dumb=randint(0,len(self.card)-1)
			self.card[i],self.card[dumb]=self.card[dumb],self.card[i]
		
		for i in self.card:
			self.Add(i[0],i[1])
			
	def drawCard(self):
		x=self.head
		self.head=self.head.next
		self.Add(x.tipe,x.value)
		return x
		
	def Add(self,type,val):
		a=kartu(type,val)
		if(self.head is None):
			self.head=a
			self.tail=a
		else:
			self.tail.next = a
			self.tail = a	
class MainMenu(forImage):
	def __init__(self,namafile,pos):#load sound and music
		forImage.__init__(self,namafile,pos)
		self.btn1=button('button2.png',(225,200),'play game!',40)
		self.btn2=button('button2.png',(225,350),'exit',40)
		
		self.font=pygame.font.Font('KBDunkTank.ttf',80)
		self.textSurface=self.font.render('Jebaited Monopoly',True,(255,255,255))
		self.rect=self.textSurface.get_rect()
		self.rect.center=((self.bgPos[0]+(self.bgSize[0]*0.5)),self.bgPos[1]+(self.bgSize[1]*0.2))
		
	def run(self):
		#we just need to draw all of this once
		pygame.mixer.music.load('sound\menu.ogg')
		pygame.mixer.music.play(-1)
		forImage.draw(self)
		gameDisplay.blit(self.textSurface,self.rect)
		self.btn1.draw()
		self.btn2.draw()
		pygame.display.update()
		
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
					
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()
					if (self.btn1.isPressed(pos)):
						pygame.mixer.music.stop()
						return 1
					elif (self.btn2.isPressed(pos)):
						return -1
class climate(forImage):
	def __init__(self,namafile,pos,ef1,ef2,file):
		forImage.__init__(self,namafile,pos)
		self.price1=ef1
		self.price2=ef2
		self.sound=file
	def effect(self,targetNode,Char):
		#no1 got the tile, just pay
		if targetNode.ownedBy is None:
			Char.uang-=self.price1
		#someone got the tile, reduce pay
		elif targetNode.status >0 and type(self.price2)==str:
			if self.price2=='hotel' and targetNode.status==2:
				targetNode.status=1
			if self.price2=='house' and targetNode.status==1:
				targetNode.status=0
		#some1 got the tile, should pay
		elif type(self.price2)==int:
			Char.uang-=self.price2
globalWritingFont=pygame.font.Font('KBDunkTank.ttf',20)
globalWritingFont2=pygame.font.Font('KBDunkTank.ttf',50)
def makeWriting(text,cnt,color):
	textSurface=globalWritingFont.render(text,True,color)
	rect=textSurface.get_rect()
	rect.center=cnt
	gameDisplay.blit(textSurface,rect)
def makeWriting2(text,cnt,color):
	textSurface=globalWritingFont2.render(text,True,color)
	rect=textSurface.get_rect()
	rect.center=cnt
	gameDisplay.blit(textSurface,rect)	
class Game(forImage):
	def __init__(self,namafile,pos):
		forImage.__init__(self,namafile,pos)
		self.Card=forImage('card.jpg',(120,100))
		self.bgKanan=forImage('sidebar.jpg',(540,0))
		self.assetbg=forImage('assetbg.jpg',(0,0))
		self.btn=button('assetbackbtn.png',(600,450),'',40)#this is only for production code
		self.dadu=button('dice.png',(620,200),'',40)
		self.path=path()
		self.deck=deck()
		#all the navigation button
		self.rentBtn=button('btnGood.png',(595,160),'Rent',20)
		self.houseBtn=button('btnGood.png',(595,240),'Buy a House',20)
		self.hotelBtn=button('btnGood.png',(595,320),'Buy a Hotel',20)
		self.skipBtn=button('btnGood.png',(595,400),'Skip',20)
		self.sellBtn=button('btnGood.png',(595,480),'Sell',20)
		self.assetbackBtn=button('assetbackbtn.png',(600,450),'',25)
		self.viewCardbg=forImage('assetbg.jpg',(0,0))
		#for the climate disaster
		self.disaster=[]
		self.disaster.append(climate('typhoon.png',(0,0),150,'hotel','sound\wind.wav'))
		self.disaster.append(climate('earthquake.png',(0,0),130,'house','sound\earthquake.ogg'))
		self.disaster.append(climate('fire.png',(0,0),130,170,'sound\wfire.wav'))
		self.endbg=forImage('end.jpg',(0,0))
	def penjara(self):
		if self.whoinPrison[0] is True and self.whoinPrison[1] is True:
			if self.Prison[0]>self.Prison[1]:
				self.whoinPrison[0]=False
			elif self.Prison[1]>self.Prison[0]:
				self.whoinPrison[1]=False
			else:
				self.whoinPrison[((self.turn)+1)%2]=False
		if self.whoinPrison[(self.turn+1)%2] is True:
			self.Prison[(self.turn+1)%2]-=1
			if self.Prison[(self.turn+1)%2] <= 0:
				self.whoinPrison[(self.turn+1)%2]=False
	def changeTurn(self):
		#code to know which climate
		#there are 2 disasters, as mentioned above
		if self.climateCount==8:
			lho=randint(0,10)
			if lho>8:self.whatClimate=self.disaster[0]
			elif lho>5:self.whatClimate=self.disaster[1]
			else:self.whatClimate=self.disaster[2]
			self.whatClimate.effect(self.node[0],self.char[0])
			self.whatClimate.effect(self.node[1],self.char[1])
			#playing music
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(pygame.mixer.Sound(self.whatClimate.sound))
			self.gameCount=3
			self.climateCount=0
		#end of climate code
		self.rentBuy=None
		if self.turn==0 and self.whoinPrison[1] is False:
			self.turn=1
			self.char[0].Stat='Waiting'
			self.char[1].Stat='Playing'
		elif self.turn==1 and self.whoinPrison[0] is False:
			self.turn=0
			self.char[1].Stat='Waiting'
			self.char[0].Stat='Playing'	
		
		self.penjara()
	def reset(self):
		self.gameCount=0
		self.whichCharToShow=None
		self.rentBuy=None #to know which sidebar to show
		self.char=[]
		self.node=[]
		self.Asset=[]
		self.char.append(player('char1.png',(0,450),0))
		self.char.append(player('char2.png',(0,500),1))
		self.node.append(self.path.head)
		self.node.append(self.path.head)
		self.Asset.append(button('btnGood.png',(595,130),'View Asset',20))
		self.Asset.append(button('btnGood.png',(595,440),'View Asset',20))
		self.char[0].Stat='Playing'
		self.char[1].Stat='Waiting'
		self.move=0
		self.turn=0
		self.frameCount=0
		self.chance=None
		self.whatCard=None
		self.dum=None
		self.tip=None
		self.climateCount=0
		self.whatClimate=None
		self.whoinPrison=[]
		self.whoinPrison.append(False)
		self.whoinPrison.append(False)
		self.path.reset()
		self.Prison=[]
		self.Prison.append(0)
		self.Prison.append(0)
		self.passing=False
		self.whowin=None
	def DrawGameNavigation(self):
		self.drawPlayerStat(0,670,40,(0,0,0),True)
		self.drawPlayerStat(1,670,350,(0,0,0),True)
		self.Asset[0].draw()
		self.Asset[1].draw()
	def DrawRentBuyNavigation(self):
		makeWriting("Choose one Below:",(670,40),(0,0,0))
		self.drawPlayerStat(self.turn,670,100,(80,80,80),False)
		self.rentBtn.draw()
		self.houseBtn.draw()
		self.hotelBtn.draw()
		self.skipBtn.draw()
		self.sellBtn.draw()
	def drawPlayerStat(self,angka,x,y,color,st):
		makeWriting("Player "+ str(angka) +":",(x,y),color)
		makeWriting("Gold:"+str(self.char[angka].uang),(x,40+y),color)
		if st:
			makeWriting("Status:"+str(self.char[angka].Stat),(x,80+y),color)
	def changeDirection(self):
		if(self.node[self.turn].bgPos[0] == 450 and self.node[self.turn].bgPos[1] != 0):
			self.char[self.turn].y=3
		elif(self.node[self.turn].bgPos[0] != 0 and self.node[self.turn].bgPos[1] == 0):
			self.char[self.turn].y=1
		elif(self.node[self.turn].bgPos[0] == 0 and self.node[self.turn].bgPos[1] != 450):
			self.char[self.turn].y=0
		elif(self.node[self.turn].bgPos[0] == 0 and self.node[self.turn].bgPos[1] == 450):
			self.char[self.turn].y=2
	def letsmove(self):
		if self.node[self.turn].placename=='start':
			self.char[self.turn].uang+=250
		x=self.node[self.turn].next.bgPos#get tile coordinate
		self.node[self.turn]=self.node[self.turn].next#go to next node
		x=(x[0]+29,x[1]+29)#set it at middle of the tile
		self.char[self.turn].bgPos=x
			
		self.changeDirection()
		self.frameCount=0
		self.move-=1	
	def run(self):
		pygame.mixer.music.load('sound\game.ogg')
		pygame.mixer.music.play(-1) 
		self.reset()
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.mixer.music.stop()
					pygame.quit()
					quit()
					
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()
					if self.gameCount==0:
						if self.rentBuy is None:
							if self.move == 0:
								if (self.dadu.isPressed(pos)):
									self.move=randint(1,6)
									self.climateCount+=1
									self.gameCount=5
									if self.move ==1:
										self.chance=True
							"""
								if (self.btn1.isPressed(pos)):
									self.climateCount+=1
									self.move=1
									self.chance=True								
								elif (self.btn2.isPressed(pos)):
									self.climateCount+=1
									self.move=2
								elif (self.btn3.isPressed(pos)):
									self.climateCount+=1
									self.move=3
								elif (self.btn4.isPressed(pos)):
									self.climateCount+=1
									self.move=4
								elif (self.btn5.isPressed(pos)):
									self.climateCount+=1
									self.move=5
								elif (self.btn6.isPressed(pos)):
									self.climateCount+=1
									self.move=6"""
							if (self.Asset[0].isPressed(pos)):
								self.gameCount=1
								self.whichCharToShow=0
							elif (self.Asset[1].isPressed(pos)):
								self.gameCount=1
								self.whichCharToShow=1
						else: #whatever is clicked, have to back to game navigation, so don't forget to put self.changeTurn() later
							if (self.rentBtn.isPressed(pos)):
								if self.node[self.turn].ownedBy is None:
									self.char[self.turn].uang-=self.node[self.turn].harga
									self.changeTurn()
								elif self.node[self.turn].ownedBy is not self.turn:
									if self.node[self.turn].status==1:
										self.char[self.turn].uang-=2*self.node[self.turn].harga
										self.char[(self.turn+1)%2].uang+=2*self.node[self.turn].harga
									elif self.node[self.turn].status==2:
										self.char[self.turn].uang-=3*self.node[self.turn].harga
										self.char[(self.turn+1)%2].uang+=3*self.node[self.turn].harga
									self.changeTurn()
									
							elif (self.houseBtn.isPressed(pos)):
								if self.char[self.turn].uang>7*self.node[self.turn].harga and self.node[self.turn].ownedBy is None:
									self.node[self.turn].ownedBy=self.turn
									self.node[self.turn].updateStatus()
									self.char[self.turn].uang-=7*self.node[self.turn].harga
									self.changeTurn()
							elif (self.hotelBtn.isPressed(pos)):
								if self.char[self.turn].uang>5*self.node[self.turn].harga and self.node[self.turn].ownedBy is not None and self.node[self.turn].ownedBy==self.turn and self.node[self.turn].status==1:
									self.node[self.turn].updateStatus()
									self.char[self.turn].uang-=5*self.node[self.turn].harga
									self.changeTurn()
							elif (self.skipBtn.isPressed(pos)):
								if self.node[self.turn].ownedBy is not None and self.node[self.turn].ownedBy is self.turn:
									self.changeTurn()
							elif (self.sellBtn.isPressed(pos)):
								if self.node[self.turn].ownedBy is not None and self.node[self.turn].ownedBy is self.turn:
									if self.node[self.turn].status==1:
										self.char[self.turn].uang+=3*self.node[self.turn].harga
									elif self.node[self.turn].status==2:
										self.char[self.turn].uang+=5*self.node[self.turn].harga
									self.node[self.turn].ownedBy=None
									self.node[self.turn].status=0
									self.changeTurn()
					elif self.gameCount==1:
						if (self.assetbackBtn.isPressed(pos)):
							self.gameCount=0
					elif self.gameCount==2:
						if (self.btn.isPressed(pos)):
							self.gameCount=0
					elif self.gameCount==3:
						if (self.btn.isPressed(pos)):
							self.gameCount=0
							self.whatClimate=None
							pygame.mixer.music.play()
					elif self.gameCount==4:
						if (self.btn.isPressed(pos)):
							pygame.mixer.music.stop()
							return 0
					elif self.gameCount==5:
						if (self.btn.isPressed(pos)):
							self.gameCount=0
					
				"""if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_LEFT:self.char1.y=1
					elif event.key==pygame.K_RIGHT:self.char1.y=2
					elif event.key==pygame.K_DOWN:self.char1.y=0
					elif event.key==pygame.K_UP:self.char1.y=3"""	
			if self.gameCount==0:
				if(self.move>0):
					self.frameCount+=1
					if self.frameCount>20:
						self.letsmove()
						if(self.move==0):
							if self.tip==5 :
								self.tip=None
							
							#for easier code, we call self.penjara in each iteration
							if self.passing:
								self.passing=False
							#when stop at start
							if self.node[self.turn].placename=='start':
								self.changeTurn()	
							#when stop at jail
							if self.node[self.turn].placename=='jail':
								self.whoinPrison[self.turn]=True
								self.passing=True
								self.Prison[self.turn]=2
								self.rentBuy=None
								self.changeTurn()
								
							if self.chance:#we could use rentBuy, because those stop at jail will have it None
								print('masuk is not none')
								self.gameCount=2
								self.whatCard=self.deck.drawCard()
								self.tip=self.whatCard.tipe
								
								if self.whatCard.tipe==1:
									self.dum=-100
									self.whatCard="You move to jail!"
									self.node[self.turn]=self.char[self.turn].moveto(self.node[self.turn],'jail')
									self.whoinPrison[self.turn]=True
									self.Prison[self.turn]=2
									self.rentBuy=None
								elif self.whatCard.tipe==2:
									self.dum=int(self.whatCard.value)
									self.whatCard="You get " + self.whatCard.value + " golds!"
									self.char[self.turn].uang+=self.dum
								elif self.whatCard.tipe==3:
									self.dum=int(self.whatCard.value)
									self.whatCard="You lose " + self.whatCard.value + "golds!"
									self.char[self.turn].uang-=self.dum
									
								elif self.whatCard.tipe==4:
									self.dum=self.whatCard.value
									self.whatCard="You move to "+self.whatCard.value + "!"
									self.node[self.turn]=self.char[self.turn].moveto(self.node[self.turn],self.dum)
									
								elif self.whatCard.tipe==5:
									self.dum=int(self.whatCard.value)
									self.whatCard="You move " + self.whatCard.value + " tiles!"
									self.move=self.dum
									
								self.chance=None
								self.gameCount=2
							
							if self.dum==-100:
								self.changeTurn()
								self.dum=None
								self.tip=None
							#5 means no walk anymore
							elif self.tip!=5:
								#beacuse it has been turn changed, once it became True, cant back
								if self.whoinPrison[self.turn] is False and not self.passing:
									self.rentBuy=self.turn
								self.dum=None
								self.tip=None
				
				if self.char[0].uang<0:
					self.gameCount=4
					self.whowin=0
				if self.char[1].uang<0:
					self.gameCount=4
					self.whowin=1
				forImage.draw(self)
				self.bgKanan.draw()
				self.Card.draw()
				self.path.draw()
				if self.rentBuy is None:
					self.DrawGameNavigation()
					self.dadu.draw()
				else:self.DrawRentBuyNavigation()
			
				self.char[0].update()
				self.char[0].draw()
				self.char[1].update()
				self.char[1].draw()
				
				if self.move>0:
					makeWriting2(str(self.move),(270,350),(255,255,0))
			elif self.gameCount==1:
				self.assetbg.draw()
				self.assetbackBtn.draw()
				self.drawPlayerStat(self.whichCharToShow,100,40,(225,225,225),True)
				self.path.writeAsset(self.whichCharToShow)
			elif self.gameCount==2:
				self.viewCardbg.draw()
				makeWriting2(self.whatCard,(400,270),(255,255,255))
			elif self.gameCount==3:
				self.whatClimate.draw()
			elif self.gameCount==4:
				self.endbg.draw()
				makeWriting2("Player "+str(self.whowin)+" win!",(400,270),(255,255,255))
			elif self.gameCount==5:
				self.assetbg.draw()
				makeWriting2("You Rolled  "+str(self.move)+" !",(400,270),(255,255,255))	
			if self.gameCount>1:
				self.btn.draw()
			pygame.display.update()
			clock.tick(60)
if __name__=='__main__':
	screens=[]
	screens.append(MainMenu(('nature.jpg'),(0,0)))
	screens.append(Game(('bg.jpg'),(90,90)))
	count=0
	while (count>=0 and count<len(screens)):
		count=screens[count].run()
	pygame.quit()
	quit()