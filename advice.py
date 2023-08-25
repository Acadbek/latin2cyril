import requests
from googletrans import Translator
from telebot import TeleBot

TOKEN = '6551237119:AAFdmLwgDrUOknvAF89RyXUFK_6lppaXPFg'
bot = TeleBot(TOKEN)

translator = Translator()

link = 'https://api.adviceslip.com/advice'

@bot.message_handler(func=lambda m: True)
def echo_all(msg):
    advice = requests.get(link).json()['slip']['advice']
    tarjima = translator.translate(advice, dest='uz')
    bot.reply_to(msg, tarjima.text)

bot.infinity_polling
