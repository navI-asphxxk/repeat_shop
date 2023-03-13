import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import data
import json

bot = telebot.TeleBot('5873814230:AAGfDLmGCzWNFexqkAmPNm4pvEIv2GTYy9M')


def callback_nike_force_pages(call):
    req = call.data.split('_')
    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as ex:
            print(ex)
    # Обработка кнопок - вперед и назад
    #callback
    elif 'force' in req[0]:
        # Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
        # Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        # markup для первой страницы
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',      # callback
                                            callback_data="{\"method\":\"force\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        # markup для второй страницы
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',      # callback
                                            callback_data="{\"method\":\"force\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',      # callback
                                            callback_data="{\"method\":\"force\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',     # callback
                                            callback_data="{\"method\":\"force\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        markup.add(                    # data цены
            InlineKeyboardButton(text=f'{data.nike_force_price_pages[page - 1]}руб - Купить', callback_data='buy'))
        # bot.edit_message_text(f' {data.shoes_name_pages[page-1]} ', reply_markup=markup, chat_id=call.message.chat.id,
        #                      message_id=call.message.message_id)

        try:
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',          # папка = callback
                                                                  media=open(f'pages/nike/force/{page}.jpg', 'rb'),
                                                                  caption=f'{data.nike_force_name_pages[page - 1]}'),
                                   reply_markup=markup,
                                   chat_id=call.message.chat.id, message_id=call.message.message_id)
        except Exception as ex:
            print(ex)



def callback_nike_monarch_pages(call):
    req = call.data.split('_')
    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as ex:
            print(ex)
    # Обработка кнопок - вперед и назад
    elif 'monarch' in req[0]:
        # Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
        # Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        # markup для первой страницы
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"monarch\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        # markup для второй страницы
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"monarch\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"monarch\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"monarch\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        markup.add(
            InlineKeyboardButton(text=f'{data.nike_monarch_price_pages[page - 1]}руб - Купить', callback_data='buy'))

        try:
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open(f'pages/nike/monarch/{page}.jpg', 'rb'),
                                                                  caption=f'{data.nike_monarch_name_pages[page - 1]}'),
                                   reply_markup=markup,
                                   chat_id=call.message.chat.id, message_id=call.message.message_id)
        except Exception as ex:
            print(ex)



def callback_nike_m2k_pages(call):
    req = call.data.split('_')
    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as ex:
            print(ex)
    # Обработка кнопок - вперед и назад
    elif 'm2k' in req[0]:
        # Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
        # Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        # markup для первой страницы
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"m2k\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        # markup для второй страницы
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"m2k\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"m2k\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"m2k\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        markup.add(
            InlineKeyboardButton(text=f'{data.nike_m2k_price_pages[page - 1]}руб - Купить', callback_data='buy'))

        try:
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open(f'pages/nike/m2k/{page}.jpg', 'rb'),
                                                                  caption=f'{data.nike_m2k_name_pages[page - 1]}'),
                                   reply_markup=markup,
                                   chat_id=call.message.chat.id, message_id=call.message.message_id)
        except Exception as ex:
            print(ex)

