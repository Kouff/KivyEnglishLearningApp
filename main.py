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


# present = (
#     'be', 'beat', 'become', 'begin', 'bleed', 'blow', 'break', 'bring', 'build',
#     'burn', 'burst', 'buy', 'can', 'catch', 'choose', 'come', 'cost', 'creep', 'cut',
#     'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'fall', 'feed', 'feel',
#     'fight', 'find', 'fit', 'fly', 'forget', 'forgive', 'freeze', 'get', 'give',
#     'go', 'grow', 'hang', 'have', 'hear', 'hide', 'hit', 'hold', 'hurt',
#     'keep', 'kneel', 'know', 'lay', 'lead', 'lean', 'learn', 'leave', 'lend',
#     'let', 'lie', 'light', 'lose', 'make', 'mean', 'meet', 'mistake', 'pay',
#     'prove', 'put', 'quit', 'read', 'ride', 'ring', 'rise', 'run', 'say',
#     'see', 'seek', 'sell', 'send', 'set', 'sew', 'shake', 'show', 'shrink',
#     'shut', 'sing', 'sink', 'sit', 'sleep', 'slide', 'sow', 'speak', 'spell',
#     'spend', 'spill', 'spoil', 'spread', 'spring', 'stand', 'steal', 'stick', 'sting',
#     'sweep', 'swell', 'swim', 'swing', 'take', 'teach', 'tear', 'tell', 'think',
#     'throw', 'understand', 'wake', 'wear', 'weep', 'wet', 'win', 'wind', 'write'
# )
# past_simple = (
#     'was', 'beat', 'became', 'began', 'bled', 'blew', 'broke', 'brought', 'built',
#     'burnt', 'burst', 'bought', 'could', 'caught', 'chose', 'came', 'cost', 'crept', 'cut',
#     'did', 'drew', 'dreamt', 'drank', 'drove', 'ate', 'fell', 'fed', 'felt',
#     'fought', 'found', 'fit', 'flew', 'forgot', 'forgave', 'froze', 'got', 'gave',
#     'went', 'grew', 'hung', 'had', 'heard', 'hid', 'hit', 'held', 'hurt',
#     'kept', 'knelt', 'knew', 'laid', 'led', 'leant', 'learnt', 'left', 'lent',
#     'let', 'lay', 'lit', 'lost', 'made', 'meant', 'met', 'mistook', 'paid',
#     'proved', 'put', 'quit', 'read', 'rode', 'rang', 'rose', 'ran', 'said',
#     'saw', 'sought', 'sold', 'sent', 'set', 'sewed', 'shook', 'showed', 'shrank',
#     'shut', 'sang', 'sank', 'sat', 'slept', 'slid', 'sowed', 'spoke', 'spelt',
#     'spent', 'spilt', 'spoilt', 'spread', 'sprang', 'stood', 'stole', 'stuck', 'stung',
#     'swept', 'swelled', 'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought',
#     'threw', 'understood', 'woke', 'wore', 'wept', 'wet', 'won', 'wound', 'wrote'
# )
# past_participle = (
#     'been', 'beaten', 'become', 'begun', 'bled', 'blown', 'broken', 'brought', 'built',
#     'burnt', 'burst', 'bought', '', 'caught', 'chosen', 'come', 'cost', 'crept', 'cut',
#     'done', 'drawn', 'dreamt', 'drunk', 'driven', 'eaten', 'fallen', 'fed', 'felt',
#     'fought', 'found', 'fit', 'flown', 'forgotten', 'forgiven', 'frozen', 'got', 'given',
#     'gone', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 'held', 'hurt',
#     'kept', 'knelt', 'known', 'laid', 'led', 'leant', 'learnt', 'left', 'lent',
#     'let', 'lain', 'lit', 'lost', 'made', 'meant', 'met', 'mistaken', 'paid',
#     'proven', 'put', 'quit', 'read', 'ridden', 'rung', 'risen', 'run', 'said',
#     'seen', 'sought', 'sold', 'sent', 'set', 'sewn', 'shaken', 'shown', 'shrunk',
#     'shut', 'sung', 'sunk', 'sat', 'slept', 'slid', 'sown', 'spoken', 'spelt',
#     'spent', 'spilt', 'spoilt', 'spread', 'sprung', 'stood', 'stolen', 'stuck', 'stung',
#     'swept', 'swollen', 'swum', 'swung', 'taken', 'taught', 'torn', 'told', 'thought',
#     'thrown', 'understood', 'woken', 'worn', 'wept', 'wet', 'won', 'wound', 'written'
# )
# rus = (
#     'Быть', 'Бить', 'Становиться', 'Начинать', 'Кровоточить', 'Дуть', 'Ломать', 'Приносить',
#     'Строить', 'Гореть', 'Взрываться', 'Покупать', 'Мочь', 'Ловить, хватать, успеть', 'Выбирать',
#     'Приходить', 'Стоить', 'Ползать', 'Резать', 'Делать', 'Рисовать, тащить', 'Мечтать, дремать',
#     'Пить', 'Водить', 'Есть', 'Падать', 'Кормить', 'Чувствовать', 'Бороться', 'Находить',
#     'Подходить по размеру', 'Летать', 'Забывать', 'Прощать', 'Замерзать', 'Получать', 'Давать',
#     'Идти', 'Расти', 'Вешать', 'Иметь', 'Слышать', 'Прятать', 'Попадать в цель', 'Держать',
#     'Причинить боль', 'Держать, хранить', 'Стоять на коленях', 'Знать', 'Класть', 'Вести',
#     'Наклоняться', 'Учить', 'Оставлять', 'Давать взаймы', 'Позволять', 'Лежать', 'Освещать',
#     'Терять', 'Производить', 'Значить', 'Встречать', 'Ошибаться', 'Платить', 'Доказывать',
#     'Положить', 'Покидать, бросать', 'Читать', 'Ездить верхом', 'Звенеть', 'Подниматься', 'Бежать',
#     'Говорить', 'Видеть', 'Искать', 'Продавать', 'Посылать', 'Ставить', 'Шить', 'Встряхивать',
#     'Показывать', 'Сжиматься', 'Закрывать', 'Петь', 'Тонуть', 'Сидеть', 'Спать', 'Скользить',
#     'Сеять', 'Говорить', 'Произносить по буквам', 'Тратить', 'Проливать', 'Портить', 'Расстилать',
#     'Прыгать', 'Стоять', 'Красть', 'Колоть', 'Жалить', 'Выметать', 'Разбухать', 'Плавать', 'Качать',
#     'Брать, взять', 'Учить', 'Рвать', 'Рассказывать', 'Думать', 'Бросать', 'Понимать',
#     'Просыпаться', 'Носить', 'Плакать', 'Мочить', 'Выигрывать', 'Извиваться', 'Писать'
# )
#
#
# class Verb:
#     verbs = []
#
#     def __init__(self, present, past_simple, past_participle, rus):
#         self.words = {'present simple': present, 'past simple': past_simple, 'past participle': past_participle}
#         if not past_participle:
#             self.words.pop('past participle')
#         self.rus = rus
#         Verb.verbs.append(self)
#
#     def get(self):
#         form = choice(list(self.words.keys()))
#         return (form, self.words[form])
#
#     def word_del(self, form):
#         self.words.pop(form)
#         self.check_or_del()
#
#     def check_or_del(self):
#         if not self.words:
#             index = Verb.verbs.index(self)
#             Verb.verbs.pop(index)


class MyApp(App):
    # def init_work_page(self):
    #     self.ti2.text = ''
    #     self.verb = choice(Verb.verbs)
    #     self.form, self.word = self.verb.get()
    #     self.lb2.text = f"{self.verb.rus}\n<{self.form.capitalize()}>"
    #
    # def go_to_work(self, instance):
    #     self.init_work_page()
    #     self.sm.switch_to(self.work_s)
    #
    # def go_to_home(self, instance):
    #     self.sm.switch_to(self.home_s)
    #
    # def next_command(self, instance):
    #     b_text = instance.text
    #     if b_text == 'Check':
    #         answer = self.ti2.text.strip()
    #         if answer == self.word:
    #             self.lb2.text = 'Right :)'
    #             self.verb.word_del(self.form)
    #         else:
    #             self.lb2.text = f'Wrong: :(\nRight: {self.word}'
    #         instance.text = 'Next'
    #     else:
    #         self.init_work_page()
    #         instance.text = 'Check'
    #
    modes_class = (IrregularVerbMode, BaseMode)

    def get_modes(self):
        instances_of_mods = []
        for mode_class in self.modes_class:
            instance = mode_class(self.sm, self.home_screen)
            instances_of_mods.append(instance)
        return instances_of_mods

    def add_mode_buttons(self, layout):
        for mode in self.get_modes():
            bt = Button(text=mode.name)
            bt.bind(on_release=mode.go_to_settings_page)
            layout.add_widget(bt)

    def create_home_page(self):
        self.home_screen = Screen(name="home")
        bl1 = BoxLayout(orientation='vertical', padding=(20, 40, 20, 40))
        lb1 = Label(text="Home")
        gl = GridLayout(cols=2)
        bl1.add_widget(lb1)
        self.add_mode_buttons(gl)
        xxx = self.get_modes()

        bt = Button(text=xxx[0].name)
        bt.bind(on_press=xxx[0].go_to_settings_page)
        gl.add_widget(bt)

        bl1.add_widget(gl)
        self.home_screen.add_widget(bl1)

        self.sm.add_widget(self.home_screen)

    #
    # def create_work_page(self):
    #     work_s = Screen(name="work")
    #     self.work_s = work_s
    #     bl2 = BoxLayout(orientation='vertical', padding=(10, 0, 10, 30))
    #     ti2 = TextInput(font_size=self.font_size)
    #     self.ti2 = ti2
    #     lb2 = Label(text="work", font_size=self.font_size)
    #     self.lb2 = lb2
    #     b2 = Button(text="Check", font_size=self.font_size)
    #     b2.bind(on_press=self.next_command)
    #     bl2.add_widget(ti2)
    #     bl2.add_widget(lb2)
    #     bl2.add_widget(b2)
    #     work_s.add_widget(bl2)
    #
    #     self.sm.add_widget(work_s)

    def build(self):
        # self.font_size = 32

        self.sm = ScreenManager(transition=RiseInTransition())
        self.create_home_page()

        self.sm.current = 'home'
        return self.sm


if __name__ == "__main__":
    # from kivy.core.window import Window
    from kivy.config import Config

    # x, y = 1080, 2340
    # Window.size = update_size(x, y)
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    # for p, ps, pp, r in zip(present, past_simple, past_participle, rus):
    #     Verb(p, ps, pp, r)
    MyApp().run()
