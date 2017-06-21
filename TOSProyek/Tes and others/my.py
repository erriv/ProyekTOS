from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from random import random
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
from kivy.graphics.context_instructions import Color

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window

class ScatterTextWidget(BoxLayout):
	teks=ObjectProperty([(0,300),(300,300),(600,300)])
	#global for linked-list
	def __init__(self):
		super(ScatterTextWidget,self).__init__()
		'''
		with self.canvas:
			Color(0,0.5,1,0.7)
			Rectangle(pos=(0,100),size=(300,100))
			Ellipse(pos=(0,400),size=(300,100))
			Line(points=([0,0,500,300,178]),close=True,width=3)
		'''
		for i in self.teks:
			with self.canvas:
				Color(0,0.5,1,0.7)
				Rectangle(pos=(i[0],i[1]),size=(150,150))
				
	def changeLabelColour(self):
		colour=[random.random() for i in xrange(3)]+[1]
		
		label1=self.ids['lbl1']
		label1.color=colour
		
		label2=self.ids['lbl2']
		label2.color=colour
class RootWidget(Label):
	def doLayout(self,*args):
		num=len(self.children)
		wpc=self.width/num
		
		positions=range(0,self.width,wpc)
		for position,child in zip(positions,self.children):
			child.height=self.height
			child.x=self.x+position
			child.y=self.y
			child.width = wpc
			
	def on_size(self,*args):
		self.doLayout()
class AnimRect(Widget):
	def anim(self):
		Animation.cancel_all(self)
		rndx=random() * self.width
		rndy=random() * self.height
		
		anima=Animation(x=rndx,y=rndy,duration=4)
		anima.start(self)
	'''	
	def on_touch_move(self,touch):
		self.x=touch.pos[0]
		self.y=touch.pos[1]
		'''
	def on_touch_down(self,touch):
		if self.collide_point(*touch.pos):
			self.anim()
			print touch.pos
			
class MyApp(App):
    def build(self):
		print(Window.width)
		print(Window.height)
		return AnimRect()
MyApp().run()