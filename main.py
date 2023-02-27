import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import json

from telegram_bot_pagination import InlineKeyboardPaginator

import callback_pages
import text_pages

bot = telebot.TeleBot('5873814230:AAGfDLmGCzWNFexqkAmPNm4pvEIv2GTYy9M')


def main_menu():
    # Кол-во позиций в меню клавиатуры - много
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    info = types.KeyboardButton(text='📢Информация')
    helping = types.KeyboardButton(text='❓Помощь в выборе')
    katalog = types.KeyboardButton(text='🛍️Каталог')
    feedback = types.KeyboardButton(text='📩Ваши предложения')
    media = types.KeyboardButton(text='🔗Наша группа')

    keyboard_menu.add(info, helping)
    keyboard_menu.add(katalog)
    keyboard_menu.add(feedback, media)

    return keyboard_menu


def katalog_menu():
    # Кол-во позиций в меню клавиатуры - много
    katalog_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    nike = types.KeyboardButton(text='👟Nike')
    adidas = types.KeyboardButton(text='Adidas')
    reebok = types.KeyboardButton(text='Reebok👟')
    converse = types.KeyboardButton(text='👟Converse👟')
    back = types.KeyboardButton(text='🔙Назад в главное меню')

    katalog_menu.add(nike, adidas, reebok)
    katalog_menu.add(converse)
    katalog_menu.add(back)

    return katalog_menu


def menu_nike():
    nike_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    force = types.KeyboardButton(text='Air Force 1 low')
    monarch = types.KeyboardButton(text='Air Monarch')
    m2k = types.KeyboardButton(text='M2K Tekno')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    nike_menu.add(force, monarch, m2k)
    nike_menu.add(back)

    return nike_menu


def menu_adidas():
    adidas_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum 84 low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    adidas_menu.add(forum, ozweego, boost)
    adidas_menu.add(back)

    return adidas_menu

def menu_reebok():
    reebok_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum 84 low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    reebok_menu.add(forum, ozweego, boost)
    reebok_menu.add(back)

    return reebok_menu

def menu_converse():
    converse_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum 84 low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    converse_menu.add(forum, ozweego, boost)
    converse_menu.add(back)

    return converse_menu


@bot.message_handler(commands=['start'])
def start(message):
    photo = open('photoPrivet.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=main_menu())

    bot.send_message(message.chat.id, '<b>privet</b>',
                     parse_mode='html', reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    # исправляет значок загрузки
    if call.message:
        bot.answer_callback_query(callback_query_id=call.id)

        # Удаление последнего сообщения бота
        if call.data == "cancel":
            keyboard_menu = main_menu()

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text='cancel', parse_mode='html', reply_markup=keyboard_menu)
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text='cancel')

        # Удаление 2х последних сообщений бота
        if call.data == "cancell":
            keyboard_menu = main_menu()

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_message(call.message.chat.id, text='cancel', parse_mode='html', reply_markup=keyboard_menu)

        callback_pages.callback_shoes_pages(call)
        callback_pages.callback_clothes_pages(call)
        callback_pages.callback_accesory_pages(call)

        if call.data == "buy":
            bot.send_message(call.message.chat.id,
                             text='<b>тиньк</b> 12345678\n'
                                  'после оплаты - @asphxxk',
                             parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == '📢Информация':
        # фотка инфы
        info = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancell")
        info.add(cancel)

        photo = open('photoInfo.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)

        # кнопка отмены, чтобы не спамить, удаляет 2 сообщения

        bot.send_message(message.chat.id, text='<b>info</b>',
                         parse_mode='html', reply_markup=info)

    if message.text == '❓Помощь в выборе':
        helping = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancel")
        helping.add(cancel)
        bot.send_message(message.chat.id, text='<i>Помощь в выборе товара -</i>\n'
                                               ' @asphxxk', parse_mode='html', reply_markup=helping)

    if message.text == '📩Отзывы':
        feedback = types.InlineKeyboardMarkup()
        feed = types.InlineKeyboardButton("Отзывы", url="https://otzovik.com/lastreviews")
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancel")
        feedback.add(feed)
        feedback.add(cancel)
        bot.send_message(message.chat.id, text='здесь вы можете ознакомиться с отзывами',
                         parse_mode='html', reply_markup=feedback)

    if message.text == '🛍️Каталог':
        # категории в каталоге в меню клавиатуры, прикреплены к фото
        photo = open('photoKatalog.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=katalog_menu())

        bot.send_message(message.chat.id, text='Каталог товаров',
                         parse_mode='html')

    if message.text == '🔙Назад в главное меню':
        bot.send_message(message.chat.id, text='back',
                         parse_mode='html', reply_markup=main_menu())

    if message.text == '🔙Назад к категориям':
        bot.send_message(message.chat.id, text='back',
                         parse_mode='html', reply_markup=katalog_menu())

    if message.text == '👟Nike':
        photo = open('pages/nike/nike.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_nike())

    if message.text == 'Adidas':
        photo = open('pages/adidas/adidas.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_adidas())

    if message.text == 'Reebok👟':
        photo = open('pages/reebok/reebok.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_reebok())

    if message.text =='👟Converse👟':
        photo = open('pages/converse', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_converse())

    if message.text == 'Air Force 1 low':
        text_pages.text_nike_force_pages(message)

bot.polling(none_stop=True)
