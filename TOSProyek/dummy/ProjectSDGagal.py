from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty,ObjectProperty,StringProperty,ListProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color, Canvas
from functools import partial
from random import *
from kivy.core.window import Window
Window.clearcolor=(0,0,0,1)
Window.size=(854,480)

class mainMenu(Widget):
	def __init__(self,**kwargs):
		super(mainMenu,self).__init__(**kwargs)
		with self.canvas:
			self.canvas.add(Rectangle(pos=self.pos,size=Window.size,source='nature.jpg',size_hint=(1,1)))	
		
		self.msg = Label(text = 'Monopoly GX')
		self.msg.font_size = Window.width*0.1
		self.msg.font_name = 'KBDunkTank.ttf'
		self.msg.pos = (Window.width*0.45,Window.height*0.75)
		self.add_widget(self.msg)
		
		self.btn1=Button(text='play game')
		self.btn1.font_size=Window.width/20
		self.btn1.size=Window.width*0.3,Window.height*0.2
		self.btn1.pos=Window.width*0.35,Window.height*0.4
		self.add_widget(self.btn1)
		
		self.btn2=Button(text='exit')
		self.btn2.font_size=Window.width/20
		self.btn2.size=Window.width*0.3,Window.height*0.2
		self.btn2.pos=Window.width*0.35,Window.height*0.1
		self.add_widget(self.btn2)
		
class ProjectSDApp(App):
	def build(self):
		self.Game=Widget()
		A=mainMenu()
		A.btn2.bind(on_release=self.stop())
		self.Game.add_widget(A)
		return self.Game
		
ProjectSDApp().run()
