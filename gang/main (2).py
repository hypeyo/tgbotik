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
keyboard.add(button1)
keyboard.add(button2)
keyboard.add('yo', 'sup')



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
    if state == 1 and message.text == 'Left':
        bot.send_message(
            message.chat.id,
            'u went left to room 2'
        )
        state = 2
    elif state == 1 and message.text == 'Right':
        bot.send_message(
            message.chat.id,
            'u went right to room 3'
        )
        state = 3
    else:
        bot.send_message(
            message.chat.id,
            'something went wrong'
        )


bot.infinity_polling()
