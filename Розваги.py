import telebot
from telebot import types
import random


bot = telebot.TeleBot("ВСТАВТЕ СВІЙ ТОКЕН")
keyboard_films = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('комедія')
btn2 = types.KeyboardButton('бойовик')
btn3 = types.KeyboardButton('серіал')
btn4 = types.KeyboardButton('вихід в головне меню')



keyboard_films.add(btn1, btn2, btn3, btn4 )

keyboard_anecdote = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('тема IT')
button2 = types.KeyboardButton('тема рибалка')
button3 = types.KeyboardButton('тема про жінок')
button4 = types.KeyboardButton('тема про водіїв')
button5 = types.KeyboardButton('вихід в головне меню')

keyboard_anecdote.add(button1, button2, button3, button4, button5)


keyboard1_play_game = types.ReplyKeyboardMarkup()
butt1 = types.KeyboardButton('камінь')
butt2 = types.KeyboardButton('ножиці')
butt3 = types.KeyboardButton('папір')
butt4 = types.KeyboardButton('вихід в головне меню')

keyboard1_play_game.add(butt1, butt2, butt3, butt4)

@bot.message_handler(commands=['start'])
def first_command(message):
    bot.send_message(message.chat.id, "Привіт, я розважальний бот, радий тебе бачити" )

@bot.message_handler(commands=['info'])
def second_command(message):
    bot.send_message(message.chat.id, "Перелік всіх команд: \n /start\n /films\n/play_games\n/anecdote" )


@bot.message_handler(commands=['films'])
def fifth_command(message):
    bot.send_message(message.chat.id, "Який жанр Вам подобається?", reply_markup=keyboard_films )

@bot.message_handler(commands=['play_games'])
def fives_command(message):
    bot.send_message(message.chat.id, "Зіграємо в гру 'камінь, ножиці, папір", reply_markup=keyboard1_play_game)

@bot.message_handler(commands=['anecdote'])
def sixth_command(message):
    bot.send_message(message.chat.id, "Якщо хочете, то Бот Вам розкаже анекдот?", reply_markup=keyboard_anecdote )

@bot.message_handler(content_types=['text'])
def anecdot(message):
    user_choice=message.text
    if user_choice == "тема IT":
        bot.send_message(message.chat.id, "Програміст заглядає в холодильник і бере масло, на якому написано 72%."
                                          "Скоро завантажиться,подумав прогрміст,і поклав назад в холодильник.")

    elif message.text == "тема рибалка":
        bot.send_message(message.chat.id, "- Любий, пам'ятаєшь ти їздив на рибалку?"
                                          "- Так, пам'ятаю!"
                                          "- Щука твоя дзвонила, сказала, що з ікрою")

    elif message.text == "тема про жінок":
        bot.send_message(message.chat.id, "Вчора вчив дружину грати у 'World of Tanks'. "
                                          "Три години обирали зовнішність та прізвища танкістів")

    elif message.text == "тема про водіїв":
        bot.send_message(message.chat.id, "Любий,я не здала на права. -А що завалила, практику чи теорію?"
                                          "-ні, інспектора, дерево і двох бомжів")
    # elif message.text == "вихід в головне меню":
    #     second_command(message)

    elif message.text in ['камінь', 'ножиці', 'папір']:
        choice_list = ['камінь', 'ножиці', 'папір']
        comp_choice = random.choice(choice_list)
        if (message.text == 'камінь' and comp_choice == 'ножиці') or \
           (message.text == 'ножиці' and comp_choice == 'папір') or \
           (message.text == 'папір' and comp_choice == 'камінь'):
            bot.send_message(message.chat.id, f'Вибір користувача {user_choice}, вибір компютера  {comp_choice}.Виграв користувач')
        elif (message.text == 'ножиці' and comp_choice == 'камінь') or \
             (message.text == 'папір' and comp_choice == 'ножиці') or \
             (message.text == 'камінь' and comp_choice == 'папір'):
            bot.send_message(message.chat.id, f"Вибір користувача {user_choice}, вибір компютера  {comp_choice}.Виграв Бот")
        else:
            bot.send_message(message.chat.id, 'Перемогла дружба')

    # elif message.text == "вихід в головне меню":
    #     second_command(message)

    elif message.text == "комедія":
        bot.send_message(message.chat.id, "Тілоохоренець для кіллера."
                                          "Актори - Раян Рейнольдс, Семюель Л. Джексон, Сальма Гайєк, Елоді Юнґ, "
                                          "Ґері Олдмен, Хоакім Де Альмейда, Річард Е. Ґрант, Сем Гезелдайн, Род Галлетт  ")

    elif message.text == "бойовик":
        bot.send_message(message.chat.id, "Трансформери"
                                          "Актори - Шая Лабаф, Меган Фокс, Джош Дюамель, Тайріз Гібсон, Джон Туртурро, "
                                          "Рейчел Тейлор, Ентоні Андерсон, Джон Войт, Кевін Данн, Джулі Вайт")

    elif message.text == "серіал":
        bot.send_message(message.chat.id, "Пес"
                                          "Актори - Микита Панфілов, Михайло Жонін, Андрій Самінін, Ольга Олексій")

    elif message.text == "вихід в головне меню":
        second_command(message)



bot.polling()