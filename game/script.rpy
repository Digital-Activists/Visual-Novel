# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define sa = Character('[saname]', color="#c8ffc8", img = 'sasha')
define av = Character('Повествователь', color = "#968E79")
define x = Character('Хранитель', color = "#1F1AB2")
define sy = Character('Существо', color = "#8B0000")
define dv = Character('Дворф', color = "#FF6347")
define gror = Character('Грор', color = "#FF4500")
define smith = Character('Бендан', color = "#FF6347")
define fentir = Character('[fentir]', color = "#50C878")
define fen = Character('Фентир', color = "#50C878")
define f1 = Character('Фентир', color = "#50C878")
define f2 = Character('Фентир', color = "#FFFF00")
define ao = Character('Какой-то артист', color = "#FF00FF")
define atwo = Character('Еще один артист', color = "#8A2BE2")
define fentira = Character('Фентира', color = "#A7FC00")
define voin = Character('Фентир-воин', color = "#490005")
define glav = Character('Глава Аккаров', color = "#FF2400")
define siluet = Character('Силуэт', color = "#42AAFF")
define b = Character('Бэндр', color = "#FD7C6E")
define bzombie = Character('Зараженный бэндр', color = "#D1E231")
define fl = Character('Светлый фуллириан', color = "#FFFFFF")
define chel = Character('Человек', color = "#78DBE2")
define god = Character('Создатель', color = "#78DBE2")
define k = Character('Король Девизариона', color = "#FFD700")
define girl = Character('Девушка', color = "#FF1493")
# Переменные
define counter = 0
define count = 0
define fonari = 0
#Звуковые эфекты
define audio.eff = "sound/aff.mp3"


#МУЗЫКА
define audio.musicone = "music/musicone.mp3"
define audio.musictwo = "music/musictwo.mp3"
define audio.opendoor = "music/opendoor.mp3"
define audio.computer = "music/computer.mp3"
define audio.portal = "music/portal.mp3"
define audio.kickhead = "music/kickhead.mp3"
define audio.telegasound = "music/telegasound.mp3"
define audio.forgesound = "music/forgesound.mp3"
define audio.musicthird = "music/musicthird.mp3"
define audio.struna = "music/struna.mp3"
define audio.city = "music/city.mp3"
define audio.taverna = "music/taverna.mp3"
define audio.helpers = "music/helpers.mp3"
define audio.fight = "music/fight.mp3"
define audio.knife = "music/knife.mp3"
define audio.bird = "music/bird.mp3"
define audio.kickdoor = "music/kickdoor.mp3"
define audio.stairs = "music/stairs.mp3"
define audio.krick = "music/krick.mp3"
define audio.rock = "music/rock.mp3"
define audio.happy = "music/happy.mp3"

image portal_rotate:
    "Object/portal.png"
    rotate 0
    linear 15 rotate 360
    repeat
    
    
    
transform zoomin:
    zoom 0 xpos 640 ypos 360 anchor(0.5, 0.5)
    linear 3 zoom 1
    
transform zoomout:
    zoom 1
    linear 5 zoom 0
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:

    scene room
    
    $ saname = renpy.input("Введите имя главного героя. \nГлавный персонаж новеллы мужского пола.", length = 12).strip()
    if saname == "":
        $saname = "Саша"
    play music musicone fadein 2
    av "Всё началось с обычного теплого летнего дня. [saname] вернулся с вечерней прогулки, и хотел было лечь спать, однако что-то тревожило его. "
    
    show sasha normal at right
    with dissolve
    
    sa "{i}Почему я чувствую, что забыл сделать что-то важное?{/i}"

    av "Долго вспоминать не пришлось, ведь это было важное дело."
    
    sa "{i}Я же хотел изучить университеты и выбрать образовательную программу!{/i}"
    
    av "Парень включил ноутбук, и выбрал для себя самый подходящий университет."
    
    sa "{i}Отлично! В Урфу завтра как раз день открытых дверей, где мне расскажут про образовательные программы и направления в IT-сфере.{/i}"
    
    sa "{i}Интересно, что меня ждёт в будущем?{/i}"
    
    hide sasha normal with dissolve
    
    av "После долгих раздумий [saname] провалился в сон."
    
    scene street
    
    av "Была прекрасная погода. Дул тёплый ветерок, а солнечные лучи пробивались сквозь листву."
    av "Наслаждаясь погодой, [saname] шёл по улицам Екатеринбурга и рассматривал здания. Через несколько минут юноша увидел на здании надпись."
    
    menu:                 
        "Посмотреть":
            jump PosleProsmotra
               
    return   
    
label PosleProsmotra:
    sa "{i}Уральский федеральный университет имени первого Президента России Б. Н. Ельцина, кажется мне сюда.{/i}"
    
    av "[saname] открыл тяжелую дверь и вошёл в здание. Но окружающая обстановка не оправдала его ожиданий."
    stop music
    scene guk
    
    av "Было пусто. Везде. В университете не было ни души."
    
    show sasha normal at right
    with dissolve
    
    sa "{i}Как странно, никого нет… Сегодня же день открытых дверей, должен быть здесь хоть кто-нибудь.{/i}"
    
    hide sasha normal with dissolve
    
    av "Парень решил воспользоваться возможностью прогуляться по коридорам университета. К тому же, сидеть и ждать, когда кто-нибудь придёт, было не в его правилах. "
    
    scene guk
    
    av "Он ходил по коридорам, заходил в кабинеты, но в здании никого не было. Почему? [saname] не знал, даже не догадывался. [saname] нервно теребил лямку рюкзака и заходил в одну аудиторию за другой."
    
    scene closedoor
    
    show sasha angry at right
    with dissolve
    
    sa "{i}Что здесь происходит? Я добирался сюда ради пустоты, да? Что ж пустота – это отличный собеседник, так и знайте!{/i}"
    sa "{i}Последняя дверь, и я ухожу домой!{/i}"
    av "Подумал он и открыл открыл деревянную дверь. За ней было темно и пусто, однако что-то привлекло внимание парня."
    play sound opendoor
    
    #Сделать открытие дверей.
    
    
    scene comp
    stop music fadeout 2
    play ambient computer
    
    show sasha normal at right 
    with dissolve
    
    sa "{i}Компьютеры?{/i}" 
    sa "{i}Странно, что никого нет, а они работают.{/i}"
    
    hide sasha normal with dissolve
    
    av "Парень подошёл к трём включенным мониторам и выбрал один из них."
    menu:
        "Какой компьютер выберешь?"
        
        "1":
            jump viborPk
        "2":
            jump viborPk
        "3":
            jump viborPk
    
    
    return


label viborPk:
    
    show sasha normal at right 
    with dissolve
    
    sa "{i}Попробую что-нибудь нажать, вдруг что-то произойдёт.{/i}"
    
    av "[saname] дотронулся до клавиатуры указательным пальцем и заметил всплывающее сообщение."
    
    menu:
        "Посмотреть":
            jump ProsmotrTab
        
label ProsmotrTab:
    show sasha surprised at right
    sa "{i}Веб-разработчик?{/i}"
    show sasha angry at right
    sa "{i}Это намёк какой-то? Что дальше-то делать? Может, мне ещё самому день открытых дверей организовать?{/i}"
    
    av "Тишина..."
    
    av "Вокруг по-прежнему не было никого, тишину нарушал только шум вентиляторов в системных блоках."
    
    av "Вдруг со всех сторон стал нарастать странный звук, а на стене начала вырисовываться фиолетовая воронка."
    
    play sound portal
    
    show portal_rotate at left with dissolve

    show sasha surprised at right
    sa "Ч-что… что за чёрт!"
    
    av "Юноша оцепенел, страх заполнил его снизу доверху. Он практически перестал дышать и продолжал смотреть на увеличивающуюся воронку. "
    
    hide portal_rotate with dissolve
    show x2 at left with dissolve
    av "Она закрылась, однако на её месте в серой мантии стоял старик с белыми как снег волосами, морщинистым лицом и голубыми глазами. "    
   
    x "Наконец-то ты пришёл, я так долго ждал тебя, Прошу, помоги нашему Королевству Девизарион, без тебя мы не справимся."
    show sasha angry at right
    sa "Ч-чего? Серьёзно? Я не пойду за каким-то стариком, вылезшим из стены."
    
    x "Я не просто старик, я Хранитель трёх струн, которые оберегают наше королевство. Несколько дней назад кто-то украл струны, и поэтому наше королевство медленно, но верно погружается в пучину хаоса."
    x "Несколько сотен лет назад мне открылось пророчество, гласившее, что в самые тяжелые времена придёт тот, кто спасёт наш мир от разрушения."
    x "Прошу, помоги мне вернуть всё на свои места."
    
    show sasha normal at right
    sa "{i}Это какой-то бред, я наверняка сплю. Хотя, если я сплю, значит, со мной вряд ли что-то может случиться, верно?{/i}"
    sa "Ладно, Хранитель, но обещать ничего не могу."
    
    av "Хранитель улыбнулся, медленно кивнул головой и отправился к стене, где несколько минут назад рисовалась яркая воронка. Старец достал цветной камень и произнёс заклинание."
    
    x "Aperi, magicae portae, aperi et accipe me et hunc puerum ad locum Qui Vocatur Excogitatio"
    
    play sound portal
    
    show portal_rotate at center with dissolve
    
    av "Портал открылся."
    
    av "Хранитель зашел в него и исчез."
    hide x2 with dissolve
    av "[saname] подошёл ближе и увидел, как мерцает фиолетовый цвет в воронке."
    
    sa "{i}Почему мне раньше не снились такие сны? Надо будет обязательно записать, чтобы не забыть…{/i}"
    
    av "Парень смело шагнул в портал и оказался в совершенно незнакомом ему месте."
    
    hide sasha normal with dissolve
    hide portal_rotate with dissolve
    stop ambient
    jump start2    
    # Конец первой сцены 