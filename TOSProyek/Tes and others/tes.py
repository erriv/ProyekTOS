from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.label import CoreLabel
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line

Window.size=(300,500)
class coba(Widget):
	background_color = ListProperty((1,1,1,1))
	data=ListProperty()

	def render2(self):
		la = self.ids['ti']
		self.data.append(la.text)
		print (self.data)
		count=0
		with self.canvas:
			#self.canvas.clear()
			for i in self.data:
				label=CoreLabel(text=i,color=(1,1,1,1))
				label.refresh()
				text=label.texture
				print(text)
				self.canvas.add(Rectangle(size=(300,40), pos=(0,(count+1)*50), texture=text))
				count+=1
				
		#la.clear()

class tesApp(App):
	def build(self):
		print(Window.width)
		print(Window.height)
		return coba()
	
if __name__=='__main__':
	tesApp().run()