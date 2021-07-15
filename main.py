import telebot
from settings import *

bot =  telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'hello')

bot.polling()