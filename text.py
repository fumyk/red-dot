good = 'Правильно !'
good_pic = '/static/yes.jpg'

text_0 = 'Кот Матроскин, прибывший в Бердск прямо из деревни Простоквашино, хочет купить себе новый компьютер и узнать намного больше о мире информатики и современных технологиях. Но только вот в чем проблема, Кот Матроскин совсем не знает, как ему выбрать современный компьютер и ничего не знает об информатике. Помоги ему сделать правильный выбор!'
text_1 = 'Кот Матроскин решил отдохнуть после долгого пути и отправился гулять по площади. "Но стоит не забывать зачем я сюда приехал!", - сказал Кот Матроскин.'
text_3 = '''Придя в магазин у кота Матроскина сразу же разбежались глаза.Он попытался разобраться сам, где что лежит, однако его попытки оказались напрасны, ведь в его деревне нет компьютеров.
Тут к Матроскиеу подходит продавец и спрашивает: "Вам помочь?"'''
text_4 = 'Я являюсь консультантом этого магазина и хочу вам помочь. Мы можем собрать новенький отличный компьютер, если вы сможете разгадать мои загадки, вы готовы?'
text_5 = '''Чтоб работа закипела,<br>
Чтобы диски ты смотрел,<br>
Чтоб без связи не сидел,<br>
Чтоб компьютер нам помог,<br>
Должен быть…'''
text_7 = '''Что же такое системный блок?
В своей практике, каких только определений системного блока я не слышал, его называли и процессором, и железной коробкой, и даже вон той штукой под столом, было ещё много разных названий – всех и не вспомню.

На самом деле, действительно, во всех этих «определениях» есть доля правды, в системном блоке находится процессор, системный блок железный и, в конце концов, он в большинстве случаев стоит под столом или рядом со столом.

А вот энциклопедическое определение системного блока звучит так:
системный блок — корпус, в котором находятся основные функциональные компоненты персонального компьютера. Корпуса обычно созданы из деталей на основе стали, алюминия и пластика, также иногда используются такие материалы как дерево или органическое стекло.'''
text_8 = 'Процессор – это главная микросхема компьютера. Он выполняет программный код, находящийся в памяти и руководит работой всех устройств компьютера. Чем выше скорость работы процессора, тем выше быстродействие компьютера.'
text_9 = '''В корпусе компьютера<br>
Она проживает.<br>
Преобразовать<br>
Изображение помогает.<br>
В видеосигнал<br>
Для монитора превращает.<br>
Ты ее узнал?<br>
Ну, как ее называют?'''
text_10 = '''Видеокарта – это устройство, преобразующее изображение, находящееся в памяти компьютера, в видеосигнал для монитора. Обычно видеокарта является платой расширения и вставляется в специальный разъём для видеокарт на материнской плате, но бывает и интегрированной.'''
text_11 = '''Жесткий диск так называют.<br>
Кто название отгадает?<br>
Копятся данные в этом устройстве,<br>
Запоминать — его главное свойство.'''
text_15 = '''Материнская плата (еще ее называют системная, главная плата) – многослойная печатная плата, к ней подключаются все элементы компьютера: жесткий диск, процессор, оперативная память, видеокарта, оптический привод и другие устройства. Устанавливается материнская плата внутри системного блока. Основная задача материнской платы - объединение и обеспечение совместной работы всех комплектующих компьютера.'''
text_pref = '''Вот ты и собрал компьютер. Поздравляю! Но как же ты будешь на нем работать без необходимой гарнитуры ? Вот тебе еще загадка - отгадаешь и я тебе расскажу кое-что...<br>
На ней кнопок очень много<br>
Алфавит и цифры есть<br>
Чтобы слово написать,<br>
Нужно кнопки нажимать. '''
text_kb = '''Клавиатура – это устройство для ввода данных в компьютер: букв, цифр и знаков. Также используется для управления системой, то есть является аналогом компьютерной мыши. По типу соединения она бывает проводной и беспроводной.<br>
Молодец. Отгадал. Но это еще не конец...<br>
Бегает по коврику,<br>
Курсором управляет,<br>
Нажатием на кнопку<br>
Программы открывает'''
text_mouse = '''Компьютерная мышь – механическое устройство, манипулятор, трансформирующий движение в управляющий сигнал.'''
text_final = '''Молодец, ты правильно отгадал все загадки и смог собрать себе компьютер. А мне надо идти. - сказал консультант и растворился в дали...
<br><br>
<i>Ура я наконец-то собрал себе компьютер и кое-что узнал о информатике. Спасибо, что помог мне с этими непростыми заданиями. До скорых встреч, а я дальше пошел изучать инфоматику!</i>'''

txt = {
    0: {
        'divs': {'Пойти в магазин техники': 2, 'Пойти гулять по улице': 1},
        'h': 'Прибытие',
        'text': text_0,
        'pic_path': '/static/0.jpg'
    },
    1: {
        'divs': {'Пойти в магазин техники': 2},
        'h': 'На прогулке',
        'text': text_1,
        'pic_path': '/static/1.jpg'
    },
    2: {
        'divs': {'Продолжить путь': 3},
        'h': 'На пути в магазин',
        'text': 'Кот Матроскин решает отправиться в магазин DNS на Универмаге в городе Бердске и купить себе компьютер.',
        'pic_path': '/static/2.jpg'
    },
    3: {
        'divs': {'Попросить помощи': 4},
        'h': 'В магазине',
        'text': text_3,
        'pic_path': '/static/3.jpg'
    },
    4: {
        'divs': {'Хорошо, давай свои загадки': 5},
        'h': 'Разговор с продавцом',
        'text': text_4,
        'pic_path': good_pic
    },
    5: {
        'divs': {'Калейдоскоп': 99, 'Системный блок': 6, 'Алмазный блок': 99},
        'h': 'Загадка',
        'text': text_5,
        'pic_path': good_pic
    },
    6: {
        'divs': {'Давай следущую загадку!': 7},
        'h': good,
        'text': text_7,
        'pic_path': '/static/corpus.jpeg'
    },
    7: {
        'divs': {'Мотор': 99, 'Жесткий диск': 99, 'Процессор': 8},
        'h': 'Ещё одна загадка...',
        'text': 'А знаешь ли ты, что называют мозгом компьютера ?',
        'pic_path': good_pic
    },
    8: {
        'divs': {'Что дальше ?': 9},
        'h': good,
        'text': text_8,
        'pic_path': '/static/cp.jpg'
    },
    9: {
        'divs': {'Видеокарта': 10, 'Процессор': 99, 'Телевизор': 99},
        'h': 'Ещё одна сложная загадка...',
        'text': text_9,
        'pic_path': good_pic
    },
    10: {
        'divs': {'Что там дальше?': 11},
        'h': good,
        'text': text_10,
        'pic_path': '/static/videocard.jpg'
    },
    11: {
        'divs': {'Дискета': 99, 'Винчестер': 12, 'Вирус': 99},
        'h': 'Вопрос так вопрос!',
        'text': text_11,
        'pic_path': good_pic
    },
    12: {
        'divs': {'Давай следущую загадку!': 13},
        'h': good,
        'text': 'Винчестер (жёсткий диск) — накопитель информации основанный на магнитных пластинах и эффекте магнетизма.',
        'pic_path': '/static/hard.jpg'
    },
    13: {
        'divs': {'Оперативная память': 14, 'Дискета': 99, 'Жесткий диск': 99},
        'h': 'Хм...',
        'text': 'Какое устройство очищает все свои данные после перезагрузки ?',
        'pic_path': good_pic
    },
    14: {
        'divs': {'Что дальше ?': 15},
        'h': good,
        'text': 'Оперативная память - это временная память компьютера, которая работает при включенном состоянии компьютера и которая нужна для нормальной работы программ и процессов.',
        'pic_path': '/static/ram.png'
    },
    15: {
        'divs': {'Скотч': 99, 'Провода': 99, 'Материнская плата': 16},
        'h': 'Что же это...',
        'text': 'Чтобы объединить все эти устройства нужна одна очень важная деталь. Знаешь что это ?',
        'pic_path': good_pic
    },
    16: {
        'divs': {'Как много частей в компьютере...': 17},
        'h': good,
        'text': text_15,
        'pic_path': '/static/mom.jpg'
    },
    17: {
        'divs': {'Книга': 99, 'Кубик Рубика': 99, 'Клавиатура': 18},
        'h': 'Системный блок готов!',
        'text': text_pref,
        'pic_path': '/static/pref.jpg'
    },
    18: {
        'divs': {'Енот': 99, 'Мышь': 19, 'Перо': 99},
        'h': 'Клавиатура',
        'text': text_kb,
        'pic_path': '/static/kb.jpg'
    },
    19: {
        'divs': {'Понял! Что дальше?': 20},
        'h': 'Мышь',
        'text': text_mouse,
        'pic_path': '/static/mouse.jpg'
    },
    20: {
        'divs': {'Мелодия': 99, 'Миниган': 99, 'Монитор': 21},
        'h': 'Ребус!',
        'text': 'Тебе нужно ещё кое-что очень важное. Разгадай ребус и узнаешь что это!',
        'pic_path': '/static/rebus-monic.jpg'
    },
    21: {
        'divs': {'Уф, как много всего': 22},
        'h': 'Монитор',
        'text': 'Правильно, это монитор. Мы с тобой понимаем, что без него системный блок будет просто железкой.',
        'pic_path': '/static/monitor.jpg'
    },
    22: {
        'divs': {},
        'h': 'Поздравляю!',
        'text': text_final,
        'pic_path': '/static/final.jpg'
    },
    99: {
        'divs': {'Начать сначала': 0},
        'h': 'О нет! Ты ошибся!',
        'text': '',
        'pic_path': '/static/error.png'
    }
}


def generate_buttons(buttons):
    final = '<div id="button-box">'
    for k, v in buttons.items():
        final += '<button onclick="getAjaxData({})" class="mui-btn mui-btn--raised mui-btn--primary">{}</button>'.format(v, k)
        if k == 'Начать сначала':
            final = final.replace('primary', 'danger')
    return final + '</div>'


def generate_main_container(level_id):
    return '''
<div id="main-container">
    <h1>Приключение кота Матроскина</h1>
    <h2 id="lvl-name">{}</h2>
    <img src="{}">
    <div id="main-text">{}</div>
    <div id="button-box">{}</div>
</div>'''.format(txt[level_id]['h'],
                 txt[level_id]['pic_path'],
                 txt[level_id]['text'],
                 generate_buttons(txt[level_id]['divs']))
