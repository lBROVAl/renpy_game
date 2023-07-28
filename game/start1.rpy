# Картинки, переменные, персонажи
define SEASONS = ["весна","лето","осень","зима"] # [ ] чтавится при перечислении
define DAYS = ["пнд.","вт.","срд.","чтв.","пят.","суб.","вскр."]
define mc = Character ("[mc]", color="#c8ffc8")
define dz = Character('Демон Знания', color="#c8ffc8")
image dz norm ="Demon_Knowleg.png"
image dzer ="Demon_zerkalo.png"

image lgo = "lgo.png"



define audio.mythos ="Nameless.mp3"
define audio.fool ="Kalambur.mp3"
define muzlo = False



image bg Desert ="bg Desert.jpg"
image bg cross ="bg cross.jpg"
image bg mellil ="bg mellil.jpg"
image bg map ="bg map.jpg"


image face ="face.png"
image sun ="sun.png"
image moon ="moon.png"

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


    ###### Позиционирование персонажей всегда строго под блоком init: ########
    $ strogo_v_center = Position (xalign=0.5, yalign=1.0) # у=1 то Демон стоит внизу экрана
    $ leftin = Position (xalign=0.4, yalign=0.4)
