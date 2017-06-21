import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticesdadu = (
	(5,-5,-5),
	(5,5,-5),
	(-5,5,-5),
	(-5,-5,-5),
	(5,-5,5),
	(5,5,5),
	(-5,-5,5),
	(-5,5,5),
	)

vertices1 = (
	(5.05,-1,-1),
	(5.05,1,-1),
	(5,1,-1),
	(5,-1,-1),
	(5.05,-1,1),
	(5.05,1,1),
	(5,-1,1),
	(5,1,1),
	)

vertices21 = (
	(3,5,3),
	(3,5.05,3),
	(1,5.05,3),
	(1,5,3),
	(3,5,1),
	(3,5.05,1),
	(1,5,1),
	(1,5.05,1),
	)

vertices22 = (
	(-3,5,-3),
	(-3,5.05,-3),
	(-1,5.05,-3),
	(-1,5,-3),
	(-3,5,-1),
	(-3,5.05,-1),
	(-1,5,-1),
	(-1,5.05,-1),
	)

vertices31 = (
	(4,2,5),
	(4,4,5),
	(2,4,5),
	(2,2,5),
	(4,2,5.05),
	(4,4,5.05),
	(2,2,5.05),
	(2,4,5.05),
	)

vertices32 = (
	(-4,-2,5),
	(-4,-4,5),
	(-2,-4,5),
	(-2,-2,5),
	(-4,-2,5.05),
	(-4,-4,5.05),
	(-2,-2,5.05),
	(-2,-4,5.05),
	)

vertices33 = (
	(1,-1,5),
	(1,1,5),
	(-1,1,5),
	(-1,-1,5),
	(1,-1,5.05),
	(1,1,5.05),
	(-1,-1,5.05),
	(-1,1,5.05),
	)

vertices41 = (
	(3,1,-5),
	(3,3,-5),
	(1,3,-5),
	(1,1,-5),
	(3,1,-5.05),
	(3,3,-5.05),
	(1,1,-5.05),
	(1,3,-5.05),
	)

vertices42 = (
	(3,-1,-5),
	(3,-3,-5),
	(1,-3,-5),
	(1,-1,-5),
	(3,-1,-5.05),
	(3,-3,-5.05),
	(1,-1,-5.05),
	(1,-3,-5.05),
	)

vertices43 = (
	(-3,1,-5),
	(-3,3,-5),
	(-1,3,-5),
	(-1,1,-5),
	(-3,1,-5.05),
	(-3,3,-5.05),
	(-1,1,-5.05),
	(-1,3,-5.05),
	)

vertices44 = (
	(-3,-1,-5),
	(-3,-3,-5),
	(-1,-3,-5),
	(-1,-1,-5),
	(-3,-1,-5.05),
	(-3,-3,-5.05),
	(-1,-1,-5.05),
	(-1,-3,-5.05),
	)

vertices51 = (
	(4,-5,4),
	(4,-5.05,4),
	(2,-5.05,4),
	(2,-5,4),
	(4,-5,2),
	(4,-5.05,2),
	(2,-5,2),
	(2,-5.05,2),
	)

vertices52 = (
	(4,-5,-4),
	(4,-5.05,-4),
	(2,-5.05,-4),
	(2,-5,-4),
	(4,-5,-2),
	(4,-5.05,-2),
	(2,-5,-2),
	(2,-5.05,-2),
	)

vertices53 = (
	(-4,-5,4),
	(-4,-5.05,4),
	(-2,-5.05,4),
	(-2,-5,4),
	(-4,-5,2),
	(-4,-5.05,2),
	(-2,-5,2),
	(-2,-5.05,2),
	)

vertices54 = (
	(-4,-5,-4),
	(-4,-5.05,-4),
	(-2,-5.05,-4),
	(-2,-5,-4),
	(-4,-5,-2),
	(-4,-5.05,-2),
	(-2,-5,-2),
	(-2,-5.05,-2),
	)

vertices55 = (
	(1,-5,1),
	(1,-5.05,1),
	(-1,-5.05,1),
	(-1,-5,1),
	(1,-5,-1),
	(1,-5.05,-1),
	(-1,-5,-1),
	(-1,-5.05,-1),
	)

vertices61 = (
	(-5.05,1,2), #kiri bwh
	(-5.05,3,2), #kanan bwh
	(-5,3,2), #kanan bwh
	(-5,1,2), #kiri bwh
	(-5.05,1,4), #kiri atas
	(-5.05,3,4), #kanan atas
	(-5,1,4), #kiri atas
	(-5,3,4), #kanan atas
	)

vertices62 = (
	(-5.05,1,-4),
	(-5.05,3,-4),
	(-5,3,-4),
	(-5,1,-4),
	(-5.05,1,-2),
	(-5.05,3,-2),
	(-5,1,-2),
	(-5,3,-2),
	)

vertices63 = (
	(-5.05,1,-1),
	(-5.05,3,-1),
	(-5,3,-1),
	(-5,1,-1),
	(-5.05,1,1),
	(-5.05,3,1),
	(-5,1,1),
	(-5,3,1),
	)

vertices64 = (
	(-5.05,-1,2), #kiri bwh
	(-5.05,-3,2), #kanan bwh
	(-5,-3,2), #kanan bwh
	(-5,-1,2), #kiri bwh
	(-5.05,-1,4), #kiri atas
	(-5.05,-3,4), #kanan atas
	(-5,-1,4), #kiri atas
	(-5,-3,4), #kanan atas
	)

vertices65 = (
	(-5.05,-1,-4),
	(-5.05,-3,-4),
	(-5,-3,-4),
	(-5,-1,-4),
	(-5.05,-1,-2),
	(-5.05,-3,-2),
	(-5,-1,-2),
	(-5,-3,-2),
	)

vertices66 = (
	(-5.05,-1,-1),
	(-5.05,-3,-1),
	(-5,-3,-1),
	(-5,-1,-1),
	(-5.05,-1,1),
	(-5.05,-3,1),
	(-5,-1,1),
	(-5,-3,1),
	)


edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)

surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6),
	)

def Cube():
	#dadu
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,1,1))
			glVertex3fv(verticesdadu[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glColor3fv((0,0,0))
			glVertex3fv(verticesdadu[vertex])
	glEnd()
	
	#titik 1
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices1[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices1[vertex])
	glEnd()
	
	#titik 21
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices21[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices21[vertex])
	glEnd()

	#titik 22
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices22[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices22[vertex])
	glEnd()

	#titik 31
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices31[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices31[vertex])
	glEnd()

	#titik 32
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices32[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices32[vertex])
	glEnd()

	#titik 33
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices33[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices33[vertex])
	glEnd()

	#titik41
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices41[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices41[vertex])
	glEnd()

	#titik42
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices42[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices42[vertex])
	glEnd()

	#titik43
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices43[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices43[vertex])
	glEnd()

	#titik44
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices44[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices44[vertex])
	glEnd()

	#titik51
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices51[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices51[vertex])
	glEnd()

	#titik52
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices52[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices52[vertex])
	glEnd()

	#titik53
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices53[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices53[vertex])
	glEnd()

	#titik54
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices54[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices54[vertex])
	glEnd()

	#titik55
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices55[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices55[vertex])
	glEnd()

	#titik61
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices61[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices61[vertex])
	glEnd()

	#titik62
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices62[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices62[vertex])
	glEnd()

	#titik63
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices63[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices63[vertex])
	glEnd()

	#titik64
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices64[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices64[vertex])
	glEnd()

	#titik65
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices65[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices65[vertex])
	glEnd()

	#titik66
	glBegin(GL_QUADS)
	for surface in surfaces:
		for vertex in surface:
			glColor3fv((1,0,0))
			glVertex3fv(vertices66[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices66[vertex])
	glEnd()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	glEnable(GL_DEPTH_TEST)
	gluPerspective(90,(display[0]/display[1]),0.1,50.0)

	counter = 0
	pilihan = 1
	glTranslatef(0.0,0.0,-40)
	
	if pilihan >3:
		glRotatef(180,1,0,0)

	while True:
		if pilihan == 1:
			if counter <82:
				glRotatef(25,1,1,1)
		elif pilihan ==2:
			if counter <78:
				glRotatef(20,1,1,1)
		elif pilihan ==3:
			if counter <90:
				glRotatef(20,0.5,1,1)
		elif pilihan ==4:
			if counter <90:
				glRotatef(20,1,0,1)
		elif pilihan ==5:
			if counter <79:
				glRotatef(20,0.5,1,1)
		elif pilihan ==6:
			if counter <90:
				glRotatef(23,0,1,0.1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(1,0,0)
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0)

					
		x = glGetDoublev(GL_MODELVIEW_MATRIX)
		#print(x)
		counter+=1
		print(counter)

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)
main()