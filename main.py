from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from random import choice, randint, random
import time
from kivy.clock import Clock
from modes import IrregularVerbMode, BaseMode

z = 0.4


def update_size(x, y):
    xx = x * z
    yy = y * z
    return (xx, yy)


def update_font_size(x):
    return x * z


class MyApp(App):
    _fs = update_font_size(64)  # font_size
    modes_class = (IrregularVerbMode,)
    instances_of_mods = {}

    def go_to_settings_page(self, instance):
        mode = self.instances_of_mods[instance.text]
        mode.go_to_settings_page()

    def set_modes(self):
        for mode_class in self.modes_class:
            instance = mode_class(self.sm, self.home_screen, self._fs)
            if self.instances_of_mods.get(instance.name) is None:
                self.instances_of_mods[instance.name] = instance
            else:
                raise Exception(f"{mode_class}`s name exist")

    def add_mode_buttons(self, layout):
        self.set_modes()
        for mode in self.instances_of_mods.values():
            bt = Button(text=mode.name, font_size=self._fs)
            bt.bind(on_release=self.go_to_settings_page)
            layout.add_widget(bt)

    def create_home_page(self):
        self.home_screen = Screen(name="home")
        bl1 = BoxLayout(orientation='vertical', padding=(20, 40, 20, 40), spacing=30)
        lb1 = Label(text="Home", size_hint=(1, .2), font_size=self._fs)
        gl = GridLayout(cols=2)
        bl1.add_widget(lb1)
        self.add_mode_buttons(gl)
        bl1.add_widget(gl)
        self.home_screen.add_widget(bl1)

        self.sm.add_widget(self.home_screen)

    def build(self):
        self.sm = ScreenManager(transition=FadeTransition(duration=0.1))
        self.create_home_page()

        self.sm.current = 'home'
        return self.sm


if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.config import Config

    x, y = 1080, 2340
    Window.size = update_size(x, y)
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    MyApp().run()
