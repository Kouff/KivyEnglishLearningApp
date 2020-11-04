from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen


class BaseMode:
    name = 'Base mode name'

    def __init__(self, screen_manager, home_screen):
        self.screen_manager = screen_manager
        self.home_screen = home_screen
        self.settings_screen = None
        self.main_screen = None

    def create_page(self, name, build):
        screen = Screen(name=name)
        main_layout, layout_and_widgets = build()
        for layout, widgets in layout_and_widgets:
            for widget in widgets:
                layout.add_widget(widget)
        screen.add_widget(main_layout)
        return screen

    def build_settings_page(self):
        pass

    def build_main_page(self):
        pass

    def create_settings_page(self):
        self.settings_screen = self.create_page('settings', self.build_settings_page)

    def create_main_page(self):
        self.main_screen = self.create_page('main', self.build_main_page)

    def go_to_home_page(self, instance):
        self.screen_manager.switch_to(self.home_screen)

    def go_to_settings_page(self):
        if self.settings_screen is None:
            self.create_settings_page()
        self.screen_manager.switch_to(self.settings_screen)

    def go_to_main_page(self, instance):
        self.screen_manager.switch_to(self.main_screen)

    def start(*args, **kwargs):
        pass


class IrregularVerbMode(BaseMode):
    name = 'Learn irregular verbs'

    def build_settings_page(self):
        bx = BoxLayout(orientation='vertical')
        bt_home = Button(text='Home')
        bt_home.bind(on_release=self.go_to_home_page)
        self.spiner_level = Spinner(
            text='Select difficulty level',
            values=('Low', 'Middle', 'High', 'All')
        )
        bt_start = Button(text='Start')
        bt_start.bind(on_release=self.start)
        return bx, zip(
            (bx,),
            ((bt_home, self.spiner_level, bt_start),)
        )

    def create_main_page(self):
        pass

    def start(self, instance):
        pass
