from random import choice, shuffle

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

low_level_regular_verbs = {'kiss': 'целовать', 'love': 'любить', 'work': 'работать', 'live': 'жить', 'add': 'добавлять',
                           'agree': 'соглашаться',
                           'answer': 'ответить', 'approve': 'утвердить', 'ask': 'просить', 'balance': 'балансировать',
                           'battle': 'сражаться', 'call': 'называть', 'change': 'изменять', 'check': 'проверять',
                           'clean': 'чистить', 'close': 'закрывать', 'coach': 'тренировать',
                           'connect': 'подключать', 'continue': 'продолжать', 'copy': 'копировать',
                           'correct': 'корректировать', 'count': 'считать', 'cry': 'плакать', 'dance': 'танцевать',
                           'depend': 'зависеть', 'develop': 'развивать', 'discover': 'обнаружить', 'divide': 'делить',
                           'double': 'удваивать', 'dream': 'мечтать', 'dress': 'одевать', 'drop': 'падать',
                           'dry': 'сушить', 'dust': 'пылить', 'empty': 'опорожнять', 'end': 'заканчивать',
                           'enjoy': 'наслаждаться', 'enter': 'входить', 'escape': 'бежать',
                           'exist': 'существовать', 'fear': 'бояться', 'fill': 'заполнять', 'fix': 'чинить',
                           'flood': 'затопить', 'fool': 'обманывать', 'guard': 'охранять', 'hate': 'ненавидеть',
                           'help': 'помогать', 'hope': 'надеяться', 'hug': 'обнимать',
                           'hunt': 'охотиться', 'ignore': 'игнорировать', 'include': 'включать', 'invite': 'приглашать',
                           'join': 'вступать', 'jump': 'прыгать', 'kick': 'пинать', 'laugh': 'смеяться',
                           'launch': 'запускать', 'like': 'нравиться', 'listen': 'слушать',
                           'load': 'грузить', 'lock': 'запирать', 'look': 'посмотреть', 'manage': 'управлять',
                           'move': 'двигаться', 'multiply': 'умножить', 'name': 'называть', 'need': 'нуждаться',
                           'number': 'нумеровать', 'observe': 'наблюдать', 'offer': 'предлагать',
                           'milk': 'доить', 'mine': 'добывать', 'miss': 'скучать', 'mix': 'смешивать',
                           'open': 'открыть', 'order': 'заказывать', 'own': 'владеть', 'paint': 'покрасить',
                           'paste': 'вставить', 'pause': 'приостанавливаться', 'play': 'играть',
                           'point': 'указывать', 'press': 'нажимать', 'print': 'печатать', 'pull': 'тянуть',
                           'push': 'толкать', 'race': 'мчаться', 'raise': 'поднимать', 'record': 'записывать',
                           'relax': 'расслабляться', 'remember': 'помнить', 'remove': 'удалять',
                           'repeat': 'повторять', 'replace': 'заменять', 'reply': 'отвечать', 'report': 'доклад',
                           'request': 'запрашивать', 'return': 'возвращать', 'save': 'сохранять', 'scream': 'кричать',
                           'search': 'искать', 'share': 'делиться', 'skip': 'пропускать',
                           'smile': 'улыбаться', 'spray': 'опрыскивать', 'start': 'начинать', 'stay': 'оставаться',
                           'step': 'шагать', 'stop': 'остановить', 'strip': 'раздевать', 'support': 'поддерживать',
                           'surprise': 'удивлять', 'suspect': 'подозревать', 'suspend': 'приостанавливать',
                           'switch': 'переключать', 'talk': 'говорить', 'taste': 'пробовать', 'thank': 'благодарить',
                           'touch': 'касаться', 'trade': 'торговать', 'travel': 'путешествовать',
                           'trouble': 'беспокоить', 'try': 'пытаться', 'trust': 'доверять', 'twist': 'крутить',
                           'unlock': 'разблокировать', 'unpack': 'распаковывать', 'use': 'пользоваться',
                           'visit': 'посещать', 'wait': 'ждать', 'walk': 'ходить', 'want': 'хотеть',
                           'warm': 'согревать', 'wash': 'мыть', 'watch': 'смотреть', 'welcome': 'приветствовать',
                           'wipe': 'протирать', 'worry': 'беспокоиться', 'yell': 'кричать', 'zip': 'застегивать',
                           'zoom': 'увеличить'}
# middle_level_regular_verbs = {'': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
#                               '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
#                               '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
#                               '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
#                               '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
#                               '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': ''}
subjects = {'I': 'я', 'you': 'ты', 'he': 'он', 'she': 'она', 'we': 'мы', 'they': 'они'}


class SentenceBuilder:
    x = ('future', 'present', 'past')
    y = ('negative', 'affirmative', 'interrogative')
    vowels = ('e', 'i', 'o', 'a', 'u', 'y')

    def __init__(self, level=None):
        self.level = level

    def build_sentence(self):
        sentence_form = getattr(self, f'{choice(self.x)}_{choice(self.y)}')
        verb = self.get_random_verb()
        subject = choice(list(subjects.keys()))
        result = sentence_form((verb, low_level_regular_verbs[verb]), (subject, subjects[subject]))
        result.update({'world_variants': self.get_word_variants(verb, subject)})
        return result

    def get_random_verb(self):
        # if self.level == 'Low':
        #     pass
        verb = choice(list(low_level_regular_verbs.keys()))
        return verb

    def get_word_variants(self, verb, subject):
        variants = ['will', 'not', 'did', 'do', 'does', subject, verb, self.get_past_verb(verb),
                    self.get_verb_for_he_she(verb)]
        shuffle(variants)
        return variants

    def get_present_do(self, subject):
        if subject in ('he', 'she'):
            return 'does'
        return 'do'

    def get_past_verb(self, verb):
        if verb.endswith('e'):
            return verb + 'd'
        elif verb[-2] not in self.vowels and verb[-1] == 'y':
            return verb[:-1] + 'ied'
        elif len(verb) > 2 and verb[-3] not in self.vowels and verb[-2] in ('i', 'o', 'a', 'u',) and verb[
            -3] not in self.vowels:
            return verb + verb[-1] + 'ed'
        return verb + 'ed'

    def get_verb_for_he_she(self, verb):
        if verb[-2] not in self.vowels and verb[-1] == 'y':
            return verb[:-1] + 'ies'
        elif verb[-1] in ('o', 's', 'x', 'z') or verb.endswith('sh') or verb.endswith('ch') or verb.endswith('tch'):
            return verb + 'es'
        return verb + 's'

    def get_rus_verb(self, time, verb):
        if time == 'future':
            pass

    def get_rus_will(self, subject):
        if subject == 'я':
            return 'буду'
        elif subject == 'ты':
            return 'будешь'
        elif subject == 'мы':
            return 'будем'
        elif subject == 'они':
            return 'будут'
        elif subject in ('он', 'она'):
            return 'будет'
        return 'буду'

    def future_negative(self, verb, subject):  # 1 -
        eng_sentence = f'{subject[0]} will not {verb[0]}.'
        rus_sentence = f'{subject[1]} не {self.get_rus_will(subject[1])} {verb[1]}.'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def future_affirmative(self, verb, subject):  # 1 +
        eng_sentence = f'{subject[0]} will {verb[0]}.'
        rus_sentence = f'{subject[1]} {self.get_rus_will(subject[1])} {verb[1]}.'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def future_interrogative(self, verb, subject):  # 1 ?
        eng_sentence = f'will {subject[0]} {verb[0]}?'
        rus_sentence = f'{subject[1]} {self.get_rus_will(subject[1])} {verb[1]}?'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def present_negative(self, verb, subject):  # 0 -
        eng_sentence = f'{subject[0]} {self.get_present_do(subject[0])} not {verb[0]}.'
        rus_sentence = f'{subject[1]} не {verb[1]}. (Текущее)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def present_affirmative(self, verb, subject):  # 0 +
        v = verb[0]
        if subject[0] in ('she', 'he'):
            v = self.get_verb_for_he_she(v)
        eng_sentence = f'{subject[0]} {v}.'
        rus_sentence = f'{subject[1]} {verb[1]}. (Текущее)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def present_interrogative(self, verb, subject):  # 0 ?
        eng_sentence = f'{self.get_present_do(subject[0])} {subject[0]} {verb[0]}?'
        rus_sentence = f'{subject[1]} {verb[1]}? (Текущее)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def past_negative(self, verb, subject):  # -1 -
        eng_sentence = f'{subject[0]} did not {verb[0]}.'
        rus_sentence = f'{subject[1]} не {verb[1]}. (Прошлое)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def past_affirmative(self, verb, subject):  # -1 +
        eng_sentence = f'{subject[0]} {self.get_past_verb(verb[0])}.'
        rus_sentence = f'{subject[1]} {verb[1]}. (Прошлое)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

    def past_interrogative(self, verb, subject):  # -1 ?
        eng_sentence = f'did {subject[0]} {verb[0]}?'
        rus_sentence = f'{subject[1]} {verb[1]}? (Прошлое)'
        return {'eng': eng_sentence, 'rus': rus_sentence.capitalize()}

# она будет любить / она не будет любить /
# она любит / она не любит
# она любила / она не любила
