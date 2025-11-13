import telebot
from telebot.types import Message
from config import API_TOKEN



bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
sup my homie! """)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    new_text = message.from_user.username + message.text.upper()    
    bot.reply_to(message, new_text)


bot.infinity_polling()
