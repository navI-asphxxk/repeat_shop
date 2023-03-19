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
               InlineKeyboardButton(text=f'▶️',
                                    callback_data=json.dumps(j_data_up)))
    markup.add(InlineKeyboardButton(text=f'{data_price[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/{brand}/{callback_string}/{page}.jpg', 'rb'),
                   caption=f'{data_name[0]}', reply_markup=markup)



def text_crocs_pages(message):
    text_pages(message, 'crocs', 'crocs', data.crocs_price_pages, data.crocs_name_pages)



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

def text_nike_vapormax_pages(message):
    text_pages(message, 'nike', 'vapormax', data.nike_vapormax_price_pages, data.nike_vapormax_name_pages)

def text_nike_air97_pages(message):
    text_pages(message, 'nike', 'vapormax', data.nike_97_price_pages, data.nike_97_name_pages)

def text_nike_air95_pages(message):
    text_pages(message, 'nike', 'air95', data.nike_95_price_pages, data.nike_95_name_pages)

def text_nike_air720_pages(message):
    text_pages(message, 'nike', 'air720', data.nike_720_price_pages, data.nike_720_name_pages)



def text_adidas_forum_low_pages(message):
    text_pages(message, 'adidas', 'forum_low', data.adidas_forum_low_price, data.adidas_forum_low_name)

def text_adidas_ozweego_pages(message):
    text_pages(message, 'adidas', 'ozweego', data.adidas_ozweego_price, data.adidas_ozweego_name)

def text_adidas_yeezy_boost_350_pages(message):
    text_pages(message, 'adidas', 'yeezy_boost_350', data.adidas_yeezy_boost_350_price,
                                                     data.adidas_yeezy_boost_350_name)

def text_adidas_ozelia_pages(message):
    text_pages(message, 'adidas', 'ozelia', data.adidas_ozelia_price, data.adidas_ozelia_name)

def text_adidas_niteball_pages(message):
    text_pages(message, 'adidas', 'niteball', data.adidas_niteball_price, data.adidas_niteball_name)

def text_adidas_falcon_pages(message):
    text_pages(message, 'adidas', 'falcon', data.adidas_falcon_price, data.adidas_falcon_name)

def text_adidas_superstar_pages(message):
    text_pages(message, 'adidas', 'superstar', data.adidas_superstar_price, data.adidas_superstar_name)

def text_adidas_stan_smith_pages(message):
    text_pages(message, 'adidas', 'stan_smith', data.adidas_stan_smith_price, data.adidas_stan_smith_name)

def text_adidas_supercourt_pages(message):
    text_pages(message, 'adidas', 'supercourt', data.adidas_supercourt_price, data.adidas_supercourt_name)

def text_adidas_terrex_pages(message):
    text_pages(message, 'adidas', 'terrex', data.adidas_terrex_price, data.adidas_terrex_name)



def text_reebok_dmx_1200_pages(message):
    text_pages(message, 'reebok', 'dmx_1200', data.reebok_dmx_1200_price, data.reebok_dmx_1200_name)

def text_reebok_instapump_fury_pages(message):
    text_pages(message, 'reebok', 'instapump_fury', data.reebok_instapump_fury_price, data.reebok_instapump_fury_name)

def text_reebok_fluffipuff_pages(message):
    text_pages(message, 'reebok', 'fluffipuff', data.reebok_fluffipuff_price, data.reebok_fluffipuff_name)

def text_reebok_dmx_1000_pages(message):
    text_pages(message, 'reebok', 'dmx_1000', data.reebok_dmx_1000_price, data.reebok_dmx_1000_name)

def text_reebok_classic_legacy_pages(message):
    text_pages(message, 'reebok', 'classic_legacy', data.reebok_classic_legacy_price, data.reebok_classic_legacy_name)

def text_reebok_daytona_dmx_pages(message):
    text_pages(message, 'reebok', 'daytona_dmx', data.reebok_daytona_dmx_price, data.reebok_daytona_dmx_name)



def text_jordan_air_1_high_pages(message):
    text_pages(message, 'jordan', 'air_1_high', data.jordan_1_high_price, data.jordan_1_high_name)

def text_jordan_air_1_mid_pages(message):
    text_pages(message, 'jordan', 'air_1_mid', data.jordan_1_mid_price, data.jordan_1_mid_name)

def text_jordan_air_1_low_pages(message):
    text_pages(message, 'jordan', 'air_1_low', data.jordan_1_low_price, data.jordan_1_low_name)

def text_jordan_3_retro_pages(message):
    text_pages(message, 'jordan', '3_retro', data.jordan_3_retro_price, data.jordan_3_retro_name)

def text_jordan_4_retro_pages(message):
    text_pages(message, 'jordan', '4_retro', data.jordan_4_retro_price, data.jordan_4_retro_name)

def text_jordan_5_retro_pages(message):
    text_pages(message, 'jordan', '5_retro', data.jordan_5_retro_price, data.jordan_5_retro_name)

def text_jordan_ultra_fly_2_low_pages(message):
    text_pages(message, 'jordan', 'ultra_fly_2_low', data.jordan_ultrafly_2_low_price,
                                                      data.jordan_ultrafly_2_low_name)

def text_jordan_legacy_312_pages(message):
    text_pages(message, 'jordan', 'legacy_312', data.jordan_legacy_312_price, data.jordan_legacy_312_name)