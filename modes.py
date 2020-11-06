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
from random import choice

from verbs import present, past_simple, past_participle, rus, IrregularVerb


class BaseMode:
    name = 'Base mode name'

    def __init__(self, screen_manager, home_screen, font_size):
        self.screen_manager = screen_manager
        self.home_screen = home_screen
        self._fs = font_size
        self.settings_screen = None
        self.main_screen = None
        self.spiner_level = None
        self.level = None

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

    def go_to_home_page(self, instance=None):
        if self.home_screen is not None:
            self.screen_manager.switch_to(self.home_screen)

    def go_to_settings_page(self, instance=None):
        if self.settings_screen is None:
            self.create_settings_page()
        if self.settings_screen is not None:
            self.screen_manager.switch_to(self.settings_screen)

    def go_to_main_page(self, instance=None):
        if self.level is None:
            if self.spiner_level is not None:
                self.spiner_level.background_color = (1, 0, 0, 1)
        else:
            if self.main_screen is None:
                self.create_main_page()
            if self.main_screen is not None:
                self.init_mode()
                self.screen_manager.switch_to(self.main_screen)

    def set_level(self, spinner, text):
        spinner.background_color = (1, 1, 1, 1)
        self.level = text

    def init_mode(self):
        pass


class IrregularVerbMode(BaseMode):
    name = 'Learn irregular verbs'

    def build_settings_page(self):
        bx = BoxLayout(orientation='vertical', padding=(20, 40), spacing=60)
        bt_home = Button(text='Home', size_hint=(1, 0.23), font_size=self._fs)
        bt_home.bind(on_release=self.go_to_home_page)
        lb = Label(text=self.name, font_size=self._fs)
        self.spiner_level = Spinner(
            text='Select difficulty level',
            values=('Low', 'Low + Middle', 'Middle', 'Middle + High', 'High', 'All'),
            size_hint=(1, 0.4),
            font_size=self._fs
        )
        self.spiner_level.bind(text=self.set_level)
        bt_start = Button(text='Start', font_size=self._fs)
        bt_start.bind(on_release=self.go_to_main_page)
        return bx, zip(
            (bx,),
            ((bt_home, lb, self.spiner_level, bt_start),)
        )

    def build_main_page(self):
        bx = BoxLayout(orientation='vertical', padding=(20, 40), spacing=10)
        bx_switch_screens = BoxLayout(orientation='horizontal', size_hint=(1, 0.075), spacing=10)
        bx_main = BoxLayout(orientation='vertical', padding=(0, 0, 0, 0), spacing=30)
        bt_home = Button(text='Home', font_size=self._fs)
        bt_home.bind(on_release=self.go_to_home_page)
        bt_settings = Button(text='Back to settings', font_size=self._fs)
        bt_settings.bind(on_release=self.go_to_settings_page)
        self.text_input_main = TextInput(font_size=self._fs, multiline=False)
        self.text_input_main.bind(on_text_validate=self.next_command)
        self.label_counter = Label(text='0/0', font_size=self._fs//2, size_hint=(1, 0.1))
        self.label_main = Label(font_size=self._fs)
        self.bt_check = Button(text='Check', font_size=self._fs)
        self.bt_check.bind(on_release=self.next_command)
        return bx, zip(
            (bx_switch_screens, bx_main, bx),
            (
                (bt_home, bt_settings),
                (self.label_counter, self.label_main, self.text_input_main, self.bt_check),
                (bx_switch_screens, bx_main)
            )
        )

    def get_verbs(self, verbs_main):
        if self.level == 'All':
            return list(verbs_main['Low']) + list(verbs_main['Middle']) + list(verbs_main['High'])
        verbs = []
        if 'Low' in self.level:
            verbs += list(verbs_main['Low'])
        if 'Middle' in self.level:
            verbs += list(verbs_main['Middle'])
        if 'High' in self.level:
            verbs += list(verbs_main['High'])
        return verbs

    def update_main_page(self):
        self.text_input_main.text = ''
        if IrregularVerb.verbs:
            self.verb = choice(IrregularVerb.verbs)
            self.form, self.word = self.verb.get()
            self.label_main.text = f"{self.verb.rus}\n<{self.form.capitalize()}>"
        else:
            self.go_to_settings_page()

    def init_mode(self):
        IrregularVerb.verbs = []
        for p, ps, pp, r in zip(
                self.get_verbs(present),
                self.get_verbs(past_simple),
                self.get_verbs(past_participle),
                self.get_verbs(rus)):
            IrregularVerb(p, ps, pp, r)
        self.all_verbs = len(IrregularVerb.verbs)
        self.label_counter.text = self.get_count_verbs()
        self.update_main_page()

    def get_count_verbs(self):
        return f'{self.all_verbs-len(IrregularVerb.verbs)}/{self.all_verbs}'

    def next_command(self, instance):
        command = self.bt_check.text
        if command == 'Check':
            answer = self.text_input_main.text.strip().lower().replace(" ", "")
            if answer == self.word:
                self.label_main.text = 'Right :)'
                self.label_counter.text = self.get_count_verbs()
                self.verb.word_del(self.form)
            else:
                self.label_main.text = f'Wrong: :(\nRight: {self.word}'
            self.bt_check.text = 'Next'
        else:
            self.update_main_page()
            self.bt_check.text = 'Check'
