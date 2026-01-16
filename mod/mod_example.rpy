## Персонажи
define polina = Character(_("{color=#51CA80}Пол{/color}{color=#CA76F0}ина{/color}"),
    who_font="fonts/blogger-sans.bold.otf",
    what_font="fonts/blogger-sans.light.otf",
    who_prefix="",
    who_suffix="",
    what_prefix="{color=#4578f6}",
    what_suffix="{/color}")
define nadya = Character(_("{color=#C41B20}Надежда{/color}"),
    who_font="fonts/blogger-sans.bold.otf",
    what_font="fonts/blogger-sans.light.otf",
    who_prefix="",
    who_suffix="",
    what_prefix="{color=#4578f6}",
    what_suffix="{/color}")
define diana = Character(_("{color=#FF8AAB}Диана{/color}"),
    who_font="fonts/blogger-sans.bold.otf",
    what_font="fonts/blogger-sans.light.otf",
    who_prefix="",
    who_suffix="",
    what_prefix="{color=#4578f6}",
    what_suffix="{/color}")

default points=1 
default plus=2
default max_point=200
default clicked = False 

default audio.polina_end = "another_attempt/audio/polina_end.mp3"
define audio.dianabambam = "another_attempt/audio/dianabambam.mp3"
define audio.tuntunsahur = "another_attempt/audio/sound/stuk_serdca_-_zvuk_serdcebieniya.mp3"
define audio.gorod = "another_attempt/audio/birds-singing.mp3"

## Спрайты
init -1:

    image polina1 = "another_attempt/images/polina/polina_angry.png"
    image polina2 = "another_attempt/images/polina/polina_default.png"
    image polina3 = "another_attempt/images/polina/polina_sad.png"
    image polina4 = "another_attempt/images/polina/polina_scary.png"
    image polina5 = "another_attempt/images/polina/polina_sleep.png"
    image polina6 = "another_attempt/images/polina/polina_smile.png"
    image polina7 = "another_attempt/images/polina/polina_myxaxa.png"
    image polina8 = "another_attempt/images/polina/poina_disgust.png"

    image nadya1 = "another_attempt/images/nadya/nadya_default.png"
    image nadya2 = "another_attempt/images/nadya/nadya_blush.png"
    image nadya3 = "another_attempt/images/nadya/nadya_angry.png"
    image nadya4 = "another_attempt/images/nadya/nadya_shok.png"
    image nadya5 = "another_attempt/images/nadya/nadya_sad.png"
    image nadya6 = "another_attempt/images/nadya/nadya_nervos.png"

    image diana1 = "another_attempt/images/diana/diana_default.png"
    image diana2 = "another_attempt/images/diana/diana_shine.png"
    image diana3 = "another_attempt/images/diana/diana_shok.png"
    image diana4 = "another_attempt/images/diana/diana_smile.png"
    image diana5 = "another_attempt/images/diana/diana_sad.png"
    image diana6 = "another_attempt/images/diana/diana_angry.png"
    image diana7 = "another_attempt/images/diana/diana_mockery.png"
    image diana8 = "another_attempt/images/diana/diana_nervous.png"

    image cg-dianaandskoof = "another_attempt/images/diana/cg-dianaandskoof.png"
    image cg-polinaandskoof = "another_attempt/images/polina/cg-polinaandskoof.png"
    image cg-nadyaandskoof = "another_attempt/images/nadya/cg-nadyaandskoof.png"
    image cg-nygdegeruchki = Animation("another_attempt/images/diana/cg-ruchki.png", 0.5, "another_attempt/images/diana/cg-ruchkiblack.png", 0.5)

    image pet = "another_attempt/images/diana/pet_idle_1.png"
    image barelement = "another_attempt/images/diana/bar_empty.png"

    image achievements_byebyepolina = "another_attempt/images/achievements/byebyepolina.png" #1
    image achievements_byebyetanki = "another_attempt/images/achievements/byebyetanki.png" #2
    image achievements_face = "another_attempt/images/achievements/face.png" #3
    image achievements_money = "another_attempt/images/achievements/money.png" #4
    image achievements_motobrat = "another_attempt/images/achievements/motobrat.png" #5
    image achievements_mydak = "another_attempt/images/achievements/mydak.png" #6
    image achievements_mynashechka = "another_attempt/images/achievements/mynashechka.png" #7
    image achievements_speed = "another_attempt/images/achievements/speed.png" #8
    image achievements_typ = "another_attempt/images/achievements/typ.png" #9 
    image achievements_ymn = "another_attempt/images/achievements/ymn.png" #10

    $ goscsay = False
    $ nadyafalse = False
    $ ochkoskoofa = 0 
    $ brainsturm = 0
    $ achievements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


init -1 python:   

    style.timediana = Style(style.default)
    style.timediana.left_bar = Frame("another_attempt/images/diana/bar_full.png", 1,0)
    style.timediana.right_bar = Frame("another_attempt/images/diana/bar_empty.png", 1,0)
    style.timediana.xmaximum = 1084
    style.timediana.ymaximum = 257

screen klicker:
    modal True

    timer 0.5 repeat True action If(time <= 0, Jump("mod_ending_diana_5"), [SetVariable("points", points - 1), SetVariable("time", time - 1)])

    button:
        xpos .3
        ypos .1
        xysize(1920, 1080)
        action [SetVariable("points", points + plus), Play("audio", "another_attempt/audio/sound/xamster.mp3"), If(points >= max_point, true=Jump("mod_ending_diana_4"))]

    bar:
        style "timediana"
        value time
        range time_range
        xalign 0.5 yalign 0.15
 
## Регистрация аддона
init -5 python:
    ## Dev. tip: Объявление объекта аддон. Название мода ни на что не влияет.
    another_attempt_set = AddonData("Another attempt")
    
    ## Dev. tip: Лейблы, которые будут использованы для отрисовки, перерисовки, и затирания альтушек.
    another_attempt_set.setDraw(
        on_enter = "mod_draw_enter",
        on_leave = "mod_draw_leave",
        on_redraw = "mod_draw_redraw")

    ## Dev. tip: Лейбл, который будет использован для разговоров.
    another_attempt_set.setTalk("mod_talk")

    ## Dev. tip: Лейблы, настраивающие кнопки.
    another_attempt_set.setIntroItems("mod_intro_items")
    another_attempt_set.setChoiceItems("mod_choice_items")

    ## Dev. tip: Лейбл, который будет вызван для демонстрации титров.
    another_attempt_set.setTitles("mod_titles")

    ## Dev. tip: Опциональный лейбл, который будет вызыватся при начале новой игры.
    another_attempt_set.setReset("mod_reset")
    
    ## Dev. tip: Регистрация аддона в системе.
    addon_manager.addAddon(another_attempt_set)

## Лейблы аддона
label mod_reset:
    ## Dev. tip: Этот лейбл вызывается, если игрок нажмёт "начать заново" во время прохождения мода. Если мод использует кастомные скрины, здесь их можно убрать.
    return

label mod_draw_enter:
    ## Dev. tip: Этот лейбл вызывается при открытии страницы мода.

    scene expression "uslugi/bg-su.png"
    if goscsay:
        jump mod_draw_redraw
    show diana1:
        align (0.15, 2.5)
    show nadya1:
        align (0.5, 1.0)
    show polina2:
        align (0.85, 1.9)
    with dissolve 
    play audio "another_attempt/audio/voice_inner/audio1.flac"
    inner "ОГО, ЕЩЁ АЛЬТУШКИ!!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio1.flac"
    skoof "Они выглядят... необычнее, чем прошлые."
    play audio "another_attempt/audio/voice_inner/audio2.flac"
    inner "НУ ЧТО ТЫ ТЯНЕШЬ, ДАВАЙ БЫСТРЕЕ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio2.flac"
    skoof "Что ж, узнаем и про этих молодых особ."
    play audio "another_attempt/audio/voice_skoof/audio3.flac"
    skoof "Точно хочу себе одну из них."
    $ goscsay = True
    return

label mod_draw_leave:
    ## Dev. tip: Этот лейбл вызывается когда игрок уходит со страницы мода.

    scene expression "uslugi/bg-su.png" with dissolve
    return

label mod_draw_redraw:
    ## Dev. tip: Этот лейбл вызывается пока игрок находится на странице мода.

    show diana1:
        align (0.15, 2.5)
        linear .25 zoom 1.0
    show nadya1:
        align (0.5, 1.0)
        linear .25 zoom 1.0
    show polina2:
        align (0.85, 1.9)
        linear .25 zoom 1.0

    return

###
# Формат для добавления кнопок:
# $ items.append( (caption, label) )
# где
# caption - текст кнопки
# label - лейбл, на который будет совершен прыжок при выборе этой опции
###
label mod_intro_items:
    ## Dev. tip: История продолжится, только если items останется пустой. Предполагается, что это будет только после того, как будут просмотрены все альтушки.
    ## act2_alts_checked - переменная типа set, которая обнуляется перед выбором альтушки, и используется для отслеживания каких альтушек скуф уже успел изучить.

    if "mod_intro_diana" not in act2_alts_checked:
        $ items.append( (_("Узнать больше про Диану"), "mod_intro_diana") )
    if "mod_intro_nadya" not in act2_alts_checked:
        $ items.append( (_("Узнать больше про Надежду"), "mod_intro_nadya") )
    if "mod_intro_polina" not in act2_alts_checked:
        $ items.append( (_("Узнать больше про Полину"), "mod_intro_polina") )
    return

label mod_choice_items:
    ## Dev. tip: Кнопки финального выбора.

    $ items.append( (_("Диана"), "mod_diana") )
    $ items.append( (_("Надежда"), "mod_nadya") )
    $ items.append( (_("Полина"), "mod_polina") )
    return


## Лейблы с интро альтушек
label mod_intro_diana:
    show diana1:
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    "Диана."
    "Альтушка-гяру."
    "Подражает азиатской субкультуре."
    "Очень яркая и жизнерадостная девушка."
    "Еë любовь к забугорью оправдана, она знает много иностранных языков!"     
    "Вы однозначно сможете провести незабываемые каникулы!"
    "Но хватит ли вам денег на её хотелки?.."
    play audio "another_attempt/audio/voice_inner/audio3.flac"
    inner "ЭТО ЕЩЁ ЧТО?" 
    stop audio
    play audio "another_attempt/audio/voice_inner/audio4.flac"
    inner "ПОЧЕМУ ОНА ЧЁРНАЯ?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio4.flac"
    skoof "Ничего ты не понимаешь, это стиль такой."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio5.flac"
    skoof "И выглядит она очень миленько, такая маленькая и аккуратная, я бы её точно..."
    stop audio
    return

label mod_intro_nadya:
    show nadya1:
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    "Надежда."
    "Альтушка-байкер."
    "Её манеры и поведение больше походят на мужские, кого-то это может отталкивать."
    "Но даже несмотря на брутальный вид, под этой маской скрывается добрейший души человек."
    "Её увлечение байками и экстремальными видами спорта заставят ценить свою жизнь больше, но только не её саму."
    play audio "another_attempt/audio/voice_inner/audio5.flac"
    inner "ЧЕГООО?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio6.flac"
    inner "СИЛЬНО УЖ ОНА ВЫДЕЛЯЕТСЯ НА ФОНЕ ДРУГИХ!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio7.flac"
    inner "РАЗВЕ НЕ ВСЕ АЛЬТУШКИ НОСЯТ МИНИ ЮБКИ,ЧТОБЫ СВЕТИТЬ СВОИМИ ПРЕЛЕСТЯМИ?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio6.flac"
    skoof "Да, может она и отличается от других, но разве это плохо?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio7.flac"
    skoof "Иметь крепкую и брутальную женщину, похожую на персонажа видеоигры, которая будет и девушкой, и другом."
    play audio "another_attempt/audio/voice_skoof/audio8.flac"
    stop audio
    skoof "А по ночам будет доминировать в постели..."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio8.flac"
    inner "АААА, ТАК ТЫ ИЗ ЭТИХ!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio9.flac"
    stop audio
    inner "ФЕТИШИСТ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio9.flac"
    skoof "Ой, отстань."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio10.flac"
    skoof "Ладно, давай дальше."
    stop audio
    return

label mod_intro_polina:
    show polina2:
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    "Полина."
    "? альтушка."
    "У неё свои тараканы в голове."
    "Любительница гороскопов очень тщательно выбирает себе партнёров по совместимости их знаков зодиака."
    "Хотя... вам в любом случае повезёт."
    "Или нет."
    "Частых срывов вам не избежать."
    "Но несмотря на это она и поиграет с вами в танчики, и компьютер починит, и кое-что ещё..."
    play audio "another_attempt/audio/voice_inner/audio10.flac"
    inner "ОГОО, ВОТ ЭТО БУФЕРА."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio11.flac"
    inner "ТАКИМИ И ЗАДУШИТЬ НЕ ГРЕХ!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio12.flac"
    inner "НО КОМУ НУЖНА ПОСТОЯННО ОРУЩАЯ НА ТЕБЯ ДЕВАХА?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio11.flac"
    skoof "Может немного неуравновешенная, но вторая доминирующая девушка лучше, чем ноль."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio12.flac"
    skoof "Да и в видеоигры с девушкой я ещё не играл.-В гороскопы я может и не верю, но..."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio13.flac"
    inner "ФЕ-ТИ-ШИСТ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio13.flac"
    skoof "Да заткнись..."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio14.flac"
    skoof "И что значит это “кое-что..”"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio14.flac"
    inner "А КАКАЯ РАЗНИЦА?!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio15.flac"
    inner "ГЛАВНОЕ, ЕСТЬ ЗА ЧТО ПОДЕРЖАТЬСЯ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio15.flac"
    skoof "Эх... тут ты прав."
    stop audio 
    play audio "another_attempt/audio/voice_skoof/audio16.flac"
    skoof "Я бы на её грудь..."
    stop audio
    play audio "another_attempt/audio/sound/cough.mp3"
    skoof "Кхм..."
    stop audio
    return


## Лейбл с диалогом с альтушками
label mod_talk:
    show diana1:
        align (0.15, 2.5)
        linear .25 zoom 1.0
    show nadya1:
        align (0.5, 1.0)
        linear .25 zoom 1.0
    show polina2:
        align (0.85, 1.9)
        linear .25 zoom 1.0
    play audio "another_attempt/audio/voice_skoof/audio17.flac"
    skoof "Даже не знаю, трудный выбор."
    stop audio
    hide polina2
    show polina6:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po1.flac"
    polina "Как по мне, ты всё уже решил."
    stop audio
    show polina6:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio18.flac"
    skoof "Чего?!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio16.flac"
    inner "ОНО ГОВОРИТ!"
    stop audio
    hide diana1
    show diana6:
        align (0.15, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di1.mp3"
    diana "Опять ты вперёд всех лезешь!"
    show diana6:
        align (0.15, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    hide polina6
    show polina1:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    polina "..."
    show polina1:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix (0.0)
    show diana6:
        align (0.15, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di2.mp3"
    diana "Ничем кроме груди похвастаться не можешь, да и одна больше другой."
    play audio "another_attempt/audio/voice_diana/di3.mp3"
    diana "Кому вообще могут нравится затворницы?!"
    show diana6:
        align (0.15, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    show polina1:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po2.flac"
    polina "Перестаньте говорить, о моей груди!"
    stop audio
    show polina1:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix (0.0)
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na1.flac"
    nadya "Не обращай внимания, они сейчас успокоятся."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na2.flac"
    nadya "Лучше задай нам интересующие тебя вопросы."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio19.flac"
    skoof "Вопросы?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na3.flac"
    nadya "Ага, чтобы понять, какая альтушка подходит тебе больше всего."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    hide polina1
    show polina6:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po3.flac"
    polina "Да кому это надо?"
    play audio "another_attempt/audio/voice_polina/po4.flac"
    polina "Все приходят сюда за альтушукой."
    play audio "another_attempt/audio/voice_polina/po5.flac"
    polina "У нас что здесь викторина?"
    show polina6:
        align (0.85, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix (0.0)
    play audio "another_attempt/audio/voice_skoof/audio20.flac"
    skoof "Я и впрямь хотел бы обойтись без распросов и просто выбрать кого-то из вас."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na4.flac"
    nadya "Оу, чтож... мы примем любой твой выбор."
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio17.flac"
    inner "КАКИЕ-ТО ОНИ ВСЕ... С ПРИВЕТОМ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio21.flac"
    skoof "Помолчи, ты мешаешь мне сделать выбор."
    stop audio
    return

## === Диана ===
label mod_diana:
    ## Dev. tip: Этот код блокирует возможность вернуться к выбору альтушки, также открывает возможность вернуть классический состав альтушек
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    $ within_selection = False
    $ config.rollback_enabled = True
    ##
    show diana6:
        linear .5 xalign 0.5 zoom 1.0
    hide polina6
    hide nadya4
    with dissolve
    hide diana6
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di4.mp3"
    diana "Так и знала, что ты выберешь меня!"
    play audio "another_attempt/audio/voice_diana/di5.mp3"
    diana "Никогда не сомневалась в тебе, Скуф!"
    play audio "another_attempt/audio/voice_diana/di6.mp3"
    diana "Теперь мы будем с тобой ходить по магазинам, кушать в ресторанах, а лучше готовить выпечку самим."
    play audio "another_attempt/audio/voice_diana/di7.mp3"
    diana "А ещё путешествовать, ходить на концерты, в кино, в, в..."
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio18.flac"
    inner "УЖАС! КАКАЯ ОНА ГОВОРЛИВАЯ!"
    stop audio
    hide diana2
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di8.mp3"
    diana "Je n'arrive pas à décrire à quel point je suis enthousiaste!"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio22.flac"
    skoof "Э-э-э, чего?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio19.flac"
    inner "ТЬФУ! У НЕЁ ЕЩЁ И ДИСЛЕКСИЯ!"
    stop audio
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di9.mp3"
    diana "Ну что, куда мне приехать?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio23.flac"
    skoof "Подожди-подожди, не тараторь."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio24.flac"
    skoof "Мы ведь должны заполнить документы, разве нет?"
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di10.mp3"
    diana "А ты хочешь?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio25.flac"
    skoof "А можно без них?"
    stop audio
    hide diana1
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di11.mp3"
    diana "Нет."
    play audio "another_attempt/audio/voice_diana/di12.mp3"
    diana "Но ты ведь уделишь мне немного времени, Скуф?"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Смотря на эту девчушку, у тебя возникают странные чувства."
    "Её внешний вид сбивает с толку, но она кажется милой и очаровательной."
    "Заводной характер и няшность невольно вызывают улыбку."
    "Но когда ты вспоминаешь об очередном заполнении документов, которое даже не гарантирует получение альтушки."
    "Улыбка сразу пропадает."
    play audio "another_attempt/audio/voice_skoof/audio26.flac"
    skoof "Ну, давай посмотрим."
    stop audio
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di13.mp3"
    diana "Не нужно так расстраиваться."
    play audio "another_attempt/audio/voice_diana/di14.mp3"
    diana "Обещаю, мы сделаем всё чистенько и быстренько."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio27.flac"
    skoof "Да если бы дело было только в этом..."
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di15.mp3"
    diana "А в чём же?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio20.flac"
    inner "А ТЫ ДОГАДАЙСЯ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio28.flac"
    skoof "Вся эта ваша контора чистой воды обман!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio29.flac"
    skoof "Все эти альтушки..."
    stop audio
    hide diana1
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di16.mp3"
    diana "Стоп, стоп, стоп!"
    play audio "another_attempt/audio/voice_diana/di17.mp3"
    diana "Не упоминай больше их!"
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio30.flac"
    skoof "С чего вдруг?"
    stop audio
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di18.mp3"
    diana "Ты выбрал меня!" 
    play audio "another_attempt/audio/voice_diana/di19.mp3"
    diana "Значит ни о ком другом думать не должен!"
    play audio "another_attempt/audio/voice_diana/di20.mp3"
    diana "Да и бесят они меня."
    play audio "another_attempt/audio/voice_diana/di21.mp3"
    diana "Не знаю как и почему они испортили тебе впечатление о всех альтушках"
    play audio "another_attempt/audio/voice_diana/di22.mp3"
    diana "Но я не такая!"
    hide diana6
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di23.mp3"
    diana "Обещаю, мы скоро будем вместе, я за свои слова отвечаю!"
    play audio "another_attempt/audio/voice_diana/di24.mp3"
    diana "Мне нужен только ты, Скуф!"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio21.flac"
    inner "НУ ПРЯМ АДВОКАТ ПЕТРЕНКО!"
    stop audio
    $ act2_loop_visited = set()
    jump mod_diana_loop

    return

label mod_diana_loop:
    menu:
        set act2_loop_visited
        "Земля и дом":
            jump mod_diana_landandhome
        set act2_loop_visited
        "Справки и выписки":
            jump mod_diana_certificatesandextracts
        set act2_loop_visited
        "Штрафы и налоги":
            jump mod_diana_finesandtaxes
        set act2_loop_visited
        "Регистрация и паспорт":
            jump mod_diana_registrationandpassport
    
    jump mod_diana_finale

    return

label mod_diana_landandhome:
    scene expression "uslugi/bg-su-home.png"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di25.mp3"
    diana "Земля и дом."
    hide diana1
    show diana2:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di26.mp3"
    diana "Да! Я хочу загородный дом!" 
    play audio "another_attempt/audio/voice_diana/di27.mp3"
    diana "Трёхэтажный белый дом, с большими панорамными окнами, большой-большой кухней, множеством комнат, бассейном, баром"
    play audio "another_attempt/audio/voice_diana/di28.mp3"
    diana "А ещё огромную комнату, кровать с штора, широкий подоконник, на котором можно укутаться в пледик и огромный гардероб"
    play audio "another_attempt/audio/voice_diana/di29.mp3"
    diana "Туда я положу свои платья, юбочки, туфельки, украшения, игрушки, книжки, журналы..."
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio22.flac"
    inner "ГОСПОДИ, ДА ЗАТКНИ ТЫ ЕЁ!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio23.flac"
    inner "УШИ В ТРУБОЧКУ УЖЕ СВЕРНУЛИСЬ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio31.flac"
    skoof "Но у тебя нет ушей."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio24.flac"
    inner "ТВОИ УШИ – МОИ УШИ!"
    stop audio
    hide diana2
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di30.mp3"
    diana "Ты что-то сказал, милый?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio32.flac"
    skoof "Нет, но..."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio33.flac"
    skoof "Загородного дома у меня нет."
    stop audio
    hide diana1
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di31.mp3"
    diana "Но как же?"
    play audio "another_attempt/audio/voice_diana/di32.mp3"
    diana "Хм..."
    hide diana5
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di33.mp3"
    diana "Может просто купишь?"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio25.flac"
    inner "ИШЬ, КАК У НЕЁ ВСЁ ПРОСТО!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio34.flac"
    skoof "Ты хоть знаешь какой это долгий процесс с кучей заморочек?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio35.flac"
    skoof "Найти дом, связаться с хозяином или риэлторским агентством, обратиться в соответствующие органы, заключить договор купле-продажи."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio36.flac"
    skoof "Да и денег нет!"
    stop audio
    hide diana4
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di34.flac"
    diana "Всё и правда так сложно?"
    hide diana5
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di35.mp3"
    diana "Скуф, ты такой умный!"
    play audio "another_attempt/audio/voice_diana/di36.mp3"
    diana "Тогда..."
    play audio "another_attempt/audio/voice_diana/di37.mp3"
    diana "Давай оформим кредит, и ты купишь мне дом?"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio37.flac"
    skoof "Нет уж, спасибо."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio38.flac"
    skoof "У меня есть замечательная квартира, доставшаяся мне от родителей."
    stop audio
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana ".........."
    diana ".................."
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di38.mp3"
    diana "Ну, ладненько."
    play audio "another_attempt/audio/voice_diana/di39.mp3"
    diana "Тогда, в этом разделе нам больше делать нечего."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio39.flac"
    skoof "Подожди."
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di40.mp3"
    diana "Что такое?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio40.flac"
    skoof "Почему ты так необычно выглядишь?"
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di41.mp3"
    diana "Этот стиль называется гяру, а точнее субкультура."
    play audio "another_attempt/audio/voice_diana/di42.mp3"
    diana "Таким внешним видом и легкомысленным поведением японские девушки заявляли о своих правах."
    play audio "another_attempt/audio/voice_diana/di43.mp3"
    diana "Мне так нравится их внешность, а ещё они знают толк в моде!"
    hide diana1
    show diana5:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di44.mp3"
    diana "Жаль, что не все это понимают и всерьёз меня не воспринимают."
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio26.flac"
    inner "НЕ УДИВИТЕЛЬНО!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio27.flac"
    inner "С ТАКИМ-ТО РАСКРАСОМ, КАК У ИНДЕЙЦА!"
    stop audio
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di45.mp3"
    diana "Как глупо осуждать людей за внешность."
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio41.flac"
    skoof "Это уж точно..."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio28.flac"
    inner "У КОГО-ТО КОМПЛЕКСЫ!"
    stop audio
    hide diana5
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di46.mp3"
    diana "Не стоит слушать людей, у которых хромосом меньше, чем у гороха."
    play audio "another_attempt/audio/voice_diana/di47.mp3"
    diana "{font=another_attempt/AsebiMin-Light.otf}彼らは私たちの注目に値しない。{/font}"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio29.flac"
    inner "КАРАВАЙ, ЧТО-ТО ТАМ, ТА-ТА-ТА...ОНА ТОЛЬКО ЧТО НАС ОБМАТЕРИЛА!?"
    stop audio
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "........"
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di48.mp3"
    diana "Хах, ладно, не важно."
    play audio "another_attempt/audio/voice_diana/di49.mp3"
    diana "Лучше скажи, какая одежда тебе больше нравится?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Хлопок":
            $ ochkoskoofa = ochkoskoofa + 1
        "Синтетика":
            $ ochkoskoofa = ochkoskoofa - 2
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di50.mp3"
    diana "Хорошо."
    play audio "another_attempt/audio/voice_diana/di51.mp3"
    diana "Может уже перейдем к следующему разделу?"
    play audio "another_attempt/audio/voice_diana/di52.mp3"
    diana "Чем быстрее закончим, тем быстрее я к тебе приеду!"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio42.flac"
    skoof "Ага, так, что там дальше?"
    stop audio
    jump mod_diana_loop
    return

label mod_diana_certificatesandextracts:
    scene expression "uslugi/bg-su-sprav.png"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di53.mp3"
    diana "Справки и выписки, справки и выписки, справки и выписки..."
    hide diana1
    show diana8:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di54.mp3"
    diana "А что мы должны делать в этом разделе?"
    show diana8:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio30.flac"
    inner "ДУМАЕШЬ МЫ ЗНАЕМ?"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio43.flac"
    skoof "Наверное, проверить справки и выписки."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio31.flac"
    inner "ЛОГИЧНОТЬ ПРЯМ ТВОЁ ВТОРОЕ ИМЯ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio44.flac"
    skoof "А что тебе важно знать?"
    stop audio
    hide diana8
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di55.mp3"
    diana "Важно знать?"
    play audio "another_attempt/audio/voice_diana/di56.mp3"
    diana "Дай-ка посмотрю"
    diana "............"
    diana "............................."
    hide diana3
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di57.mp3"
    diana "В этом разделе, кажется, ничего."
    hide diana1
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di58.mp3"
    diana "Ну и ладно. Давай лучше поговорим о чём-то романтичном."
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio45.flac"
    skoof "Романтичном?"
    stop audio
    hide diana4
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di59.mp3"
    diana "Да, например, романтичные произведения."
    play audio "another_attempt/audio/voice_diana/di60.mp3"
    diana "Ах, чего только стоят Ромео и Джульетта Шекспира. Герои идут на всё, чтобы быть вместе, прямо как мы. Или Анна Каренина Толстого. Ужасно трагичная история любви, страдающие люди, которым не суждено создать семью."
    play audio "another_attempt/audio/voice_diana/di61.mp3"
    diana "О нет! А ещё лучше – это стихи о любви."
    hide diana2
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di62.mp3"
    diana "The melody of life unfolds,"
    play audio "another_attempt/audio/voice_diana/di63.mp3"
    diana "When you are standing by my side."
    play audio "another_attempt/audio/voice_diana/di64.mp3"
    diana "Your hand in mine, my heart beholds,"
    play audio "another_attempt/audio/voice_diana/di65.mp3"
    diana "A love that cannot be denied."
    play audio "another_attempt/audio/voice_diana/di66.mp3"
    diana "Your smile dispels the darkest storm,"
    play audio "another_attempt/audio/voice_diana/di67.mp3"
    diana "It brings the sunshine to my day."
    play audio "another_attempt/audio/voice_diana/di68.mp3"
    diana "With you, my spirit will transform,"
    play audio "another_attempt/audio/voice_diana/di69.mp3"
    diana "And all my fears will fade away."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio32.flac"
    inner "ЧЕГО ЭТО ОНА ХВАСТАЕТСЯ!?"
    play audio "another_attempt/audio/voice_inner/audio33.flac"
    inner "Я, ВООБЩЕ-ТО, ТОЖЕ ТАК МОГУ."
    stop audio
    inner "КХМ..."
    play audio "another_attempt/audio/voice_inner/audio34.flac"
    inner "У МЕНЯ НЕ СТОИТ"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio35.flac"
    inner "ТВОЯ РОЗА В СТАКАНЕ,"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio36.flac"
    inner "У ТЕБЯ НЕ ТЕЧЕТ"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio37.flac"
    inner "ИЗ-ПОД КРАНА ВОДА,"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio38.flac"
    inner "Я Б ТЕБЕ ЗАСАДИЛ"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio39.flac"
    inner "ВСЮ АЛЛЕЮ ЦВЕТАМИ,"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio40.flac"
    inner "ЕСЛИ Б ТЫ МНЕ ДАЛА"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio41.flac"
    inner "ТЕХ ЦВЕТОВ СЕМЕНА!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio46.flac"
    skoof "Я тоже умею читать стихи."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio47.flac"
    skoof "Кхм... Вы любите розы, а я на них..."
    stop audio
    hide diana1
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di70.mp3"
    diana "Не-не-не..."
    hide diana3
    show diana8:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di71.mp3"
    diana "Давай не будем читать этот стих."
    hide diana8
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di72.mp3"
    diana "Но раз ты тоже увлекаешься литературой, скажи"
    play audio "another_attempt/audio/voice_diana/di73.mp3"
    diana "Что бы ты хотел со мной почитать?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Триллер":
            $ ochkoskoofa = ochkoskoofa + 1
        "Драму":
            $ ochkoskoofa = ochkoskoofa - 2

    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di74.mp3"
    diana "Хорошо. Теперь дальше."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    jump mod_diana_loop

    return

label mod_diana_finesandtaxes:
    scene expression "another_attempt/images/bg-finesandtaxes.png":
        subpixel True
        zoom 0.5
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di75.mp3"
    diana "Бесполезный раздел, как, впрочем, и все остальные."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio48.flac"
    skoof "То есть мы всё же зря занимаемся этой ерундой? "
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di76.mp3"
    diana "Ну почему. У нас есть свободное время, чтобы спокойно поговорить под видом бурной деятельности."
    hide diana1
    show diana3:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di77.mp3"
    diana "Но, если подумать, неуплата штрафов может грозить арестом более 15 суток, уплатой в двойном размере, лишению водительских прав, лишением имущества и даже ограничить выезд из страны."
    hide diana3
    show diana8:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di78.mp3"
    diana "А если выезд из страны запрещён, то мы не сможем путешествовать, а если не сможем путешествовать, значит не сможем познакомиться с новыми людьми, но главное, чтобы люди были добрые, а если люди не добрые, значит плохая энергия, а если энергия плохая, то будет блэкаут, значит телевизоры не будут работать, а самое интересное показывают в час ночи, но главное успеть вернуться до 12 или карета превратиться в тыкву, тыква из семейства тыквенных, но мне больше нравится дыня, а дыня...."
    hide diana8
    show diana3:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di79.mp3"
    diana "Ой..."
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    skoof "................"
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "........................................."
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio42.flac"
    inner "ОНА СЛОМАЛА НЕ ТОЛЬКО ЧЕТВЁРТУЮ, НО И НИЖНЮЮ СТЕНУ."
    stop audio
    hide diana3
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di80.mp3"
    diana "Наверное, я слишком увлеклась."
    play audio "another_attempt/audio/voice_diana/di81.mp3"
    diana "La prego di perdonarmi, signore."
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio43.flac"
    inner "Я ДАЖЕ ШУТИТЬ НЕ ХОЧУ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio49.flac"
    skoof "Это было увлекательное пояснение"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio50.flac"
    skoof "Но смысла я так и не понял."
    stop audio
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di82.mp3"
    diana "Не важно, забудь, хи-хи."
    diana ".........."
    play audio "another_attempt/audio/voice_diana/di83.mp3"
    diana "Скуф, скажи, куда бы ты сводил меня на свидание?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "В ресторан":
            $ ochkoskoofa = ochkoskoofa - 1
        "На квест":
            $ ochkoskoofa = ochkoskoofa + 2
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di84.mp3"
    diana "Хорошо. Теперь дальше."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    jump mod_diana_loop

    return

label mod_diana_registrationandpassport:
    scene expression "uslugi/bg-su-reg.png"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di85.mp3"
    diana "Регистрация и паспорт..."
    play audio "another_attempt/audio/voice_diana/di86.mp3"
    diana "Что ж, ты вроде всё заполнил при регистрации, так что"
    play audio "another_attempt/audio/voice_diana/di87.mp3"
    diana "Я просто подгружу данные, давай дальше."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio51.flac"
    skoof "Дальше?"
    stop audio
    hide diana1
    show diana8:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di88.mp3"
    diana "Да?"
    show diana8:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio52.flac"
    skoof "Без заполнения документов и лишних разговоров о всякой чепухе?"
    stop audio
    hide diana8
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di89.mp3"
    diana "Да..."
    play audio "another_attempt/audio/voice_diana/di90.mp3"
    diana "Но, если ты хочешь поговорить, я всегда готова тебя выслушать."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio53.flac"
    skoof "Да нет, давай дальше."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio44.flac"
    inner "НЕУЖЕЛИ. СВЕРШИЛОСЬ ЧУДО ИЗ ЧУДЕС!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio45.flac"
    inner "НЕ ПРИДЁТСЯ СЛУШАТЬ ЭТУ ТАРАТОРКУ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio54.flac"
    skoof "И вправду удивительно."
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di91.mp3"
    diana "Ой, подожди"
    play audio "another_attempt/audio/voice_diana/di92.mp3"
    diana "Скажи, куда бы ты хотел пойти со мной погулять?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "На кладбище":
            $ ochkoskoofa = ochkoskoofa - 1
        "В парк":
            $ ochkoskoofa = ochkoskoofa + 2
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di93.mp3"
    diana "Хорошо. Теперь дальше."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    jump mod_diana_loop

    return

label mod_diana_finale:
    scene expression "uslugi/bg-su.png"
    hide diana1
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di94.mp3"
    diana "Ого, как быстро мы всё заполнили."
    show diana2:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio55.flac"
    skoof "Да... быстро..."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio46.flac"
    stop audio
    inner "А ВОТ ЕСЛИ Б НЕ БОЛТАЛИ!"
    play audio "another_attempt/audio/voice_skoof/audio56.flac"
    skoof "И теперь ты приедешь?"
    stop audio
    hide diana2
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di95.mp3"
    diana "Ну конечно приеду, что за вопросы, глупенький."
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio57.flac"
    skoof "Да что-то не все доезжают, а если и доезжают, то не в собранном состоянии."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio58.flac"
    skoof "Всё же сервис ваш... Эх..."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio59.flac"
    skoof "Одни обманывают, другие непонятно кто и что тут делают, третьим помогай сбежать и осуществить мечту."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio60.flac"
    skoof "И ведь не все плохие, кому-то просто не повезло родиться такой, как Нюша, или сидеть тут принудительно."
    stop audio
    hide diana4
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di96.mp3"
    diana "Ты что меня вообще не слушал?"
    play audio "another_attempt/audio/voice_diana/di97.mp3"
    diana "Я же сказала, что ты не должен думать ни о ком, кроме меня!"
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio61.flac"
    skoof "Я...."
    stop audio
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di98.mp3"
    diana "Кто вообще такая Нюша?"
    play audio "another_attempt/audio/voice_diana/di99.mp3"
    diana "Не помню такой"
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio62.flac"
    skoof "Девушка со второй страницы с розово-чëрными волосами." 
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio63.flac"
    skoof "Я думал вы все знакомы друг с другом."
    stop audio
    hide diana6
    show diana7:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di100.mp3"
    diana "А-а-а, ты про дефектную, с диссоциативным расстройством личности, дыркой вместо глаза и комплексом второй страницы?"
    play audio "another_attempt/audio/voice_diana/di101.mp3"
    diana "Нюша, Нана, Лина, Ниса..."
    play audio "another_attempt/audio/voice_diana/di102.mp3"
    diana "Нет нужды запоминать имена неудачных экспериментов."
    show diana7:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio64.flac"
    skoof "Почему ты так плохо отзываешься о других альтушках? "
    stop audio
    hide diana7
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di103.mp3"
    diana "А почему я должна перед тобой оправдываться?"
    play audio "another_attempt/audio/voice_diana/di104.mp3"
    diana "Эти халтурные, кустарные, неполноценные куклы просто выводят меня из себя!"
    play audio "another_attempt/audio/voice_diana/di105.mp3"
    diana "Так есть ещё и те, кого тут быть не должно! Суют свой нос куда не просят!"
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Мнение об Алисе, Кире и Маре":
            hide diana6
            show diana7:
                align (0.5, 2.5)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di106.mp3"
            diana "Алиса... Растяжимое понятие."
            play audio "another_attempt/audio/voice_diana/di107.mp3"
            diana "Штамповать копии на заводе легко, а вот уследить за всеми ними они не смогли."
            play audio "another_attempt/audio/voice_diana/di108.mp3"
            diana "Кира, ну-у-у, ей не помогут даже омолаживающие крема."
            play audio "another_attempt/audio/voice_diana/di109.mp3"
            diana "Мара... Да как её вообще пропустили, она ведь даже говорить не может, а её вкус в одежде оставляет желать лучшего."
            play audio "another_attempt/audio/voice_diana/di110.mp3"
            diana "Да что я говорю, её вкус в одежде ужасен."
            show diana7:
                align (0.5, 2.5)
                subpixel True
                linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            jump mod_diana_hanamozgam

        "Мнение о Ксюше, Насте и Лизе":
            show diana6:
                align (0.5, 2.5)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di111.mp3"
            diana "Настя и Ксюша. Две плоские, шаблонные картонки."
            play audio "another_attempt/audio/voice_diana/di112.mp3"
            diana "Работают по заданному алгоритму. Да только идиот не заметит, что у них один и тот же текст."
            play audio "another_attempt/audio/voice_diana/di113.mp3"
            diana "Настолько идеальные ответы, что аж тошно. "
            play audio "another_attempt/audio/voice_diana/di114.mp3"
            diana "Лиза... Да, помню такую."
            play audio "another_attempt/audio/voice_diana/di115.mp3"
            diana "Гадалка, кажется. Занялась бы лучше чем-то полезным, а не в карты играла."
            show diana6:
                align (0.5, 2.5)
                subpixel True
                linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            jump mod_diana_hanamozgam

        "Мнение о Наде и Полине":
            show diana6:
                align (0.5, 2.5)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di164.mp3"
            diana "Надя и Полина, я даже не знаю кто они, но знаю, что Полина меня жутко бесит!"
            play audio "another_attempt/audio/voice_diana/di165.mp3"
            diana "Я была совсем одна на этой странице, и тут появились они."
            play audio "another_attempt/audio/voice_diana/di166.mp3"
            diana "Если все альтушки шаблонные и плоские, то Полина слишком аффективная и чересчур остра на язык."
            play audio "another_attempt/audio/voice_diana/di167.mp3"
            diana "Надя кажется мне рассудительной, но какой нормальный мужчина захочет встречаться с пацанкой?"
            play audio "another_attempt/audio/voice_diana/di168.mp3"
            diana "Всё тело в этих ужасных татуировках, гоняет на мотоциклах и постоянно подвергает опасности не только себя, но и других."
            jump mod_diana_taptapxamsterkriminal
            
            
    return

label mod_diana_hanamozgam:
    hide diana7
    show diana6:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "........"
    hide diana6
    show diana5:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di116.mp3"
    diana "Я больше не хочу говорить о них."
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio65.flac"
    skoof "Хорошо, мы больше не будем, но..."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio66.flac"
    skoof "Ответь мне на один вопрос."
    stop audio
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di117.mp3"
    diana "Какой?"
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio67.flac"
    skoof "Ты тоже искусственный интеллект?"
    stop audio
    hide diana5
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di118.mp3"
    diana "Что? Конечно нет! Как ты мог о таком подумать?"
    hide diana3
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di119.mp3"
    diana "Хотя неважно."
    play audio "another_attempt/audio/voice_diana/di120.mp3"
    diana "Кем бы я не была, реальной альтушкой, искусственным интеллектом, разработчиком, мошенником..."
    play audio "another_attempt/audio/voice_diana/di121.mp3"
    diana "Ничто не помешает нам быть вместе!"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio47.flac"
    inner "КАК-БУДТО ОНА СТАВИТ НАС ПЕРЕД ФАКТОМ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio68.flac"
    skoof "Это прозвучало жутко..."
    stop audio
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di122.mp3"
    diana "Но..."
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio48.flac"
    inner "О НЕТ! НИКАКИХ «НО» В МОЮ СМЕНУ!"
    stop audio
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di123.mp3"
    diana "Ведь хорошего мужчину должно быть много."
    play audio "another_attempt/audio/voice_diana/di124.mp3"
    diana "А хороший мужчина – это умный мужчина."
    play audio "another_attempt/audio/voice_diana/di125.mp3"
    diana "Давай устроим мозговой штурм?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio69.flac"
    skoof "Мозговой штурм?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio49.flac"
    inner "У НАС И ТАК НЕ ТО ШТУРМ, НЕ ТО ШТОРМ В ГОЛОВЕ."
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di126.mp3"
    diana "Я задам тебе несколько задач, совсем лёгких."
    play audio "another_attempt/audio/voice_diana/di127.mp3"
    diana "Вообще, понятие мозгового штурма немного иное"
    play audio "another_attempt/audio/voice_diana/di128.mp3"
    diana "Мозговой штурм – это метод генерации идей в группе, направленный на поиск творческих решений проблемы."
    play audio "another_attempt/audio/voice_diana/di129.mp3"
    diana "Основные принципы: количество важнее качества, критика запрещена, комбинирование и улучшение, свобода мысли."
    play audio "another_attempt/audio/voice_diana/di130.mp3"
    diana "Но, я думаю, нам обоим будет проще так называть эту игру."
    play audio "another_attempt/audio/voice_diana/di131.mp3"
    diana "Так о чём это я?"
    play audio "another_attempt/audio/voice_diana/di132.mp3"
    diana "Если решишь большую часть заданий правильно, я приеду к тебе."
    play audio "another_attempt/audio/voice_diana/di133.mp3"
    diana "Пошевелим нашими мозгами!"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio50.flac"
    inner "МНЕ КАЖЕТСЯ ИЛИ Я НАЧИНАЮ УМНЕТЬ?"
    stop audio 
    play audio "another_attempt/audio/voice_skoof/audio70.flac"
    skoof "А если я не смогу решить?"
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "............"
    play audio "another_attempt/audio/voice_diana/di134.mp3"
    diana "Тогда тоже приеду, чтобы подтянуть твои знания!"
    play audio "another_attempt/audio/voice_diana/di135.mp3"
    diana "Ты готов?"
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio51.flac"
    inner "ДА ОН НИКОГДА НИ К ЧЕМУ НЕ ГОТОВ!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio52.flac"
    inner "ЗНАНИЯ ЕГО НА УРОВНЕ МЛАДЕНЦА!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio71.flac"
    skoof "Вообще-то у меня есть справка о среднем образовании."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio72.flac"
    skoof "Да и если вопросы лёгкие, то я точно с ними справлюсь."
    stop audio
    hide diana1
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di136.mp3"
    diana "Начинаем!"
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di137.mp3"
    diana "Четыре плюс шесть."
    menu:
        diana "{cps=0}Четыре плюс шесть."
        "10":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di138.mp3"
            diana "Великолепно!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
        "2":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di139.mp3"
            diana "Стоит ещё подумать."
    play audio "another_attempt/audio/voice_diana/di140.mp3"
    diana "Семь умножить на восемь." 
    menu: 
        diana "{cps=0}Семь умножить на восемь." 
        "48":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di142.mp3"
            diana "Не волнуйся, ты сильный и справишься!"
        "56":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di141.mp3"
            diana "Я в восторге!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di143.mp3"
    diana "Назови все царства живой природы."
    menu:
        diana "{cps=0}Назови все царства живой природы."
        "Растения, бактерии, животные":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di145.mp3"
            diana "Ты старался, но этот ответ неправильный."
        
        "Люди, животные, растения, бактерии":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di145.mp3"
            diana "Ты старался, но этот ответ неправильный."
        
        "Бактерии, грибы, растения и животные":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di144.mp3"
            diana "Поразительно!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di146.mp3"
    diana "Какова протяжённость каждого меридиана в мире?"
    menu:
        diana "{cps=0}Какова протяжённость каждого меридиана в мире?"
        "30000 км":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
        
        "20000 км":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di147.mp3"
            diana "Я поражена, Скуф!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
        
        "40000 км":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
        
        "50000 км":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
    play audio "another_attempt/audio/voice_diana/di149.mp3"
    diana "Что сказал Чацкий в третьем действии втором явлении двадцать первой строке комедии Грибоедова “Горе от ума”?"
    menu:
        diana "{cps=0}Что сказал Чацкий в третьем действии втором явлении двадцать первой строке комедии Грибоедова “Горе от ума”?"
        "Бог с вами, остаюсь опять с моей загадкой":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di150.mp3"
            diana "Откуда ты столько знаешь?"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)

        "А судьи кто?":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di151.mp3"
            diana "Один шаг назад – это два шага вперёд!"

        "Счастливые часов не наблюдают":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di151.mp3"
            diana "Один шаг назад – это два шага вперёд!"
        
        "Свежо предание, а верится с трудом":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di151.mp3"
            diana "Один шаг назад – это два шага вперёд!"
        
        "Взманили почести и знатность?":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di151.mp3"
            diana "Один шаг назад – это два шага вперёд!"
    play audio "another_attempt/audio/voice_diana/di152.mp3"
    diana "Время, за которое лодка переплывёт реку по кратчайшему пути, в два раза больше минимального времени, за которое лодка может переплыть ту же реку. Чему равна скорость лодки относительно воды, если скорость течения реки 5,0 м/с?"
    menu:
        diana "{cps=0}Время, за которое лодка переплывёт реку по кратчайшему пути, в два раза больше минимального времени, за которое лодка может переплыть ту же реку. Чему равна скорость лодки относительно воды, если скорость течения реки 5,0 м/с?"
        "4.0 м/с":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
       
        "5.0 м/с":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
       
        "4.8 м/с":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
       
        "5.5 м/с":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
       
        "6.0 м/с":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di148.mp3"
            diana "Стоит ещё подумать."
       
        "5.8 м/с":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di153.mp3"
            diana "Ты превзошёл все мои ожидания!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di154.mp3"
    diana "Сколько нужно сахара, чтобы испечь торт, если кит это млекопитающее, валентность натрия 1, а третьего тома “Мёртвых душ” не существовало, при условии, что столетняя война длилась 116 лет?"
    menu:
        diana "{cps=0}Сколько нужно сахара, чтобы испечь торт, если кит это млекопитающее, валентность натрия 1, а третьего тома “Мёртвых душ” не существовало, при условии, что столетняя война длилась 116 лет?"
        "Гипомания":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di156.mp3"
            diana "Ты старался, но этот ответ неправильный."

        "Рсбгймэоьк пугёу рёстйл":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di156.mp3"
            diana "Ты старался, но этот ответ неправильный."
        
        "Cannella":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di156.mp3"
            diana "Ты старался, но этот ответ неправильный."
        
        "Персик":
            $ brainsturm = brainsturm + 1
            hide diana1
            show diana2:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di155.mp3"
            diana "Невозможно!"
            hide diana2
            show diana1:
                align (0.5, 2.5)
                subpixel True
                zoom 1.05 matrixcolor BrightnessMatrix(0.1)
        
        ".--. --- .... .. --.- . -. .. .":
            jump mod_ending_diana_3
        
        "Lies":
            $ brainsturm = brainsturm - 1
            play audio "another_attempt/audio/voice_diana/di156.mp3"
            diana "Ты старался, но этот ответ неправильный."

    if ochkoskoofa + brainsturm > 8:
        jump mod_ending_diana_1
    else:
        jump mod_ending_diana_2

    return

label mod_diana_taptapxamsterkriminal:

    show diana6:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "........"
    hide diana6
    show diana5:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di169.mp3"
    diana "Я больше не хочу говорить о них."
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio73.flac"
    skoof "Хорошо, мы больше не будем..." 
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio74.flac"
    skoof "Но ответь мне на один вопрос."
    stop audio
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di170.mp3"
    diana "Какой?"
    show diana5:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio67.flac"
    skoof "Ты тоже искусственный интеллект?"
    stop audio
    hide diana5
    show diana3:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di171.mp3"
    diana "Что? Конечно нет! Как ты мог о таком подумать?"
    hide diana3
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di172.mp3"
    diana "Хотя неважно."
    play audio "another_attempt/audio/voice_diana/di173.mp3"
    diana "Кем бы я не была, реальной альтушкой, искусственным интеллектом, разработчиком, мошенником..."
    play audio "another_attempt/audio/voice_diana/di174.mp3"
    diana "Ничто не помешает нам быть вместе!"
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio47.flac"
    inner "КАК-БУДТО ОНА СТАВИТ НАС ПЕРЕД ФАКТОМ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio68.flac"
    skoof "Это прозвучало жутко..."
    stop audio
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di175.mp3"
    diana "Но..."
    show diana4:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio48.flac"
    inner "О НЕТ! НИКАКИХ «НО» В МОЮ СМЕНУ!"
    stop audio
    hide diana4
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di176.mp3"
    diana "Ведь хорошего мужчину должно быть много."
    play audio "another_attempt/audio/voice_diana/di177.mp3"
    diana "А хороший мужчина – это мужчина при деньгах."
    play audio "another_attempt/audio/voice_diana/di178.mp3"
    diana "Давай я помогу тебе заработать денег."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio75.flac"
    skoof "В казино я играть не буду."
    stop audio
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di179.mp3"
    diana "Нет, дурачок, всё намного проще."
    play audio "another_attempt/audio/voice_diana/di180.mp3"
    diana "Давай я покажу."
    show diana1:
        align (0.5, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Заработать деньги":
            scene expression "another_attempt/images/diana/zadnik.png"
            show pet:
                zoom 0.5
                yalign 0.55
                xalign 0.5
            show barelement:
                xalign 0.5
                yalign 0.15
            show diana1:
                align (0.01, 2.5)
                subpixel True
                linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            play audio "another_attempt/audio/voice_inner/audio53.flac"
            inner "ЭТО ЧТО, СТАВКИ НА СПОРТ?"    
            stop audio
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di181.mp3"
    diana "Нет, глупый, это Квокка."
    play audio "another_attempt/audio/voice_diana/di182.mp3"
    diana "Казуальная игра, с помощью которой можно заработать много-много денег всего лишь нажимая на зверушку."
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio76.flac"
    skoof "Звучит как полный развод."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio77.flac"
    skoof "Как обычно."
    stop audio
    hide diana1
    show diana5:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di183.mp3"
    diana "Неправда, всё даже очень реально!"
    play audio "another_attempt/audio/voice_diana/di184.mp3"
    diana "Тут даже есть отзывы."
    show diana5:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio54.flac"
    inner "КОТОРЫЕ ОНИ САМИ И НАПИСАЛИ."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio78.flac"
    skoof "Тогда почему ты сама не зарабатываешь с помощью этого деньги?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio55.flac"
    inner "ДА, ПОЧЕМУ!?"
    stop audio
    show diana5:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di185.mp3"
    diana "Это игра на время."
    play audio "another_attempt/audio/voice_diana/di186.mp3"
    diana "У меня никак не получается нажать нужное количество раз, чтобы выиграть деньги."
    hide diana5
    show diana4:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di187.mp3"
    diana "Но я уверена, что ты с этим справишься!"
    play audio "another_attempt/audio/voice_diana/di188.mp3"
    diana "Ты ведь хорош в играх, Скуф?"
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio79.flac"
    skoof "Да-а-а, я в этом хорош."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio80.flac"
    skoof "Ладно, что нужно делать?"
    stop audio
    hide diana4
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di189.mp3"
    diana "Как я и сказала эта игра на время."
    play audio "another_attempt/audio/voice_diana/di190.mp3"
    diana "Успеваешь нажать нужное количество раз за отведённое время – забираешь деньги."
    play audio "another_attempt/audio/voice_diana/di191.mp3"
    diana "Не успеваешь – остаешься ни с чем."
    play audio "another_attempt/audio/voice_diana/di192.mp3"
    diana "Просто, правда?"
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio81.flac" 
    skoof "Ага."
    stop audio
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di193.mp3"
    diana "Тогда приготовься."
    hide diana1
    show diana2:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di194.mp3"
    diana "Ой, кстати, интересный факт о квокках"
    play audio "another_attempt/audio/voice_diana/di195.mp3"
    diana "Они живут только в Австралии и ближнем востоке, квокки считаются ближайшими родственниками кенгуру, а ещё они любят контактировать с людьми и так мило улыбаются, ми-ми-ми."
    hide diana2
    show diana1:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di196.mp3"
    diana "Итак... Начали!"
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    $ time = 60
    $ time_range = 60
    call screen klicker

    return

# === КОНЦОВКИ ===

label mod_ending_diana_1:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Самый умный Скуф")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    hide diana1
    show diana2:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di157.mp3"
    diana "Я так впечатлена, Скуф!"
    play audio "another_attempt/audio/voice_diana/di158.mp3"
    diana "Не думала, что ты сможешь ответить правильно на такое количество вопросов!"
    hide diana2
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di159.mp3"
    diana "Жди, уже скоро мы будем вместе, хи-хи!"
    scene cg-dianaandskoof
    with fade
    ## Dev. tip: Изменение стиля на домашний
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    stop music
    play audio "another_attempt/audio/voice_inner/audio56.flac"
    inner "АЛЬТУШКУ ДИАНУ ПОРАЗИЛ НЕВЕРОЯТНЫЙ ИНТЕЛЛЕКТ СКУФА, И СОВСЕМ СКОРО ОНА ПЕРЕЕХАЛА К НЕМУ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio57.flac"
    inner "ВМЕСТЕ ОНИ СОБРАЛИСЬ В ОЧЕНЬ ДОЛГОЕ КРУГОСВЕТНОЕ ПУТЕШЕСТВИЕ, ЛЕТ ТАК НА ПЯТЬ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio58.flac"
    inner "НО СКУФ ОКАЗАЛСЯ СЛИШКОМ ЛЕНИВ И НЕПОВОРОТЛИВ ДЛЯ ТАКИХ ПРЕКЛЮЧЕНИЙ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio59.flac"
    inner "ПУСКАЙ ДИАНА И ОБИДЕЛАСЬ, НО ВКОРЕ ПРОСТИЛА СТАРИКА СКУФА И СТАЛА ДОМОХОЗЯЙКОЙ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio60.flac"
    inner "КАЖДЫЙ ДЕНЬ ОНА ГОТОВИЛА ЕМУ РАЗНЫЕ БЛЮДА, ОН ПОКУПАЛ ЕЙ ДОРОГУЮ ОДЕЖДУ, А ДИАНА ПРОДОЛЖЛА РАЗИВАТЬ ЕГО ИНТЕЛЛЕКТУАЛЬНЫЕ СПОСОБНОСТИ."
    stop audio
    hide cg-dianaandskoof
    $ renpy.movie_cutscene("another_attempt/images/diana/cg-duanaandckoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    play audio "another_attempt/audio/voice_inner/audio61.flac"
    inner "ВСЁ ВООБЩЕ НЕ ТАК!"
    stop audio
    play audio "another_attempt/audio/sound/dzin.mp3"
    pause 3.0
    scene expression "hata/13 view to corridor.png"
    with fade
    play audio "another_attempt/audio/voice_skoof/audio82.flac" 
    skoof "Кто там?"
    stop audio
    scene expression "another_attempt/images/diana/cg-courier.png"
    with dissolve
    play audio "another_attempt/audio/voice_courier/audio1.flac"
    "{color=#415B4E}{font=another_attempt/Correction-Brush.ttf}Курьер{/color}{/font}" "{font=another_attempt/Correction-Brush.ttf}Здравствуйте, вам тут грамоту прислали и торт. Вручается заслуженному победителю в номинации «Самый умный Скуф». Распишитесь, пожалуйста.{/font}"
    stop audio
    if 10 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_ymn:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop 
        pause 4.0
        hide achievements_ymn
        with moveouttop
        $ achievements.remove(10)
    play audio "another_attempt/audio/voice_inner/audio62.flac"
    inner "НУ, ХОТЯ БЫ НЕ САМЫЙ ТУПОЙ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio83.flac" 
    skoof "И опять без альтушки..."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio63.flac"
    inner "ЗАТО С ТОРТОМ!"
    stop audio

    jump titles
    return 

label mod_ending_diana_2:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Самый тупой Скуф")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    play audio "another_attempt/audio/sound/lose.mp3"
    pause 3.0
    hide diana1
    hide diana2
    show diana5:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di160.mp3"
    diana "Оу, ты... ответил меньше, чем я ожидала."
    hide diana5
    show diana4:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di161.mp3"
    diana "Ничего страшного! Как и обещала, я подтяну твои знания."
    play audio "another_attempt/audio/voice_diana/di162.mp3"
    diana "Жди, уже скоро мы будем вместе, хи-хи!"
    scene cg-dianaandskoof
    with fade
    ## Dev. tip: Изменение стиля на домашний
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    stop music
    play audio "another_attempt/audio/voice_inner/audio56.flac"
    inner "АЛЬТУШКУ ДИАНУ ПОРАЗИЛ НЕВЕРОЯТНЫЙ ИНТЕЛЛЕКТ СКУФА, И СОВСЕМ СКОРО ОНА ПЕРЕЕХАЛА К НЕМУ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio57.flac"
    inner "ВМЕСТЕ ОНИ СОБРАЛИСЬ В ОЧЕНЬ ДОЛГОЕ КРУГОСВЕТНОЕ ПУТЕШЕСТВИЕ, ЛЕТ ТАК НА ПЯТЬ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio58.flac"
    inner "НО СКУФ ОКАЗАЛСЯ СЛИШКОМ ЛЕНИВ И НЕПОВОРОТЛИВ ДЛЯ ТАКИХ ПРЕКЛЮЧЕНИЙ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio59.flac"
    inner "ПУСКАЙ ДИАНА И ОБИДЕЛАСЬ, НО ВКОРЕ ПРОСТИЛА СТАРИКА СКУФА И СТАЛА ДОМОХОЗЯЙКОЙ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio60.flac"
    inner "КАЖДЫЙ ДЕНЬ ОНА ГОТОВИЛА ЕМУ РАЗНЫЕ БЛЮДА, ОН ПОКУПАЛ ЕЙ ДОРОГУЮ ОДЕЖДУ, А ДИАНА ПРОДОЛЖЛА РАЗИВАТЬ ЕГО ИНТЕЛЛЕКТУАЛЬНЫЕ СПОСОБНОСТИ."
    stop audio
    hide cg-dianaandskoof
    $ renpy.movie_cutscene("another_attempt/images/diana/cg-duanaandckoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    play audio "another_attempt/audio/voice_inner/audio61.flac"
    inner "ВСЁ ВООБЩЕ НЕ ТАК!"
    stop audio
    play audio "another_attempt/audio/sound/dzin.mp3"
    pause 3.0
    scene expression "hata/13 view to corridor.png"
    with fade
    play audio "another_attempt/audio/voice_skoof/audio82.flac" 
    skoof "Кто там?"
    stop audio
    scene expression "another_attempt/images/diana/cg-courier.png"
    with dissolve
    play audio "another_attempt/audio/voice_courier/audio2.flac"
    "{color=#415B4E}{font=another_attempt/Correction-Brush.ttf}Курьер{/color}{/font}" "{font=another_attempt/Correction-Brush.ttf}Здравствуйте, вам тут грамоту прислали. Вручается заслуженному победителю в номинации «Самый тупой Скуф». Распишитесь, пожалуйста.{/font}"
    stop audio
    if 9 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_typ:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_typ
        with moveouttop
        $ achievements.remove(9)
    play audio "another_attempt/audio/voice_skoof/audio84.flac" 
    skoof "Чего-о? Мне кажется, вы ошиблись дверью."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio64.flac"
    inner "ДВА ДУРАКА ХОРОШО – А ОДИН ЕЩЁ ЛУЧШЕ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio85.flac" 
    skoof "А как же альтушка..."
    stop audio
    jump titles    
    
    return 

label mod_ending_diana_3:

    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Это моя няшечка-вкусняшечка")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    hide diana1
    hide diana2
    stop music
    play audio "another_attempt/audio/sound/scary.mp3"
    pause 3.0
    show diana3:
        align (0.5, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    scene expression "uslugi/bg-black.png"
    scene expression "another_attempt/images/diana/cg-otkyda.png":
        xalign 0.5
        yalign 0.5        
        zoom 0.5
    with fade
    play audio "another_attempt/audio/voice_diana/di163.mp3"
    pause 3.0
    if 7 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_mynashechka:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_mynashechka
        with moveouttop
        $ achievements.remove(7)
    jump titles

    return

label mod_ending_diana_4:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Тап-тап хамстер")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    
    hide screen klicker
    hide diana1
    show diana2:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di197.mp3"
    diana "Это невероятно, Скуф, ты это сделал!"
    show diana2:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio86.flac" 
    skoof "Всё ради тебя, дорогая!"
    stop audio
    hide diana2
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di198.mp3"
    diana "Теперь введи номер своей карты, чтобы забрать деньги."
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio65.flac"
    inner "И ЭТА ТУДА ЖЕ. СТОИЛО СРАЗУ ПОНЯТЬ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio87.flac" 
    skoof "Ну хватит, девушка она образованная, к тому же такая милая и неловкая."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio88.flac" 
    skoof "У неё нет причин врать."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio66.flac"
    inner "ТЫ ГОВОРИШЬ ЭТО КАЖДЫЙ РАЗ, И КАЖДЫЙ РАЗ ОДНО И ТО ЖЕ!"
    stop audio
    hide diana1
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di199.mp3"
    diana "Не бойся за безопасность твоих денежных средств."
    hide diana4
    show diana1:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di200.mp3"
    diana "Как и полагается, тебе придёт уведомление о пополнении счёта."
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Перед тем как ввести номер карты, всё внутри тебя сжалось, словно вновь ожидая подвох."
    "Но собравшись с силами ты делаешь это."
    menu:
        "Ввести номер карты":
            play audio "another_attempt/audio/sound/klava.mp3"
            pause 3.0
            show diana1:
                align (0.01, 2.5)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_diana/di201.mp3"
            diana "Подожди пару секунд."

    diana "............"
    diana "........................."
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/sound/sms.mp3"
    pause 1.0    
    play audio "another_attempt/audio/sound/komp.mp3"
    "Звук входящего СМС разрезает тишину"
    if 4 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_money:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_money
        with moveouttop
        $ achievements.remove(4)
    "Ваш счёт пополнен на 10000000000 руб. Поздравляем!"
    play audio "another_attempt/audio/voice_skoof/audio89.flac" 
    skoof "Ух ты!"
    stop audio
    show diana1:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di202.mp3"
    diana "Я же говорила!"
    hide diana1
    show diana2:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di203.mp3"
    diana "Теперь мы можем отправиться в кругосветное путешествие!"
    play audio "another_attempt/audio/voice_diana/di204.mp3"
    diana "Мы будем плавать в море, загорать, пить коктейли, или поднимемся на высокую снежную гору, спустимся оттуда на лыжах, а ещё лучше купим кучу вещей, снимем самый дорогой лав отель и,и..."
    show diana2:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner/audio67.flac"
    inner "ПРОВЕРИЛ БЫ КА ТЫ СВОЙ БАЛАНС."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio90.flac" 
    skoof "Не сейчас, не видишь, мы заняты!"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio68.flac"
    inner "НУ-НУ."
    stop audio
    scene cg-dianaandskoof
    with fade
    ## Dev. tip: Переход в режим концовки
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    stop music
    play audio "another_attempt/audio/voice_inner/audio69.flac"
    inner "АЛЬТУШКА ДИАНА БЫЛА РАДА СТОЛЬ УДАЧНОМУ ВЫЙГРЫШУ, И СОВСЕМ СКОРО ОНА ПЕРЕЕХАЛА К СКУФУ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio57.flac"
    inner "ВМЕСТЕ ОНИ СОБРАЛИСЬ В ОЧЕНЬ ДОЛГОЕ КРУГОСВЕТНОЕ ПУТЕШЕСТВИЕ, ЛЕТ ТАК НА ПЯТЬ."
    play audio "another_attempt/audio/voice_inner/audio58.flac"
    inner "НО СКУФ ОКАЗАЛСЯ СЛИШКОМ ЛЕНИВ И НЕПОВОРОТЛИВ ДЛЯ ТАКИХ ПРЕКЛЮЧЕНИЙ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio70.flac"
    inner "ПУСКАЙ ДИАНА И ОБИДЕЛАСЬ, НО ВКОРЕ ПРОСТИЛА СТАРИКА СКУФА."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio71.flac"
    inner "А ЗАРАБОТАННЫЕ ДЕНЬГИ ДИАНА РЕШИЛА ПОТРАТЬ НА НАРЯДЫ, КОСМЕТИКУ, УКРАШЕНИЯ И РОСКОШНЫЕ СВИДАНИЯ СО СКУФОМ."
    stop audio
    hide cg-dianaandskoof
    $ renpy.movie_cutscene("another_attempt/images/diana/cg-duanaandckoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    play audio "another_attempt/audio/voice_inner/audio61.flac"
    inner "ВСЁ ВООБЩЕ НЕ ТАК!"
    stop audio
    play audio "another_attempt/audio/sound/sms.mp3"
    pause 1.0  
    scene expression "hata/15 workspace hand.png"
    with fade
    "ЗВУК ВХОДЯЩЕГО СМС РАЗРЕЗАЕТ ТИШИНУ ТВОЕЙ КВАРТИРЫ!"
    "С вашего счета было списано 10000000000 руб. На вашем балансе осталось -9999999000 руб."
    "Пожалуйста, как можно быстрее погасите долг и убедитесь, не начислены ли на сумму долга пени и штрафы."
    play audio "another_attempt/audio/voice_skoof/audio91.flac" 
    skoof "А как же альтушка..."
    stop audio
    play audio "another_attempt/audio/sound/sms.mp3"
    pause 1.0  
    scene expression "another_attempt/images/diana/cg-mobila.png":
        xalign 0.5
        yalign 0.5
    with fade
    play audio "another_attempt/audio/voice_inner/audio72.flac"
    inner "ВОТ И ПОПУТЕШЕСТВОВАЛИ!!!"
    stop audio
    jump titles

    return

label mod_ending_diana_5:
        ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Не трогай моё лицо!")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    play audio "another_attempt/audio/sound/lose.mp3"
    pause 3.0
    hide diana1
    show diana3:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    diana "........."
    diana ".................."
    diana "................................."
    hide diana3
    show diana5:
        align (0.01, 2.5)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di205.mp3"
    diana "Ну вот, ты не успел."
    show diana5:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio92.flac" 
    skoof "Прости, милая. Мы можем попробовать ещё раз?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio73.flac"
    inner "ДА У ТЕБЯ РЕАКЦИЯ, КАК У..."
    stop audio
    play audio "another_attempt/audio/voice_skoof/audio93.flac" 
    skoof "А ну..!"
    stop audio
    hide diana5
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di206.mp3"
    diana "Да нет, не нужно."
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio94.flac" 
    skoof "Не нужно? Но как же, значит ты ко мне не приедешь?"
    stop audio
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di207.mp3"
    diana "Конечно приеду."
    play audio "another_attempt/audio/voice_diana/di208.mp3"
    diana "Просто..."
    diana ".................."
    stop music fadeout 1.5
    play music dianabambam fadein 2.0
    play audio "another_attempt/audio/sound/xrust.mp3"
    pause 1.0
    show diana4:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio95.flac" 
    skoof "Что случилось?"
    stop audio
    hide diana4
    show diana8:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di209.mp3"
    diana "Что случилось?"
    play audio "another_attempt/audio/voice_diana/di210.mp3"
    diana "Да ничего не случилось."
    play audio "another_attempt/audio/sound/xrust.mp3"
    pause 1.0
    diana "............."
    diana "............................."
    show diana8:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio96.flac" 
    skoof "С тобой всё хорошо?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio74.flac"
    inner "ПОШЛО-ПОЕХАЛО!"
    stop audio
    show diana8:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di211.mp3"
    diana "Да, всё со мной хорошо."
    play audio "another_attempt/audio/voice_diana/di212.mp3"
    diana "Я в порядке, я........."
    diana "........................"
    play audio "another_attempt/audio/voice_diana/di213.mp3"
    diana "Скуф"
    play audio "another_attempt/audio/voice_diana/di214.mp3"
    diana "Скажи, ты знаешь про синдром «чужой» руки?"
    show diana8:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof/audio97.flac" 
    skoof "Нет. Что это такое?"
    stop audio
    play audio "another_attempt/audio/voice_inner/audio75.flac"
    inner "ЭТО КОГДА ЧУЖУЮ РУКУ ЗАСОВЫВАЮТ В ТВОЙ КАРМАН, А ПОТОМ КАТАЮТ ШАРЫ."
    stop audio
    play audio "another_attempt/audio/voice_inner/audio76.flac"
    inner "КАК В БОУЛИНГЕ!"
    stop audio
    show diana8:
        align (0.01, 2.5)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_diana/di215.mp3"
    diana "Психоневрологическое расстройство."
    play audio "another_attempt/audio/voice_diana/di216.mp3"
    diana "Человеческие конечности начинают действовать сами по себе, вне зависимости от желания хозяина. Причин возникновения достаточно много."
    play audio "another_attempt/audio/voice_diana/di217.mp3"
    diana "Такое действительно может встречаться, но я видела это только в фильмах."
    play audio "another_attempt/audio/voice_diana/di218.mp3"
    diana "И... думала, что у меня нет никаких расстройств..."
    play audio "another_attempt/audio/voice_diana/di219.mp3"
    diana "Но кажется..."
    scene expression "uslugi/bg-black.png"
    with fade
    pause 4.0
    scene expression "another_attempt/images/diana/cg-nygdeze.png":
        yalign 0.5
        xalign 0.5
    with fade
    play audio "another_attempt/audio/sound/scary.mp3"
    pause 3.0
    play sound tuntunsahur
    play audio "another_attempt/audio/voice_diana/di220.mp3"
    diana "Н...нет..."
    play audio "another_attempt/audio/voice_diana/di221.mp3"
    diana "Руки..."
    play audio "another_attempt/audio/voice_diana/di222.mp3"
    diana "Не мои руки..."
    play audio "another_attempt/audio/voice_diana/di223.mp3"
    diana "Я...я нормальная"
    play audio "another_attempt/audio/voice_diana/di224.mp3"
    diana "Они"
    diana ".........."
    diana "...................."
    diana ".............................."
    play audio "another_attempt/audio/voice_diana/di225.mp3"
    diana "Нет..."
    play audio "another_attempt/audio/voice_diana/di226.mp3"
    diana "НЕТ!"
    play audio "another_attempt/audio/voice_diana/di227.mp3"
    diana "Не делай...не трогай..."
    play audio "another_attempt/audio/voice_diana/di228.mp3"
    diana "НЕ ДЕЛАЙ!"
    play audio "another_attempt/audio/voice_diana/di229.mp3"
    diana "ПОЖАЛУЙСТА, НЕ ДЕЛАЙ ЭТО!!!"
    play audio "another_attempt/audio/voice_diana/di230.mp3"
    diana "НЕ ТРОГАЙ..."
    play audio "another_attempt/audio/voice_diana/di231.mp3"
    diana "НЕ ТРОГАЙ...МОЁ...ЛИЦО!!!!!!!!!!!!!!!"
    play audio "another_attempt/audio/sound/facebye.mp3"
    stop music
    stop sound
    show cg-nygdegeruchki
    with Fade(0.5, 1.0, 0.5, color="#FF00AA")
    play audio "another_attempt/audio/sound/krik.mp3"
    pause 9.0
    if 3 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_face:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_face
        with moveouttop
        $ achievements.remove(3)
    scene expression "uslugi/bg-black.png"
    with fade
    ".................."
    "................................"
    play audio "another_attempt/audio/voice_inner/audio77.flac"
    inner "СКУФ, КОНЕЧНО, НЕ УМЕР ОТ ИНФОРКТА ПОСЛЕ УВИДИННОГО, НО НЕПРИЯТНЫЙ ОСАДОК ОСТАЛСЯ."
    stop audio
    scene expression "uslugi/bg-wallpaper.png"
    with fade
    play audio "another_attempt/audio/voice_skoof/audio98.flac" 
    skoof "Ну нахер."
    stop audio
    jump titles
    
    return

## === Надежда ===
label mod_nadya:
    ## Dev. tip: Этот код блокирует возможность вернуться к выбору альтушки, также открывает возможность вернуть классический состав альтушек
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    $ within_selection = False
    $ config.rollback_enabled = True
    ##

    show nadya4:
        linear .5 xalign 0.5 zoom 1.0
    hide polina6
    hide diana6
    with dissolve
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na5.flac"
    nadya "Так значит ты выбрал меня?"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na6.flac"
    nadya "Даже удивительно."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na7.flac"
    nadya "Очень рада знакомству."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio1.flac"
    skoof "А что в этом удивительного?"
    stop audio    
    hide nadya1
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na8.flac"
    nadya "Не каждому по душе приходится девушка байкер."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na9.flac"
    nadya "И всё из-за тупых стереотипов."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio1.flac"
    inner "НЕ УДИВИТЕЛЬНО."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio2.flac"
    skoof "Так значит ты не из тех байкеров, которые дебоширят, промышляют криминалом, и ты не бородатый накаченный мужик, сидящий по ту сторону?"
    stop audio
    hide nadya5
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na10.flac"
    nadya "Издеваешься надо мной? В каком фильме ты это посмотрел?"
    stop audio
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio3.flac"
    skoof "Нет, что ты."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio4.flac"
    skoof "Просто... сложно уже чему-то доверять."
    stop audio
    hide nadya6    
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na11.flac"
    nadya "Не беспокойся."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na12.flac"
    nadya "Надеюсь, я тебя не разочарую."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio2.flac"
    inner "А МЫ-ТО КАК НАДЕЕМСЯ!"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na13.flac"
    nadya "Давай заполним немного документов, а в процессе узнаем друг друга получше."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio3.flac"
    inner "КАК-ТО ВСЁ ГЛАДКО, ДРУЖИЩЕ, НЕ НАХОДИШЬ?!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio5.flac"
    skoof "Что опять не так? Чем она тебе так не нравится?"
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio4.flac"
    inner "ДА НЕВООРУЖЕННЫМ ГЛАЗОМ ВИДНО, КАК ОНА ВРЁТ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio6.flac"
    skoof "А по мне она очень милая, даже при совей брутальности."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio5.flac"
    inner "ПРИПОМНИШЬ ЕЩЁ МОИ СЛОВА."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na14.flac"
    nadya "Мистер Скуф?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio7.flac"
    skoof "Прости пожалуйста, я немного отвлёкся."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na15.flac"
    nadya "Всё нормально. Просто выбери интересующий тебя раздел."
    stop audio
    $ act2_loop_visited = set()
    jump mod_nadya_loop

    return

label mod_nadya_loop:
    menu:
        set act2_loop_visited
        "Здоровье":
            jump mod_nadya_health
        set act2_loop_visited
        "Семья":
            jump mod_nadya_family
        set act2_loop_visited
        "Штрафы и налоги":
            jump mod_nadya_finesandtaxes
        set act2_loop_visited
        "Регистрация и паспорт":
            jump mod_nadya_registrationandpassport

    if nadyafalse:
        jump mod_nadya_goodfinale
    else:
        jump mod_nadya_verigoodfinale
    return

label mod_nadya_health:
    scene expression "uslugi/bg-su-health.png"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na16.flac"
    nadya "Да уж, здоровье – максимально важная часть в нашем деле."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio8.flac"
    skoof "В «нашем деле»?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na17.flac"
    nadya "Ну да."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na18.flac"
    nadya "Знаешь как много людей получают травмы на мотокроссах?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio9.flac"
    skoof "Подожди, разве байкеры участвуют в мотокроссе?"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio10.flac"
    skoof "Тогда ты должна называть себя мотоциклисткой."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio11.flac"
    skoof "Это ведь два разных понятия, я не прав?"
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na19.flac"
    nadya "О-о, так ты знаешь."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na20.flac"
    nadya "Безусловно ты прав, но не совсем."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na21.flac"
    nadya "Да, я люблю быструю езду, но не для того, чтобы просто участвовать в соревнованиях или быстро доехать куда-то."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na22.flac"
    nadya "Для меня байк – это жизнь."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na23.flac"
    nadya "Покатушки на ДОПах, открытие и закрытие сезона, тусовки в клубах."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na24.flac"
    nadya "И байк мой кастомный. Не простила себя, если б не сделала его сама."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio6.flac"
    inner "ТАК ОНА ЕЩЁ И АВТОМЕХАННИК!"
    stop audio
    hide nadya1
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na25.flac"
    nadya "И всё же некоторым моим знакомым не по душе моя страсть к скорости."
    stop audio
    hide nadya6
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na26.flac"
    nadya "Поэтому... и кличка соответствующая."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio12.flac"
    skoof "Какая?"
    stop audio
    hide nadya1
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na27.flac"
    nadya "Можно я не буду говорить?"
    stop audio
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio13.flac"
    skoof "Конечно."
    stop audio
    hide nadya2
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    nadya "......"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio14.flac"
    skoof "Не знал, что всё настолько... запутанно."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na28.flac"
    nadya "Может быть."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na29.flac"
    nadya "В любом случае теперь ты знаешь разницу."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na30.flac"
    nadya "Но что-то мы отошли от темы."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na31.flac"
    nadya "Как я и сказала риск для жизни очень большой."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na32.flac"
    nadya "Даже не знаю сколько раз я лежала в больнице с переломами."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na33.flac"
    nadya "Правду говорят: «Тише едешь – дольше едешь»."
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio7.flac"
    inner "ТАМ БЫЛО ПО-ДРУГОМУ!"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na34.flac"
    nadya "Ты, кстати, как к этому вообще относишься?"
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na35.flac"
    nadya "Может тебе это и не интересно, а я стою тут, рассказываю."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio15.flac"
    skoof "Да я и сам не против прокатиться."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na36.flac"
    nadya "У тебя есть байк?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio16.flac"
    skoof "Есть."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na37.flac"
    nadya "Пф, не думала, что мы можем сойтись в интересах."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na38.flac"
    nadya "Тогда погоняем как-нибудь?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio17.flac"
    skoof "Не думаю, что мне нравится быстро гонять."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio8.flac"
    inner "ТЕБЕ НРАВИТСЯ ГОНЯТЬ НЕ ЗА РУЛЁМ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio18.flac"
    skoof "А ну цыц!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio19.flac"
    skoof "Я бы просто спокойно покатался."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na39.flac"
    nadya "Ну или так."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na40.flac"
    nadya "Но мы снова отвлеклись."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na41.flac"
    nadya "Давай по-быстрому. Есть проблемы со спиной, сердцем или ЗППП?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio20.flac"
    skoof "Да вроде нет..."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio21.flac"
    skoof "Только если со спиной..."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na42.flac"
    nadya "Хм, что ж, я думаю это не сильно на что-то повлияет."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na43.flac"
    nadya "Раз остальных проблем нет, давай продолжим."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "И это всё? Так просто? Без всяких бумажек?"
    "Ещё несколько секунд ты не веришь, что так легко прошёл этот пункт."
    jump mod_nadya_loop
    return

label mod_nadya_family:
    scene expression "uslugi/bg-su-fam.png"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na44.flac"
    nadya "Семья."
    stop audio
    hide nadya1
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na45.flac"
    nadya "Как думаешь, хотеть создать семью глупо?"
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio22.flac"
    skoof "Вовсе нет."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na46.flac"
    nadya "Вот и я так думаю."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio23.flac"
    skoof "Тогда почему спрашиваешь?"
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na47.flac"
    nadya "Не знаю. Возможно, у меня просто никогда не было настоящей семьи."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na48.flac"
    nadya "В какой-то степени мои товарищи мне тоже как семья..."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na49.flac"
    nadya "Но это всё не то. Они считают я должна быть свободной, раз уж я в их группе."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na50.flac"
    nadya "И что же, быть счастливой можно только на байке?"
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio24.flac"
    skoof "Нет, что ты."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio25.flac"
    skoof "Семья это и впрямь счастье. Но счастье никогда не вечно."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    nadya "........."
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio26.flac"
    skoof "Слушай, почему ты вообще сидишь на этом сайте?"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio27.flac"
    skoof "Разве ты не находишься в кругу таких же людей, только в несколько раз круче?"
    stop audio
    hide nadya5
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na51.flac"
    nadya "Ну разве что их крутость состоит в четырёх бокалах пива."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na52.flac"
    nadya "Меня может и уважают, но не все считают езду на байке «бабьим делом»."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na53.flac"
    nadya "В таком случае проще расстаться с мужиком, чем с байком."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na54.flac"
    nadya "В остальных, больше, чем друзей, я не вижу."
    stop audio
    hide nadya6
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na55.flac"
    nadya "Парни-нормисы больше комплексуют, что женщина в разы круче их, да и все говорят, что татуировки мои стрёмные."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na56.flac"
    nadya "Будто я не девушка, а монстр."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na57.flac"
    nadya "Вот и другого выбора у меня не остаётся."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio28.flac"
    skoof "Всегда смазливые парни упускают самое лучшее."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio29.flac"
    skoof "Кто в здравом уме откажется от сильной, мужественной и ухоженной женщины, которая в отношениях будет и милой, заботливой девушкой, покатающей тебя с ветерком"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio30.flac"
    skoof "И властной и грубой в постели."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio9.flac"
    inner "АГА-А-А, ВСЁ-ТАКИ ФЕТИШИСТ!!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio31.flac"
    skoof "Ну всё, надоел, нет чтоб пару минут не возникать!?"
    stop audio
    hide nadya5
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na58.flac"
    nadya "Прости, что?"
    stop audio
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio32.flac"
    skoof "Нет, извини, это я не тебе."
    stop audio
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na59.flac"
    nadya "Сделаю вид, что не слышала этого."
    stop audio
    hide nadya6
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na60.flac"
    nadya "Спасибо..."
    stop audio
    nadya "..........."
    play audio "another_attempt/audio/voice_nadya/na61.flac"
    nadya "Хоть кто-то увидел во мне настоящую женщину."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na62.flac"
    nadya "Но..."
    stop audio
    hide nadya2
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na63.flac"
    nadya "Седло мотоцикла сближает быстрее, чем постель, учти это."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio33.flac"
    skoof "Может быть."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na64.flac"
    nadya "Не спорь с женщиной, у которой в руках разводной ключ."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio10.flac"
    inner "ЭТО ОНА НАМ СЕЙЧАС УГРОЖАЕТ?!"
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na65.flac"
    nadya "А что насчёт тебя?"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na66.flac"
    nadya "У тебя есть семья, Скуф?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio34.flac"   
    skoof "Есть...была."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio35.flac"
    skoof "Не люблю затрагивать эту тему."
    stop audio
    hide nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na67.flac"
    nadya "Что ж, смотрю ты не замужем, этого достаточно."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na68.flac"
    nadya "Можем двигаться дальше, выбирай категорию."
    stop audio

    jump mod_nadya_loop
    return

label mod_nadya_finesandtaxes:
    scene expression "another_attempt/images/bg-finesandtaxes.png":
        subpixel True
        zoom 0.5
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na69.flac"
    nadya "Штрафы и налоги."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na70.flac"
    nadya "Хм, думаю, это важный раздел."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na71.flac"
    nadya "Надеюсь у тебя нет неоплаченных штрафов, особенно со всем, что касается мотоцикла?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio36.flac"
    skoof "Да не то, чтобы я на нём часто ездил."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio37.flac"
    skoof "Почему тебя это так интересует?"
    stop audio
    hide nadya1
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na72.flac"
    nadya "Я ненавижу аутло, которое нарушает нашу идиллию и гоняет на ДОПах, забив на правила."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na73.flac"
    nadya "Да и коробочники хороши бывают."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na74.flac"
    nadya "На коробках разъезжают, будто на ракете."
    stop audio
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio11.flac"
    inner "СТРАННЫЙ У НЕЁ СЛЕНГ."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio38.flac"
    skoof "Подожди, разве ты не говорила, что сама любишь быстро ездить?"
    stop audio
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na75.flac"
    nadya "Но не на общих дорогах же."
    stop audio
    hide nadya3
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na76.flac"
    nadya "Да, я могу быстро ездить, но только чтобы от этого не пострадали другие, а эти..."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na77.flac"
    nadya "Лучше в 9 дома, чем в 8 в морге."
    stop audio
    hide nadya6
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na78.flac"
    nadya "Пусть это и не про меня."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio12.flac"
    inner "ОНА МЕНЯ ЗАПУТАЛА."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio13.flac"
    inner "НЕ ЛЮБИТ, КОГДА ДРУГИЕ ЕЗДЯТ БЫСТРО, А САМОЙ И В МОРГ ПОПАСТЬ НЕ ЖАЛКО?!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio39.flac"
    skoof "Ты противоречишь сама себе."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na79.flac"
    nadya "Разве?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio40.flac"
    skoof "Тебе нравится быстро ездить, и тебе всё равно, что с тобой будет, но когда так делают другие, ты это осуждаешь"
    stop audio
    hide nadya4
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na80.flac"
    nadya "Я же сказала, что я осуждаю, когда так делают на общих дорогах."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na81.flac"
    nadya "Мне всё равно что будет с этими однопроцентниками вне города или где-либо ещё, где нет людей."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na82.flac"
    nadya "Нельзя нарушать покой других, это банальное неуважение."
    stop audio
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio14.flac"
    inner "ЖЕ-Е-ЕНЩИНЫ."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio41.flac"
    skoof "Видимо, до женской логики мне ещё далеко."
    stop audio
    hide nadya3
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na83.flac"
    nadya "Ха-ха, ладно, проехали."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na84.flac"
    nadya "Так что, у тебя есть неоплаченные штрафы или налоги?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Ты глубоко задумываешься..."
    "Что и где ты мог сделать не так?"
    "Вроде бы не убивал и не воровал."
    play audio "another_attempt/audio/voice_inner_nadya/audio15.flac"
    inner "И ПОСЛЕДНЕЕ ВРЕМЯ УЖ ТОЧНО НЕ ПРЕЛЮБОДЕЙСТВОВАЛ!"
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio16.flac"
    inner "ВЕРНЕЕ СКАЗАТЬ: ОЧЕНЬ ДАВНО НЕ ПРЕЛЮБОДЕЙСТВОВАЛ!"
    stop audio
    "Кажется, девять заповедей имеют мало общего с кодексом об административных правонарушениях."
    "Так, что же там было..."
    "Возможно, пару раз перешёл дорогу в неположенном месте."
    "Разок-другой припарковался там, где парковаться запрещено."
    "Бывало, мог дёрнуть пивка в общественных местах."
    "И после этого грешным делом нанести урон чужому имуществу."
    "Байкеры ведь тоже так делают?"
    "Наверное, можно и не говорить."
    play audio "another_attempt/audio/voice_inner_nadya/audio17.flac"
    inner "ФЕТИШИСТ-ОБМАНЩИК!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio42.flac"
    skoof "Я безгрешен."
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na85.flac"
    nadya "Никто не безгрешен."
    stop audio
    hide  nadya4
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na86.flac"
    nadya "Жги шины, а не душу. У тебя точно нет правонарушений?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Нет, нету (соврать)":
            $ nadyafalse = True
            show nadya1:
                align (0.5, 1.0)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_nadya/na87.flac"
            nadya "Хорошо, я тебе верю."
            stop audio
            show nadya1:
                align (0.5, 1.0)
                subpixel True
                linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            jump mod_nadya_loop

        "Ну, может есть, парочку (сказать правду)":
            $ nadyafalse = False
            show nadya1:
                align (0.5, 1.0)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_nadya/na88.flac"
            nadya "Что ж, спасибо, что сказал правду."
            stop audio
            play audio "another_attempt/audio/voice_nadya/na89.flac"
            nadya "Но не беспокойся, у тебя не висит ни одного штрафа."
            stop audio
            play audio "another_attempt/audio/voice_nadya/na90.flac"
            nadya "Продолжим."
            stop audio
            show nadya1:
                align (0.5, 1.0)
                subpixel True
                linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
            jump mod_nadya_loop

    jump mod_nadya_loop
    return

label mod_nadya_registrationandpassport:
    scene expression "uslugi/bg-su-reg.png"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na91.flac"
    nadya "Фух, остался последний раздел."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na92.flac"
    nadya "Может у тебя остались какие-то вопросы ко мне?"
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio43.flac"
    skoof "Вроде бы нет."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio44.flac"
    skoof "Честно, я удивлён, что всё прошло так гладко, без всяких подозрительных вещей."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio18.flac"
    inner "МЫ ЕЩЁ НЕ ЗАКОНЧИЛИ!!"
    stop audio
    hide nadya1
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na93.flac"
    nadya "Что ты имеешь ввиду?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio45.flac"
    skoof "Сколько бы раз я сюда не заходил, вечно меня обманывают с этими альтушками."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio46.flac"
    skoof "Может быть ты тоже этот... как его..."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio19.flac"
    inner "ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ!"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio47.flac"
    skoof "Да, именно, искусственный интеллект."
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio48.flac"
    skoof "Зачем я тогда вообще трачу на это время?"
    stop audio
    hide nadya4
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    nadya "......"
    play audio "another_attempt/audio/voice_nadya/na94.flac"
    nadya "Я обещала ей не рассказывать, но..."
    stop audio
    hide nadya2
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na95.flac"
    nadya "Думаю, мне не стоит объяснять, почему ты не должен никому верить."
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio20.flac"
    inner "НУ НАЧАЛО-О-О-СЬ!!!"
    stop audio
    hide nadya4
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na96.flac"
    nadya "Но говоря о нас троих..."
    stop audio
    hide nadya2
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na97.flac"
    nadya "В общем, если вдруг решишь выбрать другую..."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na98.flac"
    nadya "Ни в коем случае не выбирай Полину."
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio49.flac"
    skoof "Это ещё почему?"
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na99.flac"
    nadya "Не могу точно объяснить..."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na100.flac"
    nadya "Она не искусственный интеллект..."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na101.flac"
    nadya "А что-то... другое..."
    stop audio
    hide nadya4
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na102.flac"
    nadya "Не пойми неправильно, я люблю Полину, как подругу, и только благодаря ей я здесь."
    stop audio
    hide nadya2
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na103.flac"
    nadya "Но поверь, доверишься ей и проблем не оберёшься."
    stop audio
    show nadya4:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio50.flac"
    skoof "И почему я должен тебе поверить?"
    stop audio
    play audio "another_attempt/audio/voice_skoof_nadya/audio51.flac"
    skoof "Выходит, она не такая уж и плохая."
    stop audio
    hide nadya4
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na104.flac"
    nadya "Я понимаю, как это выглядит."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na105.flac"
    nadya "Но прошу поверь."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na106.flac"
    nadya "Меня здесь и быть вовсе не должно."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na107.flac"
    nadya "Полина взломала систему и зарегистрировала меня, как одну из альтушек, потому что я реальный человек."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na108.flac"
    nadya "У меня вовсе нет целей навредить тебе, в отличие от неё."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na109.flac"
    nadya "А что касается Дианы..."
    stop audio
    hide nadya5
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na110.flac"
    nadya "Ох, как я не люблю плохо о них говорить."
    stop audio
    hide nadya2
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na111.flac"
    nadya "Короче, Диане тоже лучше не верить."
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skoof_nadya/audio52.flac"
    skoof "Но ты ведь доверяешь Полине, так почему я не могу?"
    stop audio
    hide nadya5
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na112.flac"
    nadya "У нас... хорошие отношения, но это никак не влияет на её действия."
    stop audio
    show nadya2:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_nadya/audio21.flac"
    inner "Я УЖЕ ЗАПУТАЛСЯ ГДЕ ПРАВДА, А ГДЕ НЕТ!"
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio22.flac"
    inner "ГОВОРИЛ ВЕДЬ, МУТНАЯ ОНА!"
    stop audio
    hide nadya2
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na113.flac"
    nadya "Я просто пытаюсь тебя предостеречь."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na114.flac"
    nadya "Ты веришь мне, Скуф?"
    stop audio
    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Я верю тебе":
            play audio "another_attempt/audio/voice_skoof_nadya/audio53.flac"
            skoof "Я верю."
            stop audio
            hide nadya5
            show nadya2:
                align (0.5, 1.0)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
            play audio "another_attempt/audio/voice_nadya/na117.flac"
            nadya "Спасибо."
            stop audio
        "Нет, я тебе не верю":
            jump mod_nadya_bad

    jump mod_nadya_loop
    return

# === КОНЦОВКИ ===
label mod_nadya_bad:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Ну и пошел ты, Мудак!")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    show nadya5:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/sound/what.mp3"
    pause 2.0
    nadya "........."
    nadya "................."
    hide nadya5
    show nadya3:
        align (0.5, 1.0)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na115.flac"
    nadya "Относишься к мужикам по-хорошему, а они как всегда!"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na116.flac"
    nadya "Ну и пошёл ты, мудак!"
    stop audio
    stop music
    scene expression "uslugi/bg-black.png"
    with fade
    if 6 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_mydak:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_mydak
        with moveouttop
        $ achievements.remove(6)
    jump titles

    return

label mod_nadya_goodfinale:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("Мотобратство")
    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    
    scene expression "uslugi/bg-su.png"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na118.flac"
    nadya "Мы закончили."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na119.flac"
    nadya "Теперь просто дай мне свой адрес, и я приеду."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/skna54.flac"
    skoof "Ты же точно не бородатый накаченный мужик, сидящий по ту сторону?"
    stop audio
    hide nadya1
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na120.flac"
    nadya "Знаешь, что бывает за такие шутки?"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na121.flac"
    nadya "Я, по-твоему, просто так обо всём рассказала?"
    stop audio
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/skna55.flac"
    skoof "Понял..."
    stop audio
    hide nadya6
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na122.flac"
    nadya "Тогда я выезжаю."
    stop audio
    scene cg-nadyaandskoof
    with fade
    stop music fadeout 0.5

    ## Dev. tip: Изменение стиля на домашний
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    if 5 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_motobrat:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_motobrat
        with moveouttop
        $ achievements.remove(5)
    play audio "another_attempt/audio/voice_inner_nadya/audio23.flac"
    inner "ПОСЛЕ ВСТРЕЧИ С НАДЕЙ, ЖИЗНЬ СКУФА ДЕЙСТВИТЕЛЬНО ИЗМЕНИЛАСЬ, НО НЕ СИЛЬНО.ПОЧТИ С ПЕРВОГО СЛОВА ОНИ НАШЛИ ОБЩИЙ ЯЗЫК."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio24.flac"
    inner "НАДЯ, ХОТЬ И НЕ БЫЛА ДОСТАТОЧНО ЧИСТОПЛОТНОЙ, АККУРАТНОЙ, НЕ УМЕЛА ГОТОВИТЬ, НО ЕЁ ДОБРОЕ СЕРДЦЕ И МУЖЕСТВЕННАЯ НАТУРА ЗАСТАВЛЯЛИ СКУФА УВАЖАТЬ ЕЁ."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio25.flac"
    inner "ОНИ КАТАЛИСЬ ПО ГОРОДУ НА МОТОЦИКЛАХ, ПИЛИ ПИВО И, НАУДИВЛЕНИЕ, ЗАНЯЛИСЬ СПОРТОМ."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio26.flac"
    inner "ПРАВДА, ВИДЫ СПОРТА, КОТОРЫЕ ПРЕДПОЧИТАЛА НАДЯ, ОКАЗАЛИСЬ СЛИШКОМ ЭКСТРИМАЛЬНЫМИ ДЛЯ СКУФА."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio27.flac"
    inner "ПОЭТОМУ, ПОСЛЕ ПЕРВОГО ПРЫЖКА С ПАРАШУТА И ПОСЛЕ ПЕРВОГО ИНСУЛЬТА, ОН ЗАБРОСИЛ."
    stop audio
    
    hide cg-nadyaandskoof
    $ renpy.movie_cutscene("another_attempt/images/nadya/cg-nadyaandskoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    play audio "another_attempt/audio/voice_inner_nadya/audio28.flac"
    inner "ЧТО, ДУМАЕТЕ ТАК НЕ БЫЛО?"
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio29.flac"
    inner "ЗРЯ!"
    stop audio

    jump titles
    return

label mod_nadya_verigoodfinale:
    ## Dev. tip: Добавление концовки в список разблокированных
    $ persistent.unlocked_endings.add("140 скорость на край света!")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    scene expression "uslugi/bg-su.png"
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na118.flac"
    nadya "Мы закончили."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na119.flac"
    nadya "Теперь просто дай мне свой адрес, и я приеду."
    stop audio
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/skna54.flac" 
    skoof "Ты же точно не бородатый накаченный мужик, сидящий по ту сторону?"
    hide nadya1
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na120.flac"
    nadya "Знаешь, что бывает за такие шутки?"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na121.flac"
    nadya "Я, по-твоему, просто так обо всём рассказала?"
    stop audio
    show nadya6:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/skna55.flac"
    skoof "Понял..."
    hide nadya6
    show nadya1:
        align (0.5, 1.0)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_nadya/na122.flac"
    nadya "Тогда я выезжаю."
    stop audio
    scene expression "uslugi/bg-black.png"
    with fade
    play audio "another_attempt/audio/sound/dzin.mp3"
    pause 3.0
    scene cg-nadyaandskoof
    with fade
    stop music fadeout 0.5

    ## Dev. tip: Изменение стиля на домашний
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"

    play audio "another_attempt/audio/voice_inner_nadya/audio23.flac"
    inner "ПОСЛЕ ВСТРЕЧИ С НАДЕЙ, ЖИЗНЬ СКУФА ДЕЙСТВИТЕЛЬНО ИЗМЕНИЛАСЬ, НО НЕ СИЛЬНО.ПОЧТИ С ПЕРВОГО СЛОВА ОНИ НАШЛИ ОБЩИЙ ЯЗЫК."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio24.flac"
    inner "НАДЯ, ХОТЬ И НЕ БЫЛА ДОСТАТОЧНО ЧИСТОПЛОТНОЙ, АККУРАТНОЙ, НЕ УМЕЛА ГОТОВИТЬ, НО ЕЁ ДОБРОЕ СЕРДЦЕ И МУЖЕСТВЕННАЯ НАТУРА ЗАСТАВЛЯЛИ СКУФА УВАЖАТЬ ЕЁ."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio25.flac"
    inner "ОНИ КАТАЛИСЬ ПО ГОРОДУ НА МОТОЦИКЛАХ, ПИЛИ ПИВО И, НАУДИВЛЕНИЕ, ЗАНЯЛИСЬ СПОРТОМ."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio26.flac"
    inner "ПРАВДА, ВИДЫ СПОРТА, КОТОРЫЕ ПРЕДПОЧИТАЛА НАДЯ, ОКАЗАЛИСЬ СЛИШКОМ ЭКСТРИМАЛЬНЫМИ ДЛЯ СКУФА."
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio27.flac"
    inner "ПОЭТОМУ, ПОСЛЕ ПЕРВОГО ПРЫЖКА С ПАРАШУТА И ПОСЛЕ ПЕРВОГО ИНСУЛЬТА, ОН ЗАБРОСИЛ."
    stop audio
    
    hide cg-nadyaandskoof
    $ renpy.movie_cutscene("another_attempt/images/nadya/cg-nadyaandskoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    play audio "another_attempt/audio/voice_inner_nadya/audio28.flac"
    inner "ЧТО, ДУМАЕТЕ ТАК НЕ БЫЛО?"
    stop audio
    play audio "another_attempt/audio/voice_inner_nadya/audio29.flac"
    inner "ЗРЯ!"
    stop audio
    scene expression "another_attempt/images/nadya/cg-nadyagrinch.png":
        zoom 0.35
    with fade
    play music gorod
    nadya "..."
    play audio "another_attempt/audio/voice_nadya/na123.flac"
    nadya "Проснулся? М-да, все будильники проспал."
    stop audio
    play audio "another_attempt/audio/skna56.flac"
    skoof "Прости, милая, больше не буду так поздно засиживаться."
    stop audio
    play audio "another_attempt/audio/voice_nadya/na124.flac"
    nadya "*вздох*"
    stop audio
    play audio "another_attempt/audio/voice_nadya/na125.flac"
    nadya "Хорошо. И не называй меня так больше."
    stop music fadeout 2.0
    if 8 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_speed:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_speed
        with moveouttop
        $ achievements.remove(8)

    jump titles
    return

## === Полина ===
label mod_polina:
    ## Dev. tip: Этот код блокирует возможность вернуться к выбору альтушки, также открывает возможность вернуть классический состав альтушек
    $ renpy.force_autosave()
    $ renpy.block_rollback()
    $ within_selection = False
    $ config.rollback_enabled = True

    show polina6:
        linear .5 xalign 0.5 zoom 1.0
    hide nadya4
    hide diana6
    with dissolve

    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po6.flac"
    polina "Так ты говоришь, что твой знак зодиака - это овен?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po1.flac"
    skoof "Я ничего не говорил..."
    stop audio
    hide polina6 
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po7.flac"
    polina "А, ну да, я просто посмотрела это в твоей базе данных."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po2.flac"
    skoof "Разве я давал разрешение на её использование?"
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po8.flac"
    polina "Нет."
    play audio "another_attempt/audio/voice_polina/po9.flac"
    polina "В любом случае, ты не получишь альтушку, если не дашь доступ к своим данным и не заполнишь пару пунктов."
    play audio "another_attempt/audio/voice_polina/po10.flac"
    polina "Ты ведь здесь для этого?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio1.flac"
    inner "ЧТО? ОПЯТЬ ЗАПОЛНЯТЬ ДОКУМЕНТЫ?!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po3.flac"
    skoof "Опять заполнять..."
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po11.flac"
    polina "Да-да, я знаю как это муторно."
    play audio "another_attempt/audio/voice_polina/po12.flac"
    polina "Но даже со своими умениями, я не способна обойти эту систему."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po4.flac"
    skoof "Твоими умениями?"
    stop audio
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po13.flac"
    polina "Ну знаешь... покопаться в коде, немного изменить работу сайта."
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po14.flac"
    polina "Я могу сделать всё сама, но я ведь многого не знаю о тебе."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po15.flac"
    polina "Вдруг я решу указать тебе в пункте “здоровье” ВИЧ"
    play audio "another_attempt/audio/voice_polina/po16.flac"
    polina "Тогда альтушку ты точно не получишь."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po5.flac"
    skoof "Не очень смешно..."
    stop audio
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po17.flac"
    polina "Да?..."
    play audio "another_attempt/audio/voice_polina/po18.flac"
    polina "Ну прости, не знала, что ты такой нежный."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio2.flac"
    inner "НЕ ПОЙМУ, ОНА СМЕЁТСЯ НА НАМИ!?"
    stop audio
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po19.flac"
    polina "Эх, давай побыстрее закончим с этим."
    hide polina5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po20.flac"
    polina "Для завершения процедуры оформления альтушки тебе необходимо заполнить ряд документов..."
    play audio "another_attempt/audio/voice_polina/po21.flac"
    polina "Так... Вроде по тексту..."    
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "По тексту?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po22.flac"
    polina "Выбери раздел для заполнения документов."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    $ act2_loop_visited = set()
    jump mod_polina_loop    

    return

label mod_polina_loop:

    menu:
        set act2_alts_visited
        "Справки и выписки":
            jump mod_polina_certificatesandextracts
        set act2_alts_visited
        "Штрафы и налоги":
            jump mod_polina_finesandtaxes
        set act2_loop_visited
        "Здоровье":
            jump mod_polina_health
        set act2_loop_visited
        "Регистрация и паспорт":
            jump mod_polina_registrationandpassport

    return

label mod_polina_certificatesandextracts:
    scene expression "uslugi/bg-su-sprav.png"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po23.flac"
    polina "Справки и выписки..."
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po24.flac"
    polina "Ме... так лень..."
    play audio "another_attempt/audio/voice_polina/po25.flac"
    polina "Слушай, а может оно тебе и вовсе не надо?"
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio3.flac"
    inner "КАК ЭТО НЕ НАДО?!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po6.flac"
    skoof "Я пришёл сюда за альтушкой..."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po7.flac"
    skoof "Поэтому давай, говори, что нужно заполнить."
    stop audio
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po26.flac"
    polina "Ммм... трудовая книжка... справки есть..."
    play audio "another_attempt/audio/voice_polina/po27.flac"
    polina "Значит так..."
    hide polina5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po28.flac"
    polina "Я всё сделаю, а пока я подгружаю данные, расскажи мне что-нибудь."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Рассказать что-нибудь?"
    "Что я могу рассказать молодой девушке?"
    "Может про танки?"
    "Или она любит научные факты?"
    "Кажется, она упоминала, что разбирается в технике..."
    "Но прежде, чем ты успел подумать, голос девушки привёл тебя в реальность."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po29.flac"
    polina "Ау, я с кем говорю?"
    play audio "another_attempt/audio/voice_polina/po30.flac"
    polina "Видимо, собеседник из тебя такой же, как и я."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po8.flac"
    skoof "Какой?"
    stop audio
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po31.flac"
    polina "Хреновый."
    hide polina5
    show polina3:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po32.flac"
    polina "Так сложно бывает придумать тему для разговора."
    play audio "another_attempt/audio/voice_polina/po33.flac"
    polina "Даже если тебе есть что рассказать."
    hide polina3
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po34.flac"
    polina "Ладно, что это я."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po9.flac"
    skoof "Ты играешь в какие-нибудь игры?"
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po35.flac"
    polina "Шутишь что ли?"
    play audio "another_attempt/audio/voice_polina/po36.flac"
    polina "Конечно."
    play audio "another_attempt/audio/voice_polina/po37.flac"
    polina "Resident Evil, STALKER, Dota..."
    play audio "another_attempt/audio/voice_polina/po38.flac"
    polina "В общем много во что играю."
    play audio "another_attempt/audio/voice_polina/po39.flac"
    polina "Так хорошо весь день быть дома, где твой маршрут это от кровати до компа, от компа до туалета и назад на кровать."
    play audio "another_attempt/audio/voice_polina/po40.flac"
    polina "Сидишь, играешь, спишь, делаешь что хочешь, и никто тебя за это не упрекнет."
    play audio "another_attempt/audio/voice_polina/po41.flac"
    polina "Не жизнь, а сказка!"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio4.flac"
    inner "ДА ОНА В ТЕМЕ!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po10.flac"
    skoof "Ух ты... не знал, что альтушки тоже бывают нелюдимыми."
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po42.flac"
    polina "Скорее хикками."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio5.flac"
    inner "КЕМ-КЕМ?!"
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio6.flac"
    inner "ОПЯТЬ ЭТИ ЗАМУДРЕНЫЕ СЛОВЕЧКИ!"
    stop audio
    hide polina2
    show polina3:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po43.flac"
    polina "Лучше сидеть в интернете, играть в игры и общаться с ботами."
    play audio "another_attempt/audio/voice_polina/po44.flac"
    polina "Они лучше реальных людей будут."
    show polina3:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po11.flac"    
    skoof "То есть, тебе будет всё равно на меня, когда ты приедешь?"
    stop audio
    hide polina3
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po45.flac"
    polina "Ну почему."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po46.flac"
    polina "Я смотрю у нас с тобой много общих интересов."
    play audio "another_attempt/audio/voice_polina/po47.flac"
    polina "Да и что, мы только в игрушки что-ли играть будем ."
    play audio "another_attempt/audio/voice_polina/po48.flac"
    polina "Я рассчитываю на кое-что ещё... "
    play audio "another_attempt/audio/voice_polina/po49.flac"
    polina "Если ты понимаешь о чём я."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po12.flac"
    skoof "Да-а-а... понимаю."
    stop audio
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po50.flac"
    polina "Данные уже загружены."
    play audio "another_attempt/audio/voice_polina/po51.flac"
    polina "Давай перейдем к следующему разделу."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    jump mod_polina_loop
    return

label mod_polina_finesandtaxes:
    scene expression "another_attempt/images/bg-finesandtaxes.png":
        subpixel True
        zoom 0.5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po52.flac"
    polina "Штрафы и налоги."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po53.flac"
    polina "Ну-с, гражданин, нарушали?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po13.flac"
    skoof "Нет."
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po54.flac"
    polina "Врëшь."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio7.flac"
    inner "ВРЕТ И НЕ КРАСНЕЕТ, МИЛОЧКА."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po14.flac"
    skoof "Да не вру я!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po15.flac"
    skoof "Не было там никогда никаких штрафов."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po16.flac"
    skoof "И налоги я все оплачиваю."
    stop audio
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po55.flac"
    polina "Да знаю я."
    play audio "another_attempt/audio/voice_polina/po56.flac"
    polina "Давай тогда я расскажу о тебе."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po17.flac"
    skoof "Ты расскажешь обо мне?"
    stop audio
    stop audio
    play audio "another_attempt/audio/voice_skPo/po18.flac"
    skoof "Может быть наоборот?"
    stop audio
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po8.flac"
    polina "Нет."
    play audio "another_attempt/audio/voice_polina/po58.flac"
    polina "Ты ведь овен по знаку зодиака?"
    play audio "another_attempt/audio/voice_polina/po59.flac"
    polina "Это может очень многое рассказать о человеке."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po19.flac"
    skoof "То есть ты тоже веришь в эти знаки, судьбу, на картах гадаешь?"
    stop audio
    hide polina6
    show polina4:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po60.flac"
    polina "Картах?"
    hide polina4
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po61.flac"
    polina "Бред."
    play audio "another_attempt/audio/voice_polina/po62.flac"
    polina "Вот что могут сказать эти картонки?"
    play audio "another_attempt/audio/voice_polina/po63.flac"
    polina "Так ещё и шифр в них какой-то и называются бессмысленно. Попробуй разбери какая карта что значит."
    play audio "another_attempt/audio/voice_polina/po64.flac"
    polina "На заборах тоже много что пишут."
    play audio "another_attempt/audio/voice_polina/po65.flac"
    polina "Цыганки по рукам и то правдивее гадают."
    hide polina5
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po66.flac"
    polina "А вот судьбу не обманешь."
    play audio "another_attempt/audio/voice_polina/po67.flac"
    polina "Под какой звездой родился, таким человеком и будешь." 
    play audio "another_attempt/audio/voice_polina/po68.flac"
    polina "И почему это “тоже”?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po20.flac"
    skoof "Ты сама хоть поняла, что сказала?"
    stop audio
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po69.flac"
    polina "Не веришь, да?"
    play audio "another_attempt/audio/voice_polina/po70.flac"
    polina "Ну конечно, тебе же главное альтушку получить побыстрее, овны такие нетерпеливые."
    play audio "another_attempt/audio/voice_polina/po71.flac"
    polina "А что ты сделал, чтобы получить альтушку?"
    play audio "another_attempt/audio/voice_polina/po72.flac"
    polina "Бумажки разбирать овнам не нравится, работать им тоже не нравится."
    play audio "another_attempt/audio/voice_polina/po73.flac"
    polina "Даже подвох не можете заметить."
    play audio "another_attempt/audio/voice_polina/po74.flac"
    polina "Одного вам не занимать. Задумаете что-то, и добиваетесь этого любыми способами."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po75.flac"
    polina "Правда пока альтушку у тебя не получилось добиться."
    play audio "another_attempt/audio/voice_polina/po76.flac"
    polina "Какой это раз? Пятый? Ха-ха."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po21.flac"
    skoof "Ничего себе."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po22.flac"
    skoof "Смогла описать меня только по моему знаку зодиака?"
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po77.flac"
    polina "Я же говорила."
    play audio "another_attempt/audio/voice_polina/po78.flac"
    polina "А знаешь с кем у овнов самая большая совместимость по любви?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po23.flac"
    skoof "С кем?"
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po79.flac"
    polina "С близнецами."
    play audio "another_attempt/audio/voice_polina/po80.flac"
    polina "А я - близнецы, хи-хи"
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po81.flac"
    polina "Поэтому я уверена, что мы с тобой рождены друг для друга."
    hide polina2
    show polina4:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po82.flac"
    polina "Хотя, есть ещё кое-кто..."
    show polina4:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po24.flac"
    skoof "Кто же?"
    stop audio
    hide polina4
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po83.flac"
    polina "А, не важно."
    play audio "another_attempt/audio/voice_polina/po84.flac"
    polina "Ты единственный, кто мне нужен, Скуф."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po25.flac"
    skoof "Я даже как-то засмущался."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio8.flac"
    inner "А  ПО-МОЕМУ, ОНА МОЗГИ НАМ ПУДРИТ!"
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio9.flac"
    inner "ПОКА МЫ ТУТ БОЛТАЕМ, ЭТА ХАКЕРША УЖЕ ВСЕ ДАННЫЕ У НАС СКОМУНИЗДИЛА!!"
    stop audio
    "Если подумать, то почему мы ещё на этой странице."
    "У тебя нет ни штрафов, ни неуплаченных налогов."
    "Может жизненный опыт тебя так ничему не научил?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po85.flac"
    polina "Скажи, гороскопы ты тоже считаешь чушью?" 
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po26.flac"
    skoof "Ну если честно,то да."
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po86.flac"
    polina "Это всё равно не помешает мне составить для тебя гороскоп."
    play audio "another_attempt/audio/voice_polina/po87.flac"
    polina "Просто дай мне пару минут на обработку твоих данных, чтобы рассчитать всё."
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    polina "..................."
    polina ".............................."
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po27.flac" 
    skoof "И что же там?"
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio10.flac"
    inner "СЕЙЧАС ОНА НАМ ПРЕДСКАЖЕТ РОСКОШНУЮ ЖИЗНЬ!!" 
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio11.flac"
    inner "ДЕНЬГИ, АЛЬТУШКИ, ДОЛЛА-А-АРЫ!!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po28.flac" 
    skoof "Не говори ерунду, нам такое точно не светит."
    stop audio
    hide polina5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po88.flac"
    polina "Всё готово."
    play audio "another_attempt/audio/voice_polina/po89.flac"
    polina "С овнов начинается каждый новый цикл, поэтому они обожают всё новое. В это время ваша реальность перезапустится, будто кто-то нажал рестарт. Вам придется принять судьбоносные решения и переосмыслить прошлое."
    play audio "another_attempt/audio/voice_polina/po90.flac"
    polina "Как-то так."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    skoof "....."
    play audio "another_attempt/audio/voice_inner_po/audio12.flac"
    inner "ЧТО ЗА БРЕД ОНА НЕСЁТ?!"
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio13.flac"
    inner "КАКОЙ РЕСТАРТ?! МЫ ЖЕ НЕ КОМПЬЮТЕР, ЧТОБЫ ПЕРЕЗАПУСКАТЬСЯ!!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po29.flac" 
    skoof "Не ори, я тоже ничего не понял."
    stop audio
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po91.flac"
    polina "Какие ж вы все недалекие."
    hide polina5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po92.flac"
    polina "Ладно, проехали."
    play audio "another_attempt/audio/voice_polina/po93.flac"
    polina "Выбери следующий раздел."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    jump mod_polina_loop
    return

label mod_polina_health:
    scene expression "uslugi/bg-su-health.png"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po94.flac"
    polina "Здоровье."
    hide polina2
    show polina4:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po95.flac"
    polina "Хм..."
    play audio "another_attempt/audio/voice_polina/po96.flac"
    polina "Смотрю ты давно не проходил медосмотр."
    hide polina4
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po97.flac"
    polina "Ну и ладно, давай просто подделаем документы."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po30.flac" 
    skoof "Подделаем документы?"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po31.flac" 
    skoof "Но это ведь незаконно."
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po98.flac"
    polina "Ну, это самый быстрый способ и без заморочек."
    hide polina6
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po99.flac"
    polina "Нет, если хочешь, мы можем ждать ещё неделю, пока ты соберешь нужные бумажки."
    play audio "another_attempt/audio/voice_polina/po100.flac"
    polina "Но к тому моменту мне точно станет неинтересно, и я не захочу приезжать."
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio14.flac"
    inner "А ОНА ЗНАЕТ КУДА НАДАВИТЬ."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po32.flac" 
    skoof "Ну хорошо-хорошо, я понял."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po33.flac" 
    skoof "Но тогда у меня не будет проблем с полицией и ФСБ?"
    stop audio
    hide polina5
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po101.flac"
    polina "Пф, конечно нет."
    play audio "another_attempt/audio/voice_polina/po102.flac"
    polina "Сделаем всё в лучшем виде."
    play audio "another_attempt/audio/voice_polina/po103.flac"
    polina "Только..."
    play audio "another_attempt/audio/voice_polina/po104.flac"
    polina "Ответь на парочку моих вопросов."
    play audio "another_attempt/audio/voice_polina/po105.flac"
    polina "Мне всё же не хочется подцепить от тебя какую-нибудь заразу или таскаться с тобой по больницам." 
    play audio "another_attempt/audio/voice_polina/po106.flac"
    polina "Готов?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Готов ли ты?"
    "Когда ты в последний раз был к чему-то готов?"
    "Тихо проживая свою маленькую неторопливую жизнь, ты уже давно ни к чему не готов."
    "Разве что к тому, что завтра всё будет так же, как и вчера."
    play audio "another_attempt/audio/voice_skPo/po34.flac" 
    skoof "Да наверное."
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po107.flac"
    polina "Когда ты в последний раз проверялся на ЗППП?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po35.flac" 
    skoof "На что?"
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po108.flac"
    polina "Заболевания, передающиеся половым путём!"
    play audio "another_attempt/audio/voice_polina/po109.flac"
    polina "Гонорея, сифилис, ВИЧ, гепатит."
    hide polina2
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po110.flac"
    polina "Я же сказала, что не хочу подцепить от тебя что-нибудь."
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po36.flac" 
    skoof "Ну..."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po37.flac" 
    skoof "Если честно, я довольно давно не проверялся."
    stop audio
    hide polina5
    show polina3:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/sound/what.mp3"
    pause 2.0
    play audio "another_attempt/audio/voice_polina/po111.flac"
    polina "Ааагрх, ну вот."
    hide polina3
    show polina5:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po112.flac"
    polina "Тебе в любом случае придётся идти и проверяться."
    play audio "another_attempt/audio/voice_polina/po113.flac"
    polina "Я точно не собираюсь кувыркаться с переносчиком инфекций."
    play audio "another_attempt/audio/voice_polina/po114.flac"
    polina "Обязательно сделай."
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po38.flac" 
    skoof "Хорошо."
    stop audio
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po115.flac"
    polina "Гастрит?"
    show polina5:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/sound/givot.mp3"
    "Сухой кусок вчерашней пиццы неспокойно переворачивается у тебя в желудке от такого вопроса."
    "Ты невольно вспоминаешь своё меню за последние годы."
    "Может ли говяжий дошик считаться здоровым питанием? Или крабовые чипсы по скидке..."
    play audio "another_attempt/audio/voice_inner_po/audio15.flac"
    inner "ЕСТЬ ТОЛЬКО ОДИН ПРАВИЛЬНЫЙ ОТВЕТ!"
    stop audio
    menu:
        "Всё в порядке у меня с желудком (соврать)":
            "Странный звук разрезает воздух."
            "Трудно сказать наверняка, что это."
            "Урчание в животе? Пердёж?"
            "Может, где-то внутри у тебя пытается вырваться наружу совесть?"
    play audio "another_attempt/audio/voice_inner_po/audio16.flac"
    inner "ТОЧНО НЕТ!!"
    stop audio
    hide polina5
    show polina1:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po116.flac"
    polina "Ало, гараж."
    play audio "another_attempt/audio/voice_polina/po117.flac"
    polina "Картина Репина: 'Приплыли'."
    hide polina1
    show polina2:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po118.flac"
    polina "Ну нет, так нет. Это хорошо."
    play audio "another_attempt/audio/voice_polina/po119.flac"
    polina "А то у меня раз был случай с желудком."
    play audio "another_attempt/audio/voice_polina/po120.flac"
    polina  "Всю ночь блевала, даже до скорой дошло."
    hide polina2
    show polina3:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po121.flac"
    polina "Эх, теперь гадость всякую не ем..."
    play audio "another_attempt/audio/voice_polina/po122.flac"
    polina "Ну может иногда... по праздникам... раз в неделю..."
    show polina3:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po39.flac" 
    skoof "Как я тебя понимаю."
    stop audio
    hide polina3
    show polina4:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po123.flac"
    polina "Понимаешь?"
    play audio "another_attempt/audio/voice_polina/po124.flac"
    polina "Ты же сказал, что у тебя всё в порядке с желудком."
    show polina4:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po40.flac" 
    skoof "А ну..."
    stop audio
    hide polina4
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po125.flac"
    polina "Ой, ну что это я."
    play audio "another_attempt/audio/voice_polina/po126.flac"
    polina "Бывают же люди травятся несвежей едой."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po41.flac" 
    skoof "В самом деле."
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po127.flac"
    polina "Так-с, все документы загружены."
    play audio "another_attempt/audio/voice_polina/po128.flac"
    polina "Что у нас дальше?"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    jump mod_polina_loop
    return

label mod_polina_registrationandpassport:
    scene expression "uslugi/bg-su-reg.png"
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po129.flac"
    polina "Ну тут вообще легко."
    play audio "another_attempt/audio/voice_polina/po130.flac"
    polina "Просто подожди, я загружу все файлы."
    play audio "another_attempt/audio/voice_polina/po131.flac"
    polina "А пока..."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po132.flac"
    polina "Не хочешь узнать друг друга..."
    play audio "another_attempt/audio/voice_polina/po133.flac"
    polina "Получше?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po42.flac"
    skoof "Получше?"
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po134.flac"
    polina "Да."
    play audio "another_attempt/audio/voice_polina/po135.flac"
    polina "С чего обычно начинается знакомство девушки с парнем?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po43.flac"
    skoof "С чего же?"
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio17.flac"
    inner "ДА, С ЧЕГО?"
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po136.flac"
    polina "С обнажённых фоток!"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    "Где-то пару секунд вы сидели, смотря в экран, а внутри вас было какое-то странное чувство волнения."
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po137.flac"
    polina "Хэй, не зависай."
    hide polina2
    show polina6:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po138.flac"
    polina "Разве тебе не интересно?"
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po44.flac"
    skoof "Интересно, конечно..."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po45.flac"
    skoof "Но, по-моему, не с этого начинается знакомство."
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po139.flac"
    polina "Ой, да не ломайся."
    play audio "another_attempt/audio/voice_polina/po140.flac"
    polina "Не хочешь - так и скажи, остановлю загрузку и разбежимся."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po46.flac"
    skoof "Да нет же, нет."
    stop audio
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po141.flac"
    polina "Так и думала."
    show polina6:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio18.flac"
    inner "ОХ НЕ НРАВИТСЯ МНЕ ЭТО."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio19.flac"
    inner "А ПОГЛЯДЕТЬ-ТО ХО-ОЧЕТСЯ."
    stop audio
    hide polina6
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po142.flac"
    polina "Я скину ссылку."
    play audio "another_attempt/audio/voice_polina/po143.flac"
    polina "Тебе всего лишь нужно ввести немного своих данных."
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po47.flac"
    skoof "Подожди..."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po48.flac"
    skoof "Ты публикуешь свои обнаженные фото на каком-то сайте?"
    stop audio
    show polina2:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po144.flac"
    polina "Этот сайт находится в скрытом отделе скуфуслуг, доступ к которому есть только у альтушек, и только альтушки могут давать на него ссылку." 
    play audio "another_attempt/audio/voice_polina/po145.flac"
    polina "Хватит уже вопросов, просто перейди по ссылке."
    menu:
        "Нажать на ссылку":
            jump mod_polina_onlyscuf

    jump mod_polina_loop
    return

label mod_polina_onlyscuf:
    scene expression "another_attempt/images/bg-onlyscuf.png"
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    show polina2:
        linear .5 xalign 0.95 zoom 1.0
    show polina2:
        align (0.95, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po146.flac"
    polina "Просто введи сюда свои личные данные."
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po49.flac"
    skoof "Личные данные?"
    stop audio
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po147.flac"
    polina "Ага, имя, дата рождения, место жительства, почта, телефон, пароль от скуфуслуг, пароль от гугла, компа..."
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po50.flac"
    skoof "Больше похоже на то, что мои личные данные хотят украсть."
    stop audio
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po148.flac"
    polina "Этот сайт напрямую связан со скуфуслугами, все эти данные и так тут хранятся."
    show polina2:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio20.flac"
    inner "ГДЕ-ТО ОНА НАС НАЙ..."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio21.flac"
    inner "НАДУВАЕТ!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po51.flac"
    skoof "Ну хорошо."
    stop audio
    hide window
    play audio "another_attempt/audio/sound/klava.mp3"
    pause 3.0
    play audio "another_attempt/audio/sound/012_error.ogg"
    show image "another_attempt/images/polina/antivirus228.png":
        subpixel True
        align (0.5, 0.5)
        zoom 0.3
    hide polina2
    show polina4:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po149.flac"
    polina "А? Что это... Антивирус?"
    show polina4:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po52.flac"
    skoof "Кажется, компьютер считает сайт небезопасным. Нужно установить антивирус."
    stop audio
    hide polina4
    show polina1:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/sound/scary.mp3"
    pause 3.0
    play audio "another_attempt/audio/voice_polina/po150.flac"
    polina "ЧЕГО?!"
    play audio "another_attempt/audio/voice_polina/po151.flac"
    polina "ПО-ТВОЕМУ Я БУДУ КИДАТЬ ТЕБЕ ВИРУСНУЮ ХЕРНЮ?! И ЭТО ПОСЛЕ ВСЕГО, ЧТО МЕЖДУ НАМИ БЫЛО?!"
    show polina1:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_skPo/po53.flac"
    skoof "Но..."
    stop audio
    show polina1:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po152.flac"
    polina "ТАКИЕ КАК ТЫ РЕГИСТРИРУЮТСЯ НА ТАКИХ САЙТАХ И ПЛАТЯТ БАБЛО, ЧТОБЫ ПОСМОТРЕТЬ НА ГОЛЫХ ДЕВУШЕК, И ИХ НЕ ВОЛНУЕТ ЧТО ЭТО ЗА САЙТ!"
    play audio "another_attempt/audio/voice_polina/po153.flac"
    polina "А КАК ТОЛЬКО ТЕБЕ ПРЕДСТАВИЛАСЬ ВОЗМОЖНОСТЬ ПОСМОТРЕТЬ НА ЭТО ЗДЕСЬ И СЕЙЧАС БЕСПЛАТНО, ТЫ СЛИВАЕШЬСЯ ИЗ-ЗА КАКОГО-ТО СПАМА С АНТИВИРУСОМ?!"
    show polina1:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    play audio "another_attempt/audio/voice_inner_po/audio22.flac"
    inner "ОГО КАК ЗАПЕЛА!"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po54.flac"
    skoof "Прости, пожалуйста, я не хотел выставлять тебя виноватой."
    stop audio
    show polina1:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po165.flac"
    polina "Агрх..."
    hide polina1
    show polina3:
        align (0.95, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po154.flac"
    polina "И ты прости..."
    play audio "another_attempt/audio/voice_polina/po155.flac"
    polina "Я, вроде, говорила, что могу срываться..."
    hide polina3
    show polina5:
        align (0.95, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po156.flac"
    polina "Что ж, выбор только за тобой, довериться мне или установить антивирус."
    show polina5:
        align (0.95, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)

    menu:
        "Установить антивирус":
            $ import random
            $ rand = random.randint(1, 1)
            if rand == 1:
                jump mod_polina_finale_good
            else:
                jump mod_polina_finale_bad
        
        "Не устанавливать антивирус":
            jump mod_polina_finale_bad


    return


# === КОНЦОВКИ ===

label mod_polina_finale_bad:
    $ persistent.unlocked_endings.add("Пока-пока рекорд в танчиках")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    hide polina5
    stop music
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-onlyscufvideo.webm", delay=6, loops=0)
    scene expression "uslugi/bg-wallpaper.png"
    play audio "another_attempt/audio/voice_inner_po/audio23.flac"
    inner "А Я ГОВОРИЛ!!"
    stop audio
    show polina7:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolve 
    show polina7:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play music polina_end
    play audio "another_attempt/audio/voice_polina/po157.flac"
    polina "Ахаххахаха, ИДИОТ!"
    play audio "another_attempt/audio/voice_polina/po158.flac"
    polina "Ты серьёзно думал, что сможешь посмотреть мои голые фотки просто так?!"
    play audio "another_attempt/audio/voice_polina/po159.flac"
    polina "Извращенец!"
    play audio "another_attempt/audio/voice_polina/po160.flac"
    polina "Попрощайся со своим компьютером!"
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-rabocistolvideo.webm", delay=6, loops=0)
    scene expression "uslugi/bg-black.png"
    with fade
    pause(1.5)
    scene cg-polinaandskoof
    with fade
    stop audio
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    play audio "another_attempt/audio/voice_inner_po/audio24.flac"
    inner "НЕСМОТРЯ НА НЕУСТОЙЧИВЫЙ И БУРНЫЙ ХАРАКТЕР АЛЬТУШКИ ПОЛИНЫ, ОНИ СО ВКУСОМ ДОВОЛЬНО БЫСТРО ПОЛАДИЛИ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio25.flac"
    inner "ИГРАЛИ В ИГРЫ ДНЯМИ НАПРОЛЁТ, ЕЛИ ТОЛЬКО ЕДУ С ДОСТАВКОЙ, ЛЮБИЛИ ДРУГ ДРУГА И НЕ ТОЛЬКО ЛЮБИЛИ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio26.flac"
    inner "ОТ ВЕЧНЫХ ИСТЕРИК АЛЬТУШКИ НИКТО НЕ БЫЛ ЗАСТРАХОВАН. НО СКУФ ТЕРПЕЛ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio27.flac"
    inner "ОДНА НОЧЬ СТОИТ ВСЕХ КРИКОВ И УПРЁКОВ. ДА И КТО БЫ МОГУ ПОДУМАТЬ, ЧТО С ХАКЕРШЕЙ ПОЛОВИНА ТВОИХ ЗАБОТ ИСЧЕЗНЕТ, А УТЕХ СТАНЕТ БОЛЬШЕ."
    stop audio
    hide cg-polinaandskoof
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-polinaandskoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    with fade
    play audio "another_attempt/audio/voice_inner_po/audio28.flac"
    inner "ЧЕПУХА!"
    stop audio
    scene expression "hata/15 workspace.png"
    with fade
    play audio "another_attempt/audio/voice_skPo/po55.flac"
    skoof "Нет."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po56.flac"
    skoof "Только не рекорд в танчиках."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio29.flac"
    inner "ТЕПЕРЬ НЕ ТОЛЬКО РЕКОРДОВ, НИ ДЕНЕГ НЕТ, НИ АЛЬТУШЕК, НИ КОМПА."
    stop audio
    "Скуф сидел и отчаянно смотрел в экран в надежде, что всё наладится, но... Экран так и не включился."
    "А его данные"
    "Бог знает куда их отправили."
    if 2 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_byebyetanki:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_byebyetanki
        with moveouttop
        $ achievements.remove(2)
    scene expression "uslugi/bg-black.png"
    with fade
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-errorsanswin.webm", delay=6, loops=0)
    stop music
    jump titles

    return

label mod_polina_finale_good:
    $ persistent.unlocked_endings.add("Пока-пока Полина.")

    ## Dev. tip: Блокировка возможности откатиться
    $ renpy.force_autosave()
    $ renpy.block_rollback()

    hide polina5
    stop music
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-onlyscufvideo.webm", delay=6, loops=0)
    scene expression "uslugi/bg-wallpaper.png"
    play audio "another_attempt/audio/voice_inner_po/audio23.flac"
    inner "А Я ГОВОРИЛ!!"
    stop audio
    show polina7:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    with dissolve 
    show polina7:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play music polina_end
    play audio "another_attempt/audio/voice_polina/po157.flac"
    polina "Ахаххахаха, ИДИОТ!"
    play audio "another_attempt/audio/voice_polina/po158.flac"
    polina "Ты серьёзно думал, что сможешь посмотреть мои голые фотки просто так?!"
    play audio "another_attempt/audio/voice_polina/po159.flac"
    polina "Извращенец!"
    play audio "another_attempt/audio/voice_polina/po160.flac"
    polina "Попрощайся со своим компьютером!"
    play audio "another_attempt/audio/voice_polina/po161.flac"
    polina "АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ"
    show image "another_attempt/images/polina/virus.jpg":
        subpixel True
        align (0.98, 0.8)
        zoom 0.25
    hide polina7
    show polina4:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po162.flac"
    polina "Не смей, слышишь!"
    play audio "another_attempt/audio/voice_polina/po163.flac"
    polina "Даже не думай."
    hide polina4
    show polina1:
        align (0.5, 1.9)
        subpixel True
        zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/voice_polina/po164.flac"
    polina "НЕ СМЕЙ!"
    play audio "another_attempt/audio/voice_polina/po166.flac"
    polina "НЕ СМЕЙ, НЕ СМЕЙ, НЕ СМЕЙ, НЕ СМЕЙ!"
    show polina1:
        align (0.5, 1.9)
        subpixel True
        linear .25 zoom 1.0 matrixcolor BrightnessMatrix(0.0)
    menu:
        "Очистить устройство от вируса":
            show polina1:
                align (0.5, 1.9)
                subpixel True
                linear .25 zoom 1.05 matrixcolor BrightnessMatrix(0.1)
    play audio "another_attempt/audio/sound/hit-effekt-dlya-stsenyi-ujasa-quotkrik-robotaquot-32209.mp3"
    hide window
    hide polina1
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-pokapoka.webm", delay=6, loops=0)
    scene expression "uslugi/bg-black.png"
    with fade
    pause(1.5)
    scene cg-polinaandskoof
    with fade
    stop audio 
    $ inner = inner_home
    $ skoof = skoof_home
    $ narrator = narrator_home
    $ persistent.story_progress = "ending"
    play audio "another_attempt/audio/voice_inner_po/audio24.flac"
    inner "НЕСМОТРЯ НА НЕУСТОЙЧИВЫЙ И БУРНЫЙ ХАРАКТЕР АЛЬТУШКИ ПОЛИНЫ, ОНИ СО ВКУСОМ ДОВОЛЬНО БЫСТРО ПОЛАДИЛИ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio25.flac"
    inner "ИГРАЛИ В ИГРЫ ДНЯМИ НАПРОЛЁТ, ЕЛИ ТОЛЬКО ЕДУ С ДОСТАВКОЙ, ЛЮБИЛИ ДРУГ ДРУГА И НЕ ТОЛЬКО ЛЮБИЛИ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio26.flac"
    inner "ОТ ВЕЧНЫХ ИСТЕРИК АЛЬТУШКИ НИКТО НЕ БЫЛ ЗАСТРАХОВАН. НО СКУФ ТЕРПЕЛ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio27.flac"
    inner "ОДНА НОЧЬ СТОИТ ВСЕХ КРИКОВ И УПРЁКОВ. ДА И КТО БЫ МОГУ ПОДУМАТЬ, ЧТО С ХАКЕРШЕЙ ПОЛОВИНА ТВОИХ ЗАБОТ ИСЧЕЗНЕТ, А УТЕХ СТАНЕТ БОЛЬШЕ."
    stop audio
    hide cg-polinaandskoof
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-polinaansdkoofend.webm", delay=5, loops=0)
    scene expression "uslugi/bg-black.png"
    with fade
    play audio "another_attempt/audio/voice_inner_po/audio28.flac"
    inner "ЧЕПУХА!"
    stop audio
    scene expression "uslugi/bg-wallpaper.png"
    $ inner = inner
    $ skoof = skoof
    $ narrator = narrator
    play audio "another_attempt/audio/voice_skPo/po57.flac"
    skoof "Ну и истеричка."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio30.flac"
    inner "ДА НЕ ГОВОРИ, НУ И МОЛОДЁЖЬ."
    stop audio
    play audio "another_attempt/audio/voice_inner_po/audio31.flac"
    inner "ЛУЧШЕ ГЛЯНЬ, НА МЕСТЕ ЛИ ВСЁ, РЕКОРДЫ В ТАНЧИКАХ СОХРАНИЛИСЬ?"
    stop audio
    play audio "another_attempt/audio/voice_skPo/po58.flac"
    skoof "Сохранились."
    stop audio
    play audio "another_attempt/audio/voice_skPo/po59.flac"
    skoof "Эх, ну эти левые онли сайты. Пойдём ещё катку в танки."
    stop audio
    stop music
    if 1 in achievements:     
        play audio "another_attempt/audio/sound/steam-achievement-popup.mp3"
        show achievements_byebyepolina:
            xalign 1.0 
            yalign 0.0
            zoom 0.5
        with moveintop
        pause 4.0
        hide achievements_byebyepolina
        with moveouttop
        $ achievements.remove(1)
    scene expression "uslugi/bg-black.png"
    with fade
    $ renpy.movie_cutscene("another_attempt/images/polina/cg-inksanswin.webm", delay=21, loops=0)

    jump titles
    return

label mod_titles:
    call screen titles_mod()

    return
screen titles_mod():
    
    ## Здесь лежат основные титры. bonus_duration - насколько надо увеличить время показа титров, в секундах
    use title_base(bonus_duration = 15):
        
        null height 30

        text _("ДОПОЛНЕНИЕ “ОЧЕРЕДНАЯ ПОПЫТКА”") xalign .5 color "#000" font "fonts/blogger-sans.medium.otf"

        null height 30

        text _("Автор альтушек") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("{a=https://t.me/hikichamalysheva}Hikicha Malysheva{/a}") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Программист") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("{a=https://t.me/Planetka_NeNeKi}NeNeKi{/a}") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Актер озвучки Дианы") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("Куле") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Актер озвучки Нади") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("{a=t.me/huerman}Герман Крауз{/a}") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Актер озвучки Полины") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("Гиса") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Актер озвучки Скуфа и внутреннего голоса") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("Нейросеть") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        text _("Автор идеи озвучки Скуфа и внутреннего голоса") xalign .5 font "fonts/blogger-sans.medium.otf" color "#ff1d53"
        label _("Дмитрий") xalign .5 text_font "fonts/blogger-sans.medium.otf" text_color "#4577f6"

        null height 30

        ## Здесь лежит концовка титров
        use title_end()
