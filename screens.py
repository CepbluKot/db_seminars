from logging import root
from kivy.core import text
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.uix.button import Button
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp

Window.size = (1920, 1080)


class LoginScreen(Screen):
    pass


class NavScreen(Screen):
      pass
    

class WindowManager(ScreenManager):
    
    def update_data(self):
        smth = self.ids.text_one.text
        lin = self.ids.syda
        print(smth)
        
        det = BoxLayout()

        table = MDDataTable(
            check=True,
            size_hint=(0.5, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ('fir', dp(30)),
                ('sec', dp(30)),
                ('thi', dp(30))
            ],
            row_data=[
                ('smb', '123', 'aaa'),
                ('smb 2', '345', 'bbb'),
                ('smb last', '999', 'ccc')
            ]
        )

        lin.add_widget(det)
        
        
        det.add_widget(table)

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
