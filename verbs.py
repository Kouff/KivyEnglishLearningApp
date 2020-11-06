from random import choice

present = {
    'Low': (
        'be', 'become', 'build', 'buy', 'can', 'come', 'cut', 'do', 'drink', 'drive', 'eat', 'fight', 'find', 'fly',
        'get', 'give', 'go', 'have', 'hear', 'know', 'learn', 'leave', 'let', 'lose', 'make', 'mean', 'meet', 'pay',
        'put', 'quit', 'read', 'ride', 'run', 'say', 'see', 'show', 'sit', 'sleep', 'speak', 'stand', 'teach', 'tell',
        'wear', 'write'
    ),
    'Middle': (
        'begin', 'break', 'bring', 'catch', 'choose', 'cost', 'dream', 'fall', 'feed', 'feel', 'fit', 'forget',
        'forgive', 'freeze', 'grow', 'hang', 'hide', 'hit', 'hold', 'keep', 'lay', 'lead', 'lean', 'lie', 'light',
        'mistake', 'ring', 'rise', 'sell', 'send', 'shake', 'shut', 'sing', 'sink', 'spend', 'spring', 'steal', 'swim',
        'take', 'think', 'understand', 'wake', 'win'
    ),
    'High': (
        'beat', 'bleed', 'blow', 'burn', 'burst', 'creep', 'draw', 'hurt', 'kneel', 'lend', 'prove', 'seek', 'set',
        'sew', 'shrink', 'slide', 'sow', 'spell', 'spill', 'spoil', 'spread', 'stick', 'sting', 'sweep', 'swell',
        'swing', 'tear', 'throw', 'weep', 'wet', 'wind'
    )
}
past_simple = {
    'Low': (
        'was', 'became', 'built', 'bought', 'could', 'came', 'cut', 'did', 'drank', 'drove', 'ate', 'fought', 'found',
        'flew', 'got', 'gave', 'went', 'had', 'heard', 'knew', 'learnt', 'left', 'let', 'lost', 'made', 'meant', 'met',
        'paid', 'put', 'quit', 'read', 'rode', 'ran', 'said', 'saw', 'showed', 'sat', 'slept', 'spoke', 'stood',
        'taught', 'told', 'wore', 'wrote'
    ),
    'Middle': (
        'began', 'broke', 'brought', 'caught', 'chose', 'cost', 'dreamt', 'fell', 'fed', 'felt', 'fit', 'forgot',
        'forgave', 'froze', 'grew', 'hung', 'hid', 'hit', 'held', 'kept', 'laid', 'led', 'leant', 'lay', 'lit',
        'mistook', 'rang', 'rose', 'sold', 'sent', 'shook', 'shut', 'sang', 'sank', 'spent', 'sprang', 'stole', 'swam',
        'took', 'thought', 'understood', 'woke', 'won'
    ),
    'High': (
        'beat', 'bled', 'blew', 'burnt', 'burst', 'crept', 'drew', 'hurt', 'knelt', 'lent', 'proved', 'sought', 'set',
        'sewed', 'shrank', 'slid', 'sowed', 'spelt', 'spilt', 'spoilt', 'spread', 'stuck', 'stung', 'swept', 'swelled',
        'swung', 'tore', 'threw', 'wept', 'wet', 'wound'
    )
}
past_participle = {
    'Low': (
        'been', 'become', 'built', 'bought', '', 'come', 'cut', 'done', 'drunk', 'driven', 'eaten', 'fought', 'found',
        'flown', 'got', 'given', 'gone', 'had', 'heard', 'known', 'learnt', 'left', 'let', 'lost', 'made', 'meant',
        'met', 'paid', 'put', 'quit', 'read', 'ridden', 'run', 'said', 'seen', 'shown', 'sat', 'slept',
        'spoken', 'stood', 'taught', 'told', 'worn', 'written'
    ),
    'Middle': (
        'begun', 'broken', 'brought', 'caught', 'chosen', 'cost', 'dreamt', 'fallen', 'fed', 'felt', 'fit', 'forgotten',
        'forgiven', 'frozen', 'grown', 'hung', 'hidden', 'hit', 'held', 'kept', 'laid', 'led', 'leant', 'lain', 'lit',
        'mistaken', 'rung', 'risen', 'sold', 'sent', 'shaken', 'shut', 'sung', 'sunk', 'spent', 'sprung', 'stolen',
        'swum',
        'taken', 'thought', 'understood', 'woken', 'won'
    ),
    'High': (
        'beaten', 'bled', 'blown', 'burnt', 'burst', 'crept', 'drawn', 'hurt', 'knelt', 'lent', 'proven', 'sought',
        'set', 'sewn', 'shrunk', 'slid', 'sown', 'spelt', 'spilt', 'spoilt', 'spread', 'stuck', 'stung', 'swept',
        'swollen', 'swung', 'torn', 'thrown', 'wept', 'wet', 'wound'
    )
}
rus = {
    'Low': (
        'Быть', 'Становиться', 'Строить', 'Покупать', 'Мочь', 'Приходить', 'Резать', 'Делать', 'Пить', 'Водить', 'Есть',
        'Бороться', 'Находить', 'Летать', 'Получать', 'Давать', 'Идти', 'Иметь', 'Слышать', 'Знать',
        'Учить самостоятельно',
        'Оставлять', 'Позволять', 'Терять', 'Производить', 'Значить', 'Встречать', 'Платить', 'Положить',
        'Покидать, бросать', 'Читать', 'Ездить верхом', 'Бежать', 'Говорить', 'Видеть', 'Показывать', 'Сидеть', 'Спать',
        'Разговаривать', 'Стоять', 'Учить, преподовать', 'Рассказывать', 'Носить', 'Писать'
    ),
    'Middle': (
        'Начинать', 'Ломать', 'Приносить', 'Ловить, хватать, успеть', 'Выбирать', 'Стоить', 'Мечтать, дремать',
        'Падать', 'Кормить', 'Чувствовать', 'Подходить по размеру', 'Забывать', 'Прощать', 'Замерзать', 'Расти',
        'Вешать', 'Прятать', 'Попадать в цель', 'Держать', 'Держать, хранить', 'Класть', 'Вести', 'Наклоняться',
        'Лежать', 'Освещать', 'Ошибаться', 'Звенеть', 'Подниматься', 'Продавать', 'Посылать', 'Встряхивать',
        'Закрывать', 'Петь', 'Тонуть', 'Тратить', 'Прыгать', 'Красть', 'Плавать', 'Брать, взять', 'Думать', 'Понимать',
        'Просыпаться', 'Выигрывать'
    ),
    'High': (
        'Бить', 'Кровоточить', 'Дуть', 'Гореть', 'Взрываться', 'Ползать', 'Рисовать, тащить', 'Причинить боль',
        'Стоять на коленях', 'Давать взаймы', 'Доказывать', 'Искать', 'Ставить', 'Шить', 'Сжиматься', 'Скользить',
        'Сеять', 'Произносить по буквам', 'Проливать', 'Портить', 'Расстилать', 'Колоть', 'Жалить', 'Выметать',
        'Разбухать', 'Качать', 'Рвать', 'Бросать', 'Плакать', 'Мочить', 'Извиваться'
    )
}


class IrregularVerb:
    verbs = []

    def __init__(self, present, past_simple, past_participle, rus):
        self.words = {'present simple': present, 'past simple': past_simple, 'past participle': past_participle}
        if not past_participle:
            self.words.pop('past participle')
        self.rus = rus
        IrregularVerb.verbs.append(self)

    def get(self):
        form = choice(list(self.words.keys()))
        return (form, self.words[form])

    def word_del(self, form):
        self.words.pop(form)
        self.check_or_del()

    def check_or_del(self):
        if not self.words:
            index = IrregularVerb.verbs.index(self)
            IrregularVerb.verbs.pop(index)

# For testing
# for x1, x2, x3, x4 in zip(present, past_simple, past_participle, rus):
#     print(x1, x2, x3, x4)
#     print(len(present[x1]), len(past_simple[x2]), len(past_participle[x3]), len(rus[x4]))
#     for z1, z2, z3, z4 in zip(present[x1], past_simple[x2], past_participle[x3], rus[x4]):
#         print(z1, z2, z3, z4)
#         print()
#
#     print('----------------------------------------')
