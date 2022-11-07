from kivymd.app import MDApp

from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SlideTransition, RiseInTransition

Window.size = (412, 732)

from itertools import chain
from kivy.graphics.texture import Texture

class Gradient(object):
    @staticmethod
    def horizontal(*args):
        texture = Texture.create(size=(len(args), 1), colorfmt='rgba')
        buf = bytes([int(v * 255) for v in chain(*args)])  # flattens
        texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        return texture
    @staticmethod
    def vertical(*args):
        texture = Texture.create(size=(1, len(args)), colorfmt='rgba')
        buf = bytes([int(v * 255) for v in chain(*args)])  # flattens
        texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        return texture

class Main(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(MDApp):
    def build(self):
        self.title = "BeneFit"
        self.icon  = "assets/icon/icon.png"
        return Main()

    def on_start(self):
        pass
        # self.fps_monitor_start()
        # self.root.current = "home_screen"
        # self.root.current = "streak_screen"
        # self.root.current = "message_screen"
        # self.root.current = "profile_screen"
        # self.root.current = "community_screen"
        # self.root.current = "notification_screen"
        # self.root.current = "fitness_diary_screen"

    def view_streak(self):
        self.root.transition = RiseInTransition()
        self.root.current = "streak_screen"
        self.root.transition = SlideTransition()

if __name__ == "__main__":
    MyApp().run()