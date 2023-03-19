import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

import data
import json

bot = telebot.TeleBot(BOT_TOKEN)

def callback_pages(call, brand, callback_string, data_price, data_name):
    req = call.data.split('_')
    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as ex:
            print(ex)
    # Обработка кнопок - вперед и назад
    elif callback_string in req[0]:
        # Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']

        # Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))

        # callback в формате json
        j_data_up = {"method": callback_string,
                     "NumberPage": page + 1,
                     "CountPage": count
                     }
        j_data_down = {"method": callback_string,
                       "NumberPage": page - 1,
                       "CountPage": count
                       }

        # markup для первой страницы
        if page == 1:

            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data=json.dumps(j_data_up)))

        # markup для второй страницы
        elif page == count:

            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data=json.dumps(j_data_down)),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:

            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data=json.dumps(j_data_down)),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data=json.dumps(j_data_up)))

        markup.add(
            InlineKeyboardButton(text=f'{data_price[page - 1]}руб - Купить', callback_data='buy'))
        # bot.edit_message_text(f' {data.shoes_name_pages[page-1]} ', reply_markup=markup, chat_id=call.message.chat.id,
        #                      message_id=call.message.message_id)

        try:
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open(f'pages/{brand}/{callback_string}/{page}.jpg', 'rb'),
                                                                  caption=f'{data_name[page - 1]}'),
                                   reply_markup=markup,
                                   chat_id=call.message.chat.id, message_id=call.message.message_id)
        except Exception as ex:
            print(ex)


def callback_crocs_pages(call):
    callback_pages(call, 'crocs', 'crocs', data.crocs_price_pages, data.crocs_name_pages)

def callback_nike_force_pages(call):
    callback_pages(call, 'nike', 'force', data.nike_force_price_pages, data.nike_force_name_pages)

def callback_nike_dunk_high_pages(call):
    callback_pages(call, 'nike', 'dunk_high', data.nike_dunk_high_price_pages, data.nike_dunk_high_name_pages)

def callback_nike_dunk_low_pages(call):
    callback_pages(call, 'nike', 'dunk_low', data.nike_dunk_low_price_pages, data.nike_dunk_low_name_pages)

def callback_nike_monarch_pages(call):
    callback_pages(call, 'nike', 'monarch', data.nike_monarch_price_pages, data.nike_monarch_name_pages)

def callback_nike_m2k_pages(call):
    callback_pages(call, 'nike', 'm2k', data.nike_m2k_price_pages, data.nike_m2k_name_pages)

def callback_nike_plus_pages(call):
    callback_pages(call, 'nike', 'plus', data.nike_plus_price_pages, data.nike_plus_name_pages)

def callback_nike_vapormax_pages(call):
    callback_pages(call, 'nike', 'vapormax', data.nike_vapormax_price_pages, data.nike_vapormax_name_pages)

def callback_nike_air97_pages(call):
    callback_pages(call, 'nike', 'air97', data.nike_97_price_pages, data.nike_97_name_pages)

def callback_nike_air95_pages(call):
    callback_pages(call, 'nike', 'air95', data.nike_95_price_pages, data.nike_95_name_pages)

def callback_nike_air720_pages(call):
    callback_pages(call, 'nike', 'air720', data.nike_720_price_pages, data.nike_720_name_pages)


