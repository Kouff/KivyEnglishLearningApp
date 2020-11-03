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
    name = 'Name mode'

    def __init__(self, screen_manager, home_screen):
        self.screen_manager = screen_manager
        self.home_screen = home_screen

    def create_settings_page(*args, **kwargs):
        pass

    def create_main_mode_page(*args, **kwargs):
        pass

    def start(*args, **kwargs):
        pass


class IrregularVerbMode(BaseMode):
    name = 'Learn irregular verbs'

    def create_settings_page(self, instance):
        bx = BoxLayout(orientation='vertical')
        self.spiner_level = Spinner(
            text='Select difficulty level',
            values=('Home', 'Work', 'Other', 'Custom')
        )
        bt = Button(text='Start')
        bt.bind(on_release=self.start)
        bx.add_widget(self.spiner_level)
        bx.add_widget(bt)
        self.sm.add_widget(bx)

    def create_main_mode_page(self, instance):
        pass

    def start(self, instance):
        pass
