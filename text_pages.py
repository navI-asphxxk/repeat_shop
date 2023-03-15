import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

import data

bot = telebot.TeleBot(BOT_TOKEN)


def text_nike_force_pages(message):
    count = len(data.nike_force_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"force\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_force_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/force/{page}.jpg', 'rb'),
                   caption=f'{data.nike_force_name_pages[0]}', reply_markup=markup)


def text_nike_dunk_high_pages(message):
    count = len(data.nike_dunk_high_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"dunk_high\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_dunk_high_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/dunk_high/{page}.jpg', 'rb'),
                   caption=f'{data.nike_dunk_high_name_pages[0]}', reply_markup=markup)


def text_nike_dunk_low_pages(message):
    count = len(data.nike_dunk_low_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"dunk_low\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_dunk_low_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/dunk_low/{page}.jpg', 'rb'),
                   caption=f'{data.nike_dunk_low_name_pages[0]}', reply_markup=markup)

def text_nike_monarch_pages(message):
    count = len(data.nike_monarch_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"monarch\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_monarch_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/monarch/{page}.jpg', 'rb'),
                   caption=f'{data.nike_monarch_name_pages[0]}', reply_markup=markup)


def text_nike_m2k_pages(message):
    count = len(data.nike_m2k_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"m2k\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_m2k_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/m2k/{page}.jpg', 'rb'),
                   caption=f'{data.nike_m2k_name_pages[0]}', reply_markup=markup)


def text_nike_plus_pages(message):
    count = len(data.nike_plus_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"plus\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.nike_plus_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/nike/plus/{page}.jpg', 'rb'),
                   caption=f'{data.nike_plus_name_pages[0]}', reply_markup=markup)

