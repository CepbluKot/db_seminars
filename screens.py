
from logging import root
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = (1920, 1080)


class LoginScreen(Screen):

    pass


class NavScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class TestApp(MDApp):

    def build(self):
        kv = Builder.load_file('scrn.kv')

        return kv

    def login(self):
        login = self.root.ids.login_field.text
        password = self.root.ids.password_field.text
        self.root.ids.login_field.text = ''
        self.root.ids.password_field.text = ''
        print(login, password)
        self.root.transition = RiseInTransition()
        self.root.current = 'NavScreen'


TestApp().run()
