import os

import requests
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

bot = TeleBot(token=os.getenv('TOKEN'))
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat


@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    chat = message.chat
    name = message.chat.first_name

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Попробуй ввести команду /newcat',
    )

    # bot.send_photo(chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Попробуй ввести команду /newcat')


bot.polling()