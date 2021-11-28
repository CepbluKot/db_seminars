from kivy.core import text
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.behaviors import elevation
from kivymd.uix.datatables import MDDataTable
from kivy.uix.button import Button
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp


Window.size = (1920, 1080)


class LoginScreen(Screen):
    pass


class NavScreen(Screen):
    pass


class WindowManager(ScreenManager):

    def preset(self):
        
        lin = self.ids.main_table
        
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
                ('smddddb', '123', 'aaa'),
                ('smdddb 2', '345', 'bbb'),
                ('smddb last', '999', 'ccc')
            ],
            elevation=0
        )
        lin.add_widget(det)
        det.add_widget(table)

    def update_data(self):
        
        lin = self.ids.main_table
        
        det = BoxLayout()

        table = MDDataTable(
            size_hint=(0.5, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ('fir', dp(30)),
                ('sec', dp(30)),
                ('thi', dp(30))
            ],
            row_data=[
                ('nobd', '123', 'aaa'),
                ('nobd 2', '345', 'bbb'),
                ('nobd last', '999', 'ccc')
            ],
            elevation=0
        )
        det.add_widget(table)
        lin.add_widget(det)
        


class TestApp(MDApp):

    def build(self):
        kv = Builder.load_file('scrn.kv')
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Purple"
        return kv

    def login(self):
        login = self.root.ids.login_field.text
        password = self.root.ids.password_field.text
        self.root.ids.login_field.text = ''
        self.root.ids.password_field.text = ''
        print(login, password)
        self.root.transition = RiseInTransition()
        self.root.current = 'NavScreen'

        lin = self.root.ids.main_table
        det = MDBoxLayout()
        
        table_prebuild = MDDataTable(
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
            ],
            elevation=0
        )
        lin.add_widget(det)
        det.add_widget(table_prebuild)
        


TestApp().run()
