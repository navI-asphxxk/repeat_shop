import json

import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

import data

bot = telebot.TeleBot(BOT_TOKEN)


def text_pages(message, brand, callback_string, data_price, data_name):
    count = len(data_name)
    page = 1
    markup = InlineKeyboardMarkup()

    # callback в формате json
    j_data_up = {"method": callback_string,
                 "NumberPage": page + 1,
                 "CountPage": count
                 }

    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data=json.dumps(j_data_up)))
    markup.add(InlineKeyboardButton(text=f'{data_price[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/{brand}/{callback_string}/{page}.jpg', 'rb'),
                   caption=f'{data_name[0]}', reply_markup=markup)

def text_nike_force_pages(message):
    text_pages(message, 'nike', 'force', data.nike_force_price_pages, data.nike_force_name_pages)


def text_nike_dunk_high_pages(message):
    text_pages(message, 'nike', 'dunk_high', data.nike_dunk_high_price_pages, data.nike_dunk_high_name_pages)


def text_nike_dunk_low_pages(message):
    text_pages(message, 'nike', 'dunk_low', data.nike_dunk_low_price_pages, data.nike_dunk_low_name_pages)

def text_nike_monarch_pages(message):
    text_pages(message, 'nike', 'monarch', data.nike_monarch_price_pages, data.nike_monarch_name_pages)


def text_nike_m2k_pages(message):
    text_pages(message, 'nike', 'm2k', data.nike_m2k_price_pages, data.nike_m2k_name_pages)


def text_nike_plus_pages(message):
    text_pages(message, 'nike', 'plus', data.nike_plus_price_pages, data.nike_plus_name_pages)

