import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

from config import send_error

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
                       InlineKeyboardButton(text=f'▶️',
                                            callback_data=json.dumps(j_data_up)))

        # markup для второй страницы
        elif page == count:

            markup.add(InlineKeyboardButton(text=f'◀️',
                                            callback_data=json.dumps(j_data_down)),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:

            markup.add(InlineKeyboardButton(text=f'◀️',
                                            callback_data=json.dumps(j_data_down)),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'▶️',
                                            callback_data=json.dumps(j_data_up)))

        markup.add(
            InlineKeyboardButton(text=f'{data_price[page - 1]}руб - Купить', callback_data='buy'))
        # bot.edit_message_text(f' {data.shoes_name_pages[page-1]} ', reply_markup=markup, chat_id=call.message.chat.id,
        #                      message_id=call.message.message_id)


        bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open(f'pages/{brand}/{callback_string}/{page}.jfif', 'rb'),
                                                                  caption=f'{data_name[page - 1]}'),
                                   reply_markup=markup,
                                   chat_id=call.message.chat.id, message_id=call.message.message_id)



def callback_crocs_pages(call):
    callback_pages(call, 'crocs', 'crocs', data.crocs_price_pages, data.crocs_name_pages)



def callback_nike_force_pages(call):
    callback_pages(call, 'nike', 'force', data.nike_force_price_pages, data.nike_force_name_pages)

def callback_nike_dunk_high_pages(call):
    callback_pages(call, 'nike', 'dunkHigh', data.nike_dunk_high_price_pages, data.nike_dunk_high_name_pages)

def callback_nike_dunk_low_pages(call):
    callback_pages(call, 'nike', 'dunkLow', data.nike_dunk_low_price_pages, data.nike_dunk_low_name_pages)

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



def callback_adidas_forum_low_pages(call):
    callback_pages(call, 'adidas', 'forumLow', data.adidas_forum_low_price, data.adidas_forum_low_name)

def callback_adidas_ozweego_pages(call):
    callback_pages(call, 'adidas', 'ozweego', data.adidas_ozweego_price, data.adidas_ozweego_name)

def callback_adidas_yeezy_boost_350_pages(call):
    callback_pages(call, 'adidas', 'yeezyBoost350', data.adidas_yeezy_boost_350_price,
                                                      data.adidas_yeezy_boost_350_name)

def callback_adidas_ozelia_pages(call):
    callback_pages(call, 'adidas', 'ozelia', data.adidas_ozelia_price, data.adidas_ozelia_name)

def callback_adidas_niteball_pages(call):
    callback_pages(call, 'adidas', 'niteball', data.adidas_niteball_price, data.adidas_niteball_name)

def callback_adidas_falcon_pages(call):
    callback_pages(call, 'adidas', 'falcon', data.adidas_falcon_price, data.adidas_falcon_name)

def callback_adidas_superstar_pages(call):
    callback_pages(call, 'adidas', 'superstar', data.adidas_superstar_price, data.adidas_superstar_name)

def callback_adidas_stan_smith_pages(call):
    callback_pages(call, 'adidas', 'stanSmith', data.adidas_stan_smith_price, data.adidas_stan_smith_name)

def callback_adidas_supercourt_pages(call):
    callback_pages(call, 'adidas', 'supercourt', data.adidas_supercourt_price, data.adidas_supercourt_name)

def callback_adidas_terrex_pages(call):
    callback_pages(call, 'adidas', 'terrex', data.adidas_terrex_price, data.adidas_terrex_name)



def callback_reebok_dmx_1200_pages(call):
    callback_pages(call, 'reebok', 'dmx1200', data.reebok_dmx_1200_price, data.reebok_dmx_1200_name)

def callback_reebok_instapump_fury_pages(call):
    callback_pages(call, 'reebok', 'instapumpFury', data.reebok_instapump_fury_price, data.reebok_instapump_fury_name)

def callback_reebok_fluffipuff_pages(call):
    callback_pages(call, 'reebok', 'fluffipuff', data.reebok_fluffipuff_price, data.reebok_fluffipuff_name)

def callback_reebok_dmx_1000_pages(call):
    callback_pages(call, 'reebok', 'dmx1000', data.reebok_dmx_1000_price, data.reebok_dmx_1000_name)

def callback_reebok_classic_legacy_pages(call):
    callback_pages(call, 'reebok', 'classicLegacy', data.reebok_classic_legacy_price, data.reebok_classic_legacy_name)

def callback_reebok_daytona_dmx_pages(call):
    callback_pages(call, 'reebok', 'daytonaDmx', data.reebok_daytona_dmx_price, data.reebok_daytona_dmx_name)



def callback_jordan_air_1_high_pages(call):
    callback_pages(call, 'jordan', 'air1high', data.jordan_1_high_price, data.jordan_1_high_name)

def callback_jordan_air_1_mid_pages(call):
    callback_pages(call, 'jordan', 'air1mid', data.jordan_1_mid_price, data.jordan_1_mid_name)

def callback_jordan_air_1_low_pages(call):
    callback_pages(call, 'jordan', 'air1low', data.jordan_1_low_price, data.jordan_1_low_name)

def callback_jordan_3_retro_pages(call):
    callback_pages(call, 'jordan', '3retro', data.jordan_3_retro_price, data.jordan_3_retro_name)

def callback_jordan_4_retro_pages(call):
    callback_pages(call, 'jordan', '4retro', data.jordan_4_retro_price, data.jordan_4_retro_name)

def callback_jordan_5_retro_pages(call):
    callback_pages(call, 'jordan', '5retro', data.jordan_5_retro_price, data.jordan_5_retro_name)

def callback_jordan_ultra_fly_2_low_pages(call):
    callback_pages(call, 'jordan', 'ultraFly2low', data.jordan_ultrafly_2_low_price,
                                                      data.jordan_ultrafly_2_low_name)

def callback_jordan_legacy_312_pages(call):
    callback_pages(call, 'jordan', 'legacy312', data.jordan_legacy_312_price, data.jordan_legacy_312_name)

