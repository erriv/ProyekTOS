from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (960,540)
Window.clearcolor = get_color_from_hex('#000000') # black

class HomeScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class MovingImage(DragBehavior,Image):
    pass

class StaticImage(Image):
    pass

SM=Builder.load_file('ProjectSD.kv')

class ProjectSDApp(App):
    def build(self):
        A = SM
        A.screens[1].ids.gamefloat.add_widget(MovingImage(size_hint = [0.3,0.3]))
        A.screens[1].ids.gamefloat.add_widget(StaticImage(pos = (0,0)))
        return A

if __name__=='__main__':
	print(Window.size)
	print(SM.screens[1].size)
	ProjectSDApp().run()