# Вы можете расположить сценарий своей игры в этом файле.
# в обязательном поряке создавать отдельные файлы init, transform, screen
# Определение персонажей игры.
init:
    # onn = ("eye.png" 0.5, 0.2, reverse = False)
    # off = ("eye.png" 0.5, 0.2, reverse = True)
    $ sila = 0
    $ intellekt = 0
    $ harizma = 0
    $ lovkost = 0
    $ eda = 0
    $ dengi = 100


    ###### Позиционирование персонажей всегда строго под блоком init: ########
    $ strogo_v_center = Position (xalign=0.5, yalign=1.0) # у=1 то Демон стоит внизу экрана
    $ leftin = Position (xalign=0.4, yalign=0.4)

# Игра начинается здесь:
label go:
    scene bg cross
    with fade
    mc "Мы попадаем на перекресток некольких дорог."
    show dz norm at strogo_v_center
    "Выбери путь, [mc]!"

    show screen lok
    window auto hide
    pause
    #show screen meny_panel

