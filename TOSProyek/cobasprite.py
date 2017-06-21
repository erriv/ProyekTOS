import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((960,540))

class spritesheet(object):
	def __init__(self, filename):
		self.sheet = pygame.image.load(filename).convert()
	def image_at(self, rectangle, colorkey = None):
        #Loads image from x,y,x+offset,y+offset
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image
		
ss = spritesheet('char1.png')
image = ss.image_at((0, 0, 32, 32))

gameDisplay.blit(image,(160,160))
pygame.display.update()

