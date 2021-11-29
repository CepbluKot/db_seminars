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
import psycopg2


con = psycopg2.connect(
    database="db_sem",
    user="postgres",
    password="752505",
    host="127.0.0.1",
    port="5432"
)


Window.size = (2560, 1600)


class LoginScreen(Screen):
    pass


class NavScreen(Screen):
    pass


class WindowManager(ScreenManager):

    def preset(self):

        lin = self.ids.main_table

        det = BoxLayout()

        cur = con.cursor()
        cur.execute('SELECT * FROM tarifs')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        con.commit()

        cur = con.cursor()
        cur.execute('SELECT * FROM mt')

        row = cur.fetchall()
        con.commit()

        table = MDDataTable(
            check=True,
            size_hint=(0.5, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ('id', dp(30)),
                ('first_name', dp(30)),
                ('sec_name', dp(30)),
                ('last_name', dp(30)),
                ('phone_id', dp(30)),
                ('address_id', dp(30))
            ], use_pagination=True,
            row_data=row,
            elevation=0
        )
        lin.add_widget(det)
        det.add_widget(table)

    def update_data(self):

        lin = self.ids.main_table

        det = BoxLayout()

        cur = con.cursor()
        first_name = self.ids.first_name.text
        surname = self.ids.surname.text
        las_name = self.ids.last_name.text
        phone_num = self.ids.phone_number.text
        address = self.ids.address.text

        cur.execute('insert into mt (first_name, sec_name, last_name, phone_id, address_id)  values ( %s, %s, %s, %s, %s);',
                    (first_name, surname, las_name, 123, 132))

        cur.execute('SELECT * FROM mt')

        row = cur.fetchall()
        con.commit()

        table = MDDataTable(
            size_hint=(0.5, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ('id', dp(30)),
                ('first_name', dp(30)),
                ('sec_name', dp(30)),
                ('last_name', dp(30)),
                ('phone_id', dp(30)),
                ('address_id', dp(30))
            ],
            row_data=row, use_pagination=True,
            elevation=0
        )
        det.add_widget(table)
        lin.add_widget(det)

        self.ids.first_name.text = ''
        self.ids.surname.text = ''
        self.ids.last_name.text = ''
        self.ids.phone_number.text = ''
        self.ids.address.text = ''


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

        cur = con.cursor()
        cur.execute('SELECT * FROM mt')

        row = cur.fetchall()
        con.commit()

        table_prebuild = MDDataTable(
            size_hint=(0.5, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ('id', dp(30)),
                ('first_name', dp(30)),
                ('sec_name', dp(30)),
                ('last_name', dp(30)),
                ('phone_id', dp(30)),
                ('address_id', dp(30))
            ],
            row_data=row, use_pagination=True,
            elevation=0
        )
        lin.add_widget(det)
        det.add_widget(table_prebuild)


TestApp().run()
