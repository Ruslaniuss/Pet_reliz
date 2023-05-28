import play

play.set_backdrop("light blue")
eat = False


@play.when_program_starts#функція для початку програми
def start():
    global player, speech, facts
    text1 = play.new_text(words="г-грати, с-спати, ч-їсти, п-погладити", x=0, y=280, font_size=50)
    text2 = play.new_text(words="м-мити, л-лазити, т-танцювати, ф-факт про мене", x=0, y=240, font_size=40)
    player = play.new_image(image="Amigo_privetstvie.png", x=0, y=0, size=40)
    speech = play.new_text(words="Привіт, я Аміго!", x=0, y=-240, font_size=50)
    facts = play.new_text(words="", x=0, y=-270, font_size=30)
@play.repeat_forever#ігровий цикл
async def do():
    global eat
    if play.key_is_pressed("г"):
        player.size = 150
        player.image = "Amigo_stoit.jpg"
        speech.words = "Юххху ураааа, круто"
        #await play.timer(2.0)
        #speech.words = "Хочу ще!"
        #player.image = "Amigo_pauk.jpg"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Класно пограли, що будемо робити?"
        eat = True
    if play.key_is_pressed("с"):
        player.size = 80
        player.image = "Amigo_pauk.jpg"
        speech.words = "Я спати"
        await play.timer(5.0)
        speech.words = "Хррррр, хррррр"
        await play.timer(5.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я виспався, що будемо робити?"
    if play.key_is_pressed("ч") and eat == True:
        player.size = 150
        player.image = "Amigo_eda.jpg"
        speech.words = "Ммм, як смачно!"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я смачно поїв, що будемо робити?"
        eat = False
    if play.key_is_pressed("ч") and eat==False:
        speech.words = "Я вже наївся, пограй зі мною або полазь!"
    if play.key_is_pressed("п"):
        player.size = 150
        player.image = "Amigo_rad.jpg"
        speech.words = "Приємно"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Що будемо робити?"
    if play.key_is_pressed("л"):
        player.size = 150
        player.image = "Amigo_lazit.jpg"
        speech.words = "Лізь за мною!"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Прогулялися, що будемо робити?"
        eat = True
    if play.key_is_pressed("м"):
        player.size = 50
        player.image = "Amigo_moetsa.png"
        speech.words = "Купі купі"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я помився, що будемо робити?"
    if play.key_is_pressed("т"):
        player.size = 150
        player.image = "Amigo_tantsuet.png"
        speech.words = "Юхху"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я потанцював, що будемо робити?"
    if play.key_is_pressed("ф"):
        player.size = 150
        player.image = "Amigo_idet_po_tebya.jpg"
        speech.font_size = 30
        speech.words = "15 годин на добу лінивці сплять. А навіть коли не сплять, то пересуваються"
        facts.words = " дуже повільно і лише за необхідності (звідси назва)."
        await play.timer(5.0)
        speech.words = "У лінивців довга шия, що дозволяє їм досягати листя,"
        facts.words = " мінімально пересуваючись."
        await play.timer(5.0)
        speech.words = "Шия лінивців дуже рухлива та дозволяє повертати голову на 270 градусів, "
        facts.words = "має 8 або 9 шийних хребців."
        await play.timer(5.0)
        facts.words = ""
        speech.font_size = 50
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Правда цікаві факти? Що будемо робити?"
play.start_program()#запуск програми