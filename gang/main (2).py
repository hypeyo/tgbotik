import telebot
from config import API_TOKEN
from telebot.types import Message
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)


button1 = telebot.types.KeyboardButton(text="yo")
button2 = telebot.types.KeyboardButton(text="sup")
button3 = telebot.types.KeyboardButton(text="bro")
button4 = telebot.types.KeyboardButton(text="fr")
button5 = telebot.types.KeyboardButton(text="no way")
button6 = telebot.types.KeyboardButton(text="gang")
keyboard.add('yo', 'sup', 'bro', 'fr', 'no way', 'gang')



bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    hello_message = f'sup my homie! <b>{message.from_user.username}</b>'
    bot.send_message(
        message.chat.id,
        hello_message,
        reply_markup=keyboard,
        parse_mode= 'HTML'
    )
    state = 1

@bot.message_handler(func=lambda message: True)
def text_message(message: Message):
    global state
    if state == 1 and message.text == 'yo':
        bot.send_message(
            message.chat.id,
            'u went left to room 2'
        )
        state = 2
    elif state == 1 and message.text == 'sup':
        bot.send_message(
            message.chat.id,
            'u went right to room 3'
        )
        state = 3
    elif state == 2 and message.text == 'bro':
        bot.send_message(
            message.chat.id,
            'u went right to room 4'
        )
        state = 4
    elif state == 3 and message.text == 'gang':
        bot.send_message(
            message.chat.id,
            'u went right to room 6'
        )
        state = 6
    elif state == 2 and message.text == 'fr':
        bot.send_message(
            message.chat.id,
            'u went right to room 5'
        )
        state = 5
    elif state == 3 and message.text == 'no way':
        bot.send_message(
            message.chat.id,
            'u went right to room 5'
        )
        state = 5
    else:
        bot.send_message(
            message.chat.id,
            'something went wrong'
        )


bot.infinity_polling()
