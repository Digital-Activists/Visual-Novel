#начало третьей сцены 
label start3:
    scene stolica with dissolve
    play music city fadein 2
    av "[saname] вновь оказался в незнакомом ему месте совсем один."
    av "Однако вместо дремучего леса перед ним появился громадный город – столица королевства Девизарион."

    scene vorota with dissolve
    av "[saname] прошёл городские ворота и понял, что никогда не видел столь живописного места: столица стояла на возвышенности, поэтому казалось, что верхушки зданий касались облаков."
    av "Столица была настолько большой, что в ее пределах умещался лес и водопад, рынок, куда съезжались торговцы со всех соседних королевств, широкая мощеная камнем площадь, поселение жителей и, конечно, дворец Короля."
    av "Жизнь в столице шла свои чередом: жители улыбались, смеялись, ругались, решали бытовые проблемы, работали, но никто не говорил о пропавших струнах."
    av "В городе не было ни паники, ни хаоса, к тому же все готовились к какому-то празднику."
    show sasha normal at right with dissolve 
    sa "{i}Странно, почему до поселения бэндров дошли слухи, а досюда нет?{/i}"
    sa "{i}Попробую что-нибудь узнать.{/i}"
    sa "{i}Где в большом городе чаще всего появляются слухи? Наверное, в какой-нибудь местной харчевне. Выпивка многим развязывает язык.{/i}"
    av "Харчевня “На распутье” находилась рядом с городскими воротами, в воздухе витал запах пива и вина, слышались песни и крики радостных жителей, которые были похожи на людей."
    av "Однако высокий рост,  длинные руки и очень тонкие пальцы выдавали в них магических существ."
    av "[saname] догадался, что это были фентиры. В харчевне вместе с ними пили бэндры и обычные на вид люди - жители других королевств."
    
    scene bar with dissolve
    stop music
    play music taverna
    show sasha normal at right with dissolve
    av "Зайдя в здание, [saname] ощутил на себе несколько пристальных взглядов, но, не обращая на них внимания, подошёл к барной стойке."
    av "Он хотел поговорить с управляющим, но его прервали…"
    av "[saname] увидел рядом с собой фентира, в глазах которого читалась грусть и тоска. Он сидел за стойкой и допивал свою пинту пива."
    show xalon at left with dissolve
    
    if (count == 0):
        $fentir = 'Фентир'
        
    fentir "Давно я не видел в наших краях таких, как ты."
    sa "Таких, как я, это каких?"
    fentir "Людей. Последний раз человека видели, когда создавался Девизарион. Согласно одной из легенд, человек сотворил наше Королевство."
    sa "Один дворф говорил мне, что Девизарион создал бэндр. Кому мне верить?"
    fentir "Дворфы склонны гордиться тем, что не имеет к ним никакого отношения. К тому же, все думают по-разному..."
    fentir "Фентиры считают, что Создатель был фентиром, дворфы - бэндром. Лишь фуллирианы знают правду, но молчат." 
    show sasha pensive at right 
    sa "{i}Странный этот фентир. Он либо изрядно выпил, либо что-то хочет от меня.{/i}"
    show sasha normal at right
    fentir "Никому не говори, что ты человек. Некоторые считают, что люди приносят несчастья. Когда в королевстве прознают, что струны пропали, ты можешь остаться без головы." 
    show sasha surprised at right
    sa "Так ты знаешь, что струны пропа…?!"
    fentir "Тише, тише. Нельзя, чтобы кто-то знал. Я много чего знаю, например, что тебя привёл Хранитель и что ты должен нас спасти."
    fentir "Знаешь, я не верю в эту чепуху. Ты простой мальчишка, как только Хранитель нашел тебя?"
    show sasha angry at right 
    sa "Я не просил, чтобы меня находили."
    fentir "Конечно, нет."
    show sasha normal at right
    fentir "Хорошо, что ты нашёл меня. Хранитель предупреждал о твоем прибытии. Я помогу тебе в поиске второй струны, но на многое не надейся." 
    fentir "О пропаже струн никто не знает, только приближенные Короля. Слухи, конечно, рано или поздно дойдут до каждого, но панику лучше отложить на потом."
    fentir "Король тайно направил все военные силы на поиск струн, а Хранителю приказал найти тебя, поэтому о твоем прибытии знаю только я, Король и волшебник."
    fentir "Если ты заметил, жители празднуют тридцатитрёхлетие Девизариона, в столицу приехали представители других королевств, возможно, среди них есть предатель."
    fentir "Струны можно использовать как могущественнейшее оружие, не исключено, что одну из них мог похитить шпион."
    fentir "Направляйся на главную площадь и попробуй что-нибудь выяснить. Сблизься с простыми рабочими, они могли что-то видеть или слышать, заодно узнаешь, чем занимается большая часть фентиров."
label qes:
    scene bar
    show sasha normal at right
    show xalon at left
    
    menu:
        "Кто ты такой?":
            jump qesone
        "Кто такие фентиры?":
            jump qestwo
        "Из кого состоит армия Короля?":
            jump qesthree
        "Вопросов нет.":
            jump select
        
label qesone:
    scene bar
    show sasha normal at right
    show xalon at left
    sa "Кто ты такой?"
    fentir "Я Халлон, начальник личной стражи Короля. Я служу ему уже больше десяти лет."
    $count += 1
    if(count > 0):
        $fentir = 'Халлон'
    fentir "Он призвал меня, когда королевство вело войну с аккарами, и попросил возглавить его армию."
    fentir "Война была выиграна, но не было ни пиршеств, ни радостных песен. Многие потеряли в этой войне близких и родных…"
    sa "{i}Его взгляд такой печальный, как будто он тоже лишился кого-то.{/i}"
    sa "{i}Не буду на него давить.{/i}"
    jump qes
label qestwo:
    scene bar
    show sasha normal at right
    show xalon at left
    sa "Кто такие фентиры?"
    fentir "Фентиры - это существа, преобразующие магию из камней, которые добывают бэндры."
    fentir "Они могут по-разному использовать магию."
    fentir "Cоздавать внешний вид заказов для других королевств, наполнять предметы красотой и доступностью для покупателя, изготавливать для него удобную среду пользования."
    sa "{i}Как же фентиры напоминают мне фронтенд-разработчиков, даже странно.{/i}"
    sa "{i}Фронтенд-разработчики ведь тоже занимаются разработкой графического интерфейса, создают сайты, удобные и доступные для пользователя.{/i}"
    jump qes
label qesthree:
    scene bar
    show sasha normal at right
    show xalon at left
    sa "Из кого состоит армия Короля?"
    fentir "Из фентиров, бэндров и в большей степени атирусов."
    fentir "Когда шла война с аккарами армия состояла из фентиров и бэндров, однако они не  могли справиться с противником."
    fentir " Поэтому Король призвал на помощь атирусов - воинов другого королевства. Война закончислась."
    jump qes
    
label select:
    scene bar
    show sasha normal at right
    show xalon at left
    sa "Мне пора идти, как мне потом найти тебя?"
    fentir "Подойти ко дворцу и скажи, что я приказал тебя пропустить."
    sa "До встречи."
    stop music
    
    scene vorota with dissolve
    show sasha normal at right with dissolve
    
    av "[saname] вышел из харчевни и долго думал о Халлоне: фентиру можно было доверять, однако взгляд, полный тоски и печали, беспокоил юношу."
    av "Халлон как будто бы не хотел жить, как будто в этом мире для него не осталось света."
    av "Незаметно для себя [saname] подошел к площади."
    scene ploshad with dissolve
    show sasha normal at right with dissolve
    stop music
    
    play music helpers fadein 2
    av "На площади все суетились: кто-то украшал дома, кто-то репетировал песни и танцы, кто-то подметал улицы, кто-то готовился открыть лавку с товарами."
    av "Однако внимание парня привлёк один очень беспокойный фентир, он всем раздавал указания и причитал..."
    show fentir at left with dissolve
    fen "Мы ничего не успеваем!"
    sa "Здравствуй, господин, не нужна ли вам какая-нибудь помощь?"
    fen "С чего бы это тебе мне помогать?"
    sa "Я слышал, что вы ничего не успеваете. Так почему бы не помочь доброму человеку?"
    fen "Да, мы ничего не успеваем подготовить к празднику, а торжество начнется уже вечером."
    fen "Нашему королевству нельзя ударить в грязь лицом."
    fen "Я дам тебе 2 задания, как выполнишь, возвращайся ко мне."
    hide fentir with dissolve
    $zadaniya = 0
label zadanie:
    scene ploshad
    show sasha normal at right
    menu:
        "Что сделать в первую очередь?"
        "Помочь украсить площадь":
            jump paintpl
        "Помочь составить расписание праздника":
            jump raspisanie

#ПОМОГАЕТ УКРАШАТЬ ПЛОЩАДЬ
label paintpl:
    $zadaniya += 1
    scene ploshad
    show sasha normal at right
    av "[saname] подошёл к нескольким фентирам.  Они не могли решить, с чего начать работу."
    show nxtfen at left with dissolve:
        xalign -0.1
    show fentir2 at center with dissolve:
        xalign 0.15
    f1 "Я говорю, что нужно начинать с огней, а потом расставить палатки!"
    f2 "Да что ты понимаешь, бестолочь! А про украшения ты не забыл?"
    show sasha normal at right with dissolve
    sa "Подождите, давайте не будем ругаться. Сделаем всё поэтапно."
    f1 "А ты кто вообще такой?"
    sa "Я вызвался помочь вам подготовиться к празднику, спросите вон у того господина."
    f2 "Раз вызвался - помогай! У нас есть есть план того, как должна выглядеть площадь к празднику."
    f2 "Дома должны быть украшены цветами и флажками, в фонари нужно положить камни, чтобы они освещали гостям путь, и нужно расставить палатки."
    sa "{i}Уже смеркается, а на площади совсем темно. Если кто-то упадет в темноте, будет плохо.{/i}"
    sa "Для начала добавим немного света!"
    av "Фентиры вручили парню три маленьких камня и разделились."
    hide nxtfen with dissolve
    hide fentir2 with dissolve
    $fonari = 0
#Действие в paintpl
label deyst:
    scene ploshad
    show sasha normal at right 
    menu:
        "К какому фонарю подойти?"
        "Фонарь рядом с входом на площадь.":
            jump ffonar
        "Фонарь рядом с домом на колёсах приезжих артистов.":
            jump tfonar
        "Фонарь рядом со сценой":
            jump thfonar
label ffonar:
    $fonari += 1
    scene ploshad
    show sasha normal at right
    av "[saname] залез на передвижную лестницу и зажег фонарь."
    sa "Да будет свет!"
    if fonari == 3:
        jump sl
    else:
        jump deyst
    
label tfonar:
    $fonari += 1
    scene ploshad
    show sasha normal at right
    av "[saname] залез на передвижную лестницу и зажег фонарь."
    sa "Готово!"
    av "Вдруг из дома на колёсах послышались голоса."
    menu:
        "Подслушать":
            jump podsl
        "Не подслушивать":
            if fonari == 3:
                jump sl
            else:
                jump deyst
label podsl:
    scene ploshad
    show sasha pensive at right
    av "[saname] оперся на стену дома и услышал разговор двух артистов."
    ao "Я тут услышал, что в королевстве беда. Струны украли, король теперь беззащитен."
    ao "Что он будет делать без своей магии?"
    atwo "У короля сильная армия. Да и тебе то что? Может, это вообще неправда."
    ao "Правда! Я подслушал разговор двух старух на рынке. Странно, что весь город об этом не судачит."
    atwo "А кто украл?"
    av "Внезапно передвижная лестница, на которой стоял [saname], качнулась, и юноша упал."
    av "Голоса стихли."
    show sasha angry at right
    sa "{i}Чёрт,я почти узнал, кто украл струны!{/i}"
    if fonari == 3:
        jump sl
    else:
        jump deyst
    
label thfonar:
    $fonari += 1
    scene ploshad
    show sasha normal at right 
    av "[saname] залез на передвижную лестницу и зажег фонарь."
    sa "Получилось!"
    if fonari == 3:
        jump sl
    else:
        jump deyst

label sl:
    #нужна локация с темной площадью чтобы поставить здесь светлую
    scene ploshad
    show sasha normal at right 
    sa "{i}Отлично, теперь на площади светло. Кажется, что фентиры уже расставили палатки с угощениями для гостей. Осталось только украсить площадь.{/i}"
    show nxtfen at left with dissolve:
        xalign -0.1
    show fentir2 at center with dissolve:
        xalign 0.15
    f1 "Хорошая работа. Мы фентиры в первую очередь всегда заботимся о комфорте заказчика."
    f1 "Конечно, внешний вид конечного продукта важен, но не стоит забывать о практичности."
    f1 "Теперь слушай внимательно."
    f1 "Одна из задач фентиров - сбор заказов, которые не только удовлетворяют требованиям покупателя к внешнему виду, но и удобны для него."
    f1 "То есть для каждого королевства, в которое поставляются наши товары, мы создаем что-то уникальное."
    f2 "На площади соберуться представители разных королевств, у каждого королевства есть флаг определенного цвета, поэтому все цвета должны присутствовать на площади."
    f2 "Твоя задача вот этим камнем изменять цвета украшений в соответствии с королевством."
    f2 "А теперь самое главное."
    f2 "Королевство Ротерион - {color=#ff0000}красный цвет.{/color}"
    f2 "Анатлион - {color=#008000}зеленый цвет{/color}."
    f2 "Девизарион - {color=#FFFF00}жёлтый цвет{/color}."
    f2 "Атирион - {color=#0000FF}синий цвет{/color}."
    f2 "А мы пока пойдём расставлять цветы."
    sa "Ну вроде бы запомнил. Думаю, для фентиров это очень важно."
    av "[saname] подошёл к бесцветным украшениям, висящих на стенах домов. Рядом с украшениями на маленьких бумажках были подписаны названия королевств."
    hide nxtfen with dissolve
    hide fentir2 with dissolve
    jump firstvopros
label firstvopros:
    scene ploshad
    show sasha normal at right
    $pravotvet = 0
    menu:
        "Королевство Анатлион. Какой цвет?"
        "Зеленый":
            $pravotvet += 1
            jump secondvopros
        "Желтый":
            jump secondvopros
        "Красный":
            jump secondvopros
        "Синий":
            jump secondvopros
label secondvopros:
    scene ploshad
    show sasha normal at right
    menu:
        "Королевство Девизарион. Какой цвет?"
        "Красный":
            jump thirdvopros
        "Синий":
            jump thirdvopros
        "Желтый":
            $pravotvet += 1
            jump thirdvopros
        "Зеленый":
            jump thirdvopros
        
label thirdvopros:
    scene ploshad
    show sasha normal at right
    menu:
        "Королевство Ротерион. Какой цвет?"
        "Желтый":
            jump fourvopros
        "Синий":
            jump fourvopros
        "Зеленый":
            jump fourvopros
        "Красный":
            $pravotvet += 1
            jump fourvopros
            
label fourvopros:
    scene ploshad
    show sasha normal at right
    menu:
        "Королевство Атирион. Какой цвет?"
        "Зеленый":
            jump itog
        "Синий":
            $pravotvet += 1
            jump itog
        "Красный":
            jump itog
        "Желтый":
            jump itog

label itog:
    scene ploshad
    show sasha normal at right
    show nxtfen at left with dissolve:
        xalign -0.1
    show fentir2 at center with dissolve:
        xalign 0.15
    
    if pravotvet == 4:
        f1 "Ого, ты справился с первого раза!"
        f2 "Ты можешь стать первоклассным фентиром. За такую отличную работу мы подарим тебе этот камень на память!"
        sa "Спасибо!"
        sa "Мне уже пора, я был рад познакомиться!"
        hide nxtfen with dissolve
        hide fentir2 with dissolve
        if(zadaniya == 2):
            jump nextvetka
        else:
            jump zadanie
    elif pravotvet == 3:
        f1 "Ого, ты справился с первого раза!"
        f2 "Ты можешь стать первоклассным фентиром."
        sa "Спасибо!"
        sa "Мне уже пора, я был рад познакомиться!"
        hide nxtfen with dissolve
        hide fentir with dissolve
        if(zadaniya == 2):
            jump nextvetka
        else:
            jump zadanie
    else:
        f1 "Чёрт, сегодня не наш день. Придётся переделывать."
        f2 "Не расстраивайся, парень. Ни у кого с первого раза не получается."
        sa "Простите, что доставил неудобства."
        sa "Мне уже пора, я был рад познакомиться!"
        hide nxtfen with dissolve
        hide fentir with dissolve
        if(zadaniya == 2):
            jump nextvetka
        else:
            jump zadanie
    
label raspisanie:
    $zadaniya += 1
    scene vorota 
    av "[saname] подошёл к фентире, стоящей рядом со входом на площадь."
    show sasha normal at right with dissolve 
    show fentira at left with dissolve
    sa "Здравствуй, госпожа. Меня прислали, чтобы помочь тебе."
    fentira "Здравствуй, путник. Перейдём сразу к делу, праздник начнется совсем скоро."
    fentira "Одной из нескольких задач фентиров является адаптация заказа для покупателя."
    fentira "Если быть точнее, в разных королевствах наши продукты могут выглядеть по-разному, поэтому фентиры делают несколько версий проектов для разных королевств."
    sa "{i}Я понял, в моем мире фронтенд-разработчик отвечает за то, чтобы сервис корректно работал на разных устройствах.{/i}"
    fentira "Многие гости из других королевств разговаривают на других языках. Но расписание праздника написано только на языке Девизариона."
    fentira "Пожалуйста, переведи расписание на другой язык."
    sa "Будет сделано!"
    hide fentira with dissolve
    show sasha pensive at right
    sa "{i}Как я смогу перевести расписание на другой язык, если я сам знаю только язык Девизариона?{/i}"
    jump translate

label translate:
    scene vorota 
    show sasha normal at right 
    $perevod = 0
    menu:
        "Как перевести фразу \"расписание мероприятия\"?"
        "Event schedule":
            $perevod += 1
            jump translate2
        "Something incomprehensible":
            jump translate2
        "Идите вон":
            jump translate2
            
label translate2:
    scene vorota 
    show sasha normal at right 
    menu:
        "Как перевести фразу \"огненное шоу\"?"
        "Девизарион объявляет войну":
            jump translate3
        "Fire show":
            $perevod += 1
            jump translate3
        "The strings are gone":
            jump translate3

label translate3:
    scene vorota 
    show sasha normal at right
    menu:
        "Как перевести фразу \"представления артистов\"?"
        "Performances of artists":
            $perevod += 1
            jump translateend
        "Зима близко":
            jump translateend
        "The King is dead":
            jump translateend
            
label translateend:
    scene vorota
    show sasha normal at right
    show fentira at left with dissolve
    if perevod == 3:
        fentira "Ты отлично справился с работой. Спасибо. Ты настоящий фентир."
        fentira "Надеюсь, ты понял, как важна наша работа, ведь если мы допустим хотя бы одну ошибку, заказчик может нас неправильно понять."
        sa "Да, я понял. Спасибо за такой ценный урок."
        sa "Думаю, мне пора идти."
        hide fentira with dissolve
        if(zadaniya == 2):
            jump nextvetka
        else:
            jump zadanie
    else:
        fentira "О, нет. Теперь придётся всё  делать самой. Зря я тебе доверилась."
        sa "Думаю, мне пора идти."
        hide fentira with dissolve
        if(zadaniya == 2):
            jump nextvetka
        else:
            jump zadanie

label nextvetka:
    scene vorota 
    show sasha normal at right 
    
    sa "Пора возвращаться к фентиру, который давал мне задания."
    hide sasha normal with dissolve
    stop music fadeout 2
    play music city 
    scene ploshad with dissolve 
    show sasha normal at right with dissolve
    show fentir at left with dissolve 
    sa "Господин, я выполнил задания."
    fen "Благодарю. Теперь мы успеем подготовиться к празднику. В качестве награды прими этот билет в первый ряд."
    sa "Спасибо!"
    fen "Скажи, ты понял, чем занимаются фентиры?"
    sa "Да, они преобразуют магию из камней, с помощью которой изменяют заказы других королевств, делая их красивыми, удобными и функциональными."
    fen "Верно!"
    sa "До встречи, господин."
    hide fentir with dissolve
    sa "{i}Жаль, что я не узнал ничего полезного насчет пропажи струн. Интересно, что выяснил Халлон?{/i}"
    av "[saname] был рад, что смог помочь фентирам. Ему понравилась их работа."
    av "Однако поиск второй струны затягивался на неопределенный срок."
    av "Парень подошёл к дверям дворца, прошёл через стражу и оказался в кабинете у Халлона."
    hide sasha normal with dissolve
    stop music
    
    scene kabinet with dissolve
    show sasha normal at right with dissolve
    av "Кабинет выглядел мрачно: один деревянный стол, одно маленькое окно, книжный шкаф."
    show xalon at left with dissolve
    av "На столе стоял подсвечник, а рядом с ним стопка писем. Халлон сидел за столом и что-то читал."
    fentir "Удалось выяснить что-нибудь?"
    sa "Боюсь, что нет."
    sa "Я слышал, как два приезжих артиста разговаривали о пропаже струн, но они только обсуждали слухи."
    sa "Я не смог подслушать что-то важное."
    fentir "Ясно."
    fentir "Хранитель прислал сову. Он был у аккаров."
    fentir "Ты же знаешь, что Хранитель по приказу Короля использует магию, чтобы сдерживать аккаров, пока струны не нашли."
    fentir "Так вот аккары перестали реагировать на магию."
    fentir "Сильнее магии Хранителя в этом мире только магия струн и Короля."
    fentir "Я могу предположить, что вторая струна у аккаров. Если это так, мы не сможем победить их."
    fentir "Они опасные существа, они не имеют ни чести, ни сочувствия. Они убивают быстро и беспощадно. Они..они…"
    
    menu:
        "Не давить на Халлона":
            jump vetka2
        "Расспросить Халлона":
            jump sprosxalon

label sprosxalon:
    scene kabinet
    show sasha normal at right
    show xalon at left 
    
    sa "Они что?"
    fentir "Они убили мою семью. Во время войны."
    fentir "Король ещё не призвал армию атирусов. Аккары нападали на деревни, на города, убивали и фентиров, и бэндров."
    fentir "Никого не оставляли на своём пути. Не жалели даже женщин и детей. Поганые твари!"
    fentir "Я сражался в то время у окраин королевства. Моя семья жила рядом со столицей."
    fentir "Как только война закончилась, я ринулся к возлюбленной. Я думал о том, как она встретит меня, я увижу ее улыбку и расплачусь…"
    fentir "Но ничего этого не было. Она умерла, вместе со всеми жителями поселения."
    fentir "Аккары сожгли всё до тла. Пустота и пепел. Я так и не нашёл ее тело."
    fentir "Глубоко в душе я верю, что она где-то ждет меня, что она не умерла, что вся эта ужасная война была дурацкой шуткой."
    sa "Халлон, мне очень жаль."
    av "Халлон промолчал"
    jump vetka2
    
label vetka2:
    scene kabinet 
    show sasha normal at right
    show xalon at left
    av "На улице становилось совсем темно, однако огромная луна вышла из-за туч и осветила всю столицу."
    av "[saname] выглянул из окна и увидел, как собираются на площади фентиры, бэндры и представители других королевств, как они готовятся праздновать тридцатитрёхлетие Девизариона."
    av "Как весело им жилось в неведении..."
    sa "Мне дали билет в первый ряд на праздник, не хочешь пойти со мной?"
    fentir "Боюсь, что это не для меня."
    fentir "Иди и повеселись, а потом вновь приходи сюда."
    av "[saname] уже хотел выйти из комнаты, как вдруг в дверь постучали."
    play sound kickdoor
    voin "Милорд, на столицу напали! Аккары!"
    av "Халлон подскочил со стула и посмотрел на парня."
    fentir "Бежим."
    
    scene stairs with dissolve
    show sasha2 at left with dissolve   
    #show fentirvoin at right with dissolve
    show xalon2 at right with dissolve:
        xalign 0.7
    show fentirvoin at right with dissolve
    play ambient stairs
    av "[saname], Халлон и фентир-воин бежали вниз по лестнице."
    fentir "Где они сейчас?"
    voin "Направляются к площади."
    fentir "Там сейчас весь город и гости других королевств!"
    fentir "Сколько у нас есть человек?"
    voin "Только личная охрана Короля, 15 человек."
    fentir "А сколько их?"
    voin "Около двух-трёх сотен."    
    av "Все трое выбежали из дворца и направились к площади."
    stop ambient
    
    scene ploshad with dissolve
    play music fight fadein 2
    av "На площади началась паника, все старались убежать, спрятаться, но аккары не щадили никого."
    av "Запахло кровью."
    scene ploshadp with dissolve 

    show sasha angry at right with dissolve
    show xalon at left with dissolve 
    fentir "Лови!"
    av "Халлон кинул парню небольшой меч."
    fentir "Попробуй остаться в живых."
    hide xalon with dissolve
    play ambient knife
    av "Халлон побежал собирать личную охрану Короля. [saname] остался один, он стоял на площади и не знал, что ему делать."
    av "То ли спасаться самому, то ли спасать других."
    av "Как вдруг сзади него послышалось что-то похожее на рычание."
    av "[saname] обернулся и увидел высокое существо без лица."
    show vzlom with dissolve:
        yalign 0.2
        xalign -0.1
    av "Это был аккар, который намеревался убить его."
    av "Аккар был безоружен, поэтому было неясно, как он собирается атаковать."
    av "Аккар замахнулся рукой и ударил парня."
    show sasha surprised at right 
    sa "{i}О, Боже, как больно!{/i}"
    show sasha angry at right
    av "Аккар сделал выпад вправо."
    jump fight

label fight:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    menu:
        "Что делать?"
        "Стоять на месте":
            jump action1
        "Отпрыгнуть назад":
            jump action2
        "Наклониться вправо":
            jump action3
        "Наклониться влево":
            jump action4

label action1:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] не вынес второго удара."
    scene background with dissolve
    "Аккар убил вас."
    jump fight
    
label action2:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] пережил удар."
    jump fight2
    
label action3:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] не вынес второго удара."
    scene background with dissolve
    "Аккар убил вас."
    jump fight
    
label action4:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] пережил удар."
    jump fight2

label fight2:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "Аккар сделал выпад влево."
    menu:
        "Что делать?"
        "Стоять на месте":
            jump actionone
        "Отпрыгнуть назад":
            jump actiontwo
        "Наклониться вправо":
            jump actionthird
        "Наклониться влево":
            jump actionfour

label actionone:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] не вынес удара."
    scene background with dissolve
    "Аккар убил вас."
    jump fight2

label actiontwo:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] пережил удар."
    jump poslefight

label actionthird:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] пережил удар."
    jump poslefight

label actionfour:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1
    av "[saname] не вынес удара."
    scene background with dissolve
    "Аккар убил вас."
    jump fight2
    
    
label poslefight:
    scene ploshadp
    show sasha angry at right 
    show vzlom:
        yalign 0.2
        xalign -0.1 
        
    av "[saname] вонзил в аккара меч, существо упало замертво."
    hide vzlom with dissolve
    sa "Черт, я убил его! Я убил аккара!"
    sa "Надо бежать дальше."
    av "[saname] побежал на середину площади, нужно было спасать простых жителей."
    av "Как раз подоспели Халлон и охрана Короля."
    av "Они быстро расправились с несколькими аккарами. Но врагов всё равно было гораздо больше."
    av "Ничего не оставалось делать, кроме как сражаться."
    
     # МУЗ ПАУЗА КОГДА БДЕТ МУЗЫКА
     
    av "[saname] мужественно одолел двух аккаров и спас гостью из другого королевства от верной смерти."
    av "Парень огляделся, аккары терпели поражение. Халлон и его отряд были очень подготовленными бойцами."
    av "[saname] уже начал радоваться, как вдруг убитые аккары поднялись с земли."
    av "Это было похоже на магию, очень темную магию."
    av "Юноша посмотрел на Халлона и увидел ужас на его лице."
    sa "{i}Значит, этого не было раньше! Что же делать?{/i}"
    av "Площадь заполонили аккары. А во главе них стоял особенный аккар."
    av "Он держал в руке струну и теперь мог не только управлять своей армией, но и воскрешать аккаров."    
    av "Аккары стали бессмертными, непобедимыми."
    av "Несколько фентиров из отряда Халлона подбежали к предводителю аккаров, но он лишь взмахнул рукой и отбросил их назад."
    av "Фентиры потеряли сознание."
    av "Как можно было победить непобедимого врага?"
    av "Парню и Халлону в голову пришла одна и та же мысль - нужно отобрать струну."
    hide sasha angry with dissolve
    
    show xalon2 at right with dissolve
    show glav at left with dissolve
    
    av "Ослабленный Халлон побежал к аккару, но тот не стал использовать магию струны, а вытащил клинок."
    glav "Давно мы не виделись, Халлон. Всё ещё хочешь отомстить за ту девку? Как там её звали?"
    fentir "Ее звали Элениэль!"
    
    av "Халлон ударил аккара, но тот отразил мощный удар и ударил фентира в ответ."
    av "С руки Халлона закапала кровь."
    glav "Да-да, точно. Она была такой хрупкой, я лично навестил ваш дом в тот день."
    glav "Знаешь, убивать ее было очень приятно, но еще приятнее было представлять твоё лицо, когда ты найдешь ее бездыханное тело."
    glav "Постой, так от нее даже тела не осталось. Ха-ха-ха."
    av "Халлон с силой ударил несколько раз по туловищу аккара, но раны на его теле в мгновение затянулись."
    glav "Халлон, ты стал таким слабым и беспомощным, как же ты будешь защищать своего драгоценного короля?"
    glav "Покончим с этим!"
    av "Аккар достал струну и начал говорить заклинание, однако Халлон отрубил его руку, струна упала на землю."
    av "Вместе с ней на землю упал и Халлон."
    av "Предводитель аккаров проткнул его грудь клинком."
    av "Изо рта Халлона потекла кровь."
    glav "Ты думал, меня так легко убить? Обычным мечом?"
    hide xalon2 with dissolve
    show sasha angry at right with dissolve
    sa "А этим получиться тебя убить?"
    av "[saname] незаметно для предводителя аккаров подобрал струну и выставил ее перед собой."
    glav "Ах ты, паршивец! Маленький, гадкий человечишко!"
    av "Аккары стали окружать парня, как вдруг, неожиданно для себя самого, он сказал заклинание."
    sa "Discite iustitiam, si vive!"
    av "Один за другим аккары стали падать на землю."
    av " Последним упал и предводитель аккаров."
    hide glav with dissolve
    stop ambient
    stop music fadeout 2
    av "Битва была окончена."
    
    av "[saname] подбежал к умирающему Халлону, сел рядом с ним на колени."
    show sasha gr at right
    show xalon at left with dissolve 
    sa "Халлон, нет, не умирай. Ты нужен королевству, прошу, не умирай."
    sa "Лекаря! Позовите лекаря!"
    fentir "Ты молодец. Я зря сомневался в тебe. Я никогда так не ошибался в своей жизни."
    fentir "Поверь, я давно думал о смерти. Как думаешь, есть ли жизнь после смерти?"
    fentir "Если есть, то я вновь увижу мою Элениэль."
    sa "Конечно, Халлон. Ты обязательно увидишь её."
    fentir "Хорошо."
    av "Халлон умер."
    av "На площади стояла мертвая тишина."
    av "[saname] сидел рядом с Халлоном и плакал. Он не заметил, как потерял сознание."
    hide sasha gr with dissolve
    hide xalon with dissolve
    
    
    scene komnata
    show sasha normal at right with dissolve 
    av "[saname] очнулся в какой-то комнате. Было утро. Рядом на кровати сидел Хранитель."
    sa "Халлон!"
    show x2 at left with dissolve 
    x "Да, я знаю."
    x "Прости, что не пришел раньше. Вы храбро сражались."
    x "Вас всех должен благодарить не только Девизарион, но и другие королевства."
    x "Аккары не остановились бы только на Девизарионе."
    x "Халлон погиб достойно. Я у него в вечном долгу."
    sa "Нам нужно найти последнюю струну, ты знаешь, где она?"
    x "У фуллирианов."
    sa "Телепортируй меня"
    x "Но ты еще слишком слаб!"
    show sasha angry at right 
    sa "Я сказал, телепортируй меня! Я докажу, что Халлон умер не напрасно."
    x "Будь по-твоему. Я не смогу отправиться с тобой. Я всё ещё слишком слаб, чтобы защищать тебя."
    av "Хранитель сказал заклинание и открыл портал."
    play sound portal
    show portal_rotate at center with dissolve
    hide sasha angry with dissolve
    x "Боюсь, что это будет самой опасной частью твоего путешествия."
    jump start4
    #КОНЦЕ третьей сцены
    
    
        