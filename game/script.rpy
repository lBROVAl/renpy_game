# Вы можете расположить сценарий своей игры в этом файле.
# в обязательном поряке создавать отдельные файлы init, transform, screen
# Определение персонажей игры.

transform alphin: ###### лучше вывести в отдельный фаил ######
    alpha 0
    xpos 491, ypos 123
    linear 3 alpha 1
transform eye:
    zoom 0
    xpos 640 ypos 360
    linear 2 zoom 1
    repeat 1

transform zoomin:
    zoom 1
    linear 0.5 zoom 1.1
    linear 1 zoom 0.8
    linear 0.5 zoom 1
    repeat

init:
    # onn = ("eye.png" 0.5, 0.2, reverse = False)
    # off = ("eye.png" 0.5, 0.2, reverse = True)
    $ energia = 100
    $ nastroy = 100
    $ golod = 100
    $ jajda = 100
    $ sila = 0
    $ intellekt = 0
    $ harizma = 0
    $ lovkost = 0
    $ eda = 0
    $ dengi = 100
    $ theweekday = 0


    ###### Позиционирование персонажей всегда строго под блоком init: ########
    $ strogo_v_center = Position (xalign=0.5, yalign=1.0) # у=1 то Демон стоит внизу экрана
    $ leftin = Position (xalign=0.4, yalign=0.4)

# Игра начинается здесь:
label start:
    play music mythos
    scene bg Desert
    with fade
    "Я прихожу в себя и оглядываюсь: Где это я? Как я здесь оказался? Ничего не понимаю! Я вижу пустыню и какие-то руины... Погодите,я что в Сахаре?! Нооо..."
    "В следующий миг передо мной объявляется нечто."
    show dz norm at alphin
    "Я слышу голос, скрипучий, как старая граммафонная пластинка. Если, конечно, еще есть люди, которые помнят, как звучат эи штуки..."
    $ mc = renpy.input("Назови себя, путник!", length =24, allow="ЯЧСМИТБЮЭЖДЛОРПАВФЦУКЕНГШЩЗХ-ёйцукенгшщзхъэждлорпавыфячсмитьбю'").strip()
    if mc =="":
        $ mc = "Никто"
    dz "Приветствую тебя в этом месте [mc]!"
#    show screen atributpanel
    show screen energpanel
    show screen eatpanel
    show screen Waterpanel
    show screen nastpanel
    show screen daytpanel
    mc "Что это за херня у меня над головой?!"
    dz "Предполагалось, что это будут твои статы. Что они означают, догадайся сам по значкам. Но полагаю, это не единственный вопрос, который терзает тебя, [mc]!"
    menu vopros_menu:
        dz "Спрашивай. Я постараюсь ответить на все. Для этого я и послан сюда."
        "Кто ты?":
            mc "Кто ты, тварь?"
            dz "Я - Демон знания"
            jump vopros_menu

        "Где я?":
            mc "Где я нахожусь?"
            dz "Ты находишься здесь"
            mc "Очень смешно! А где это «здесь»? Что это за мать его место?"
            dz "Это место - результат насилия над кодом."
            mc "О-о..."
            hide dz norm
            show bg panorama

            mc "Понятно"
            scene bg Desert
            show dz norm
            jump vopros_menu

        "Как?!":
            mc "Как я здесь оказался?"
            dz "Очевидно, ты запустил игру"
            mc "Хм..."
            "Я припонил, что действтельно запускал что-то такое, надеясь найти хорошую хентай-навеллу."
            dz "Что-то похожее ты и нашел. Наше присутствие здесь результат принуждения кода прграммы к БДСМ с чайником-разработчиком."
            mc "Ты прочел мои мысли?!"
            dz "Нет. Угадал по лицу."
            jump vopros_menu

        "Музыка":
            mc "Что за музыка?"
            if muzlo:
                mc "Какая хрень! Лучше верни как было!"
                dz "Извини, но поменять можно лишь один раз. Слушай теперь что есть."
                jump vopros_menu
            else:
                dz "Это Nox Arcana, альбом Necronomicon, трэк «The Nameless City». Думаю, она подходит к антуражу локации."
                menu:
                    dz "Тебе не нравится?"
                    "Нравится":
                        mc "Нравится"
                        dz "Хорошо!"
                        jump vopros_menu
                    "Не нравится":
                        mc "Мне не нравится эта музыка. Как-то мрачно..."
                        $ muzlo = True
                        dz "Нет проблем, можем сменить!"
                        play music fool
                        mc "Э-э-э..."
                        jump vopros_menu
        "Зачем?":
            mc "Для чего это всё?"
            dz "Хорошо, что спросил. Это всё создавалось с одной целью - отработать навыки автора в работе с ренпаем"
            menu:
                dz "Тебе интересно?"
                "Да":
                    mc "Пусть похвасается"
                    hide dz
                "Нет":
                    mc "Нет"
                    jump vopros_menu
        "Не хочу":
            mc "Я нехочу ничего спрашивать"
            dz "Отлично"
            jump end

    show face at zoomin:
        xalign 0.4 yalign 0.4
    show dz norm
    mc "Эм... Демон? Тут из-за тебя какая-то морда выглядывает..."
    dz "Что?"
    show dz norm:
        linear 0.4 xalign 0.95 yalign 0.9
    hide dz norm
    show dzer at right
    show face at zoomin:
        xalign 0.4 yalign 0.4
        linear 0.5 xalign 0.7 yalign 0.1
        linear 0.5 xalign 0.8 yalign 1.0
        linear 1.0 xalign 0.0 yalign 0.0
        linear 1.5 xalign 1.0 yalign 0.0
        linear 0.5 xalign 1.0 yalign 0.5
        linear 0.5 xalign 0.4 yalign 0.4
        repeat
    dz "Ах, эта..."
    dz "Это кодер пытался натянуть ренпай на глобус. Вишь, что вышло."
    dz "Разлеталося"
    mc "..."
    dz "Не обращай внимания. Устанет - само свалит"
    hide face
    dz "Во, видишь? Свалило."
    show dzer:
        linear 0.4 xalign 0.5 yalign 0.9
    dz "Пойдем!"
    jump go

label end:
    "Конец диалога"

    return
