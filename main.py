from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import *
from random import choice, randint

from modes import IrregularVerbMode, BaseMode


def update_size(x, y):
    z = 0.4
    xx = x * z
    yy = y * z
    return (xx, yy)


class MyApp(App):
    modes_class = (IrregularVerbMode,)
    instances_of_mods = {}

    def go_to_settings_page(self, instance):
        mode = self.instances_of_mods[instance.text]
        mode.go_to_settings_page()

    def set_modes(self):
        for mode_class in self.modes_class:
            instance = mode_class(self.sm, self.home_screen)
            if self.instances_of_mods.get(instance.name) is None:
                self.instances_of_mods[instance.name] = instance
            else:
                raise Exception(f"{mode_class}`s name exist")

    def add_mode_buttons(self, layout):
        self.set_modes()
        for mode in self.instances_of_mods.values():
            bt = Button(text=mode.name)
            bt.bind(on_release=self.go_to_settings_page)
            layout.add_widget(bt)

    def create_home_page(self):
        self.home_screen = Screen(name="home")
        bl1 = BoxLayout(orientation='vertical', padding=(20, 40, 20, 40))
        lb1 = Label(text="Home")
        gl = GridLayout(cols=2)
        bl1.add_widget(lb1)
        self.add_mode_buttons(gl)
        bl1.add_widget(gl)
        self.home_screen.add_widget(bl1)

        self.sm.add_widget(self.home_screen)

    def build(self):
        # self.font_size = 32
        self.sm = ScreenManager(transition=RiseInTransition())
        self.create_home_page()

        self.sm.current = 'home'
        return self.sm


if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.config import Config

    x, y = 1080, 2340
    Window.size = update_size(x, y)
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    # for p, ps, pp, r in zip(present, past_simple, past_participle, rus):
    #     Verb(p, ps, pp, r)
    MyApp().run()
