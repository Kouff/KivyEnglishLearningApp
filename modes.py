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

    def create_settings_page(*args, **kwargs):
        pass

    def create_main_mode_page(*args, **kwargs):
        pass

    def go_to_settings_page(self, *args, **kwargs):
        print('go_to_settings_page')
        self.create_settings_page()
        self.screen_manager.switch_to(self.settings_screen)

    def go_to_main_mode_page(*args, **kwargs):
        pass

    def start(*args, **kwargs):
        pass


class IrregularVerbMode(BaseMode):
    name = 'Learn irregular verbs'

    def create_settings_page(self):
        self.settings_screen = Screen(name="settings")
        bx = BoxLayout(orientation='vertical')
        self.spiner_level = Spinner(
            text='Select difficulty level',
            values=('Low', 'Middle', 'High', 'All')
        )
        bt = Button(text='Start')
        bt.bind(on_release=self.start)
        bx.add_widget(self.spiner_level)
        bx.add_widget(bt)
        self.settings_screen.add_widget(bx)

    def create_main_mode_page(self):
        pass

    def start(self, instance):
        pass
