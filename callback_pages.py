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



class Crocs:
    def crocs_pages(call):
        callback_pages(call, 'crocs', 'crocs', data.Crocs.crocs_price, data.Crocs.crocs_name)




class Nike:
    def force_pages(call):
        callback_pages(call, 'nike', 'force', data.Nike.force_price, data.Nike.force_name)

    def dunk_high_pages(call):
        callback_pages(call, 'nike', 'dunkHigh', data.Nike.dunk_high_price, data.Nike.dunk_high_name)

    def dunk_low_pages(call):
        callback_pages(call, 'nike', 'dunkLow', data.Nike.dunk_low_price, data.Nike.dunk_low_name)

    def monarch_pages(call):
        callback_pages(call, 'nike', 'monarch', data.Nike.monarch_price, data.Nike.monarch_name)

    def m2k_pages(call):
        callback_pages(call, 'nike', 'm2k', data.Nike.m2k_price, data.Nike.m2k_name)

    def plus_pages(call):
        callback_pages(call, 'nike', 'plus', data.Nike.plus_price, data.Nike.plus_name)

    def vapormax_pages(call):
        callback_pages(call, 'nike', 'vapormax', data.Nike.vapormax_price, data.Nike.vapormax_name)

    def air97_pages(call):
        callback_pages(call, 'nike', 'air97', data.Nike.air97_price, data.Nike.air97_name)

    def air95_pages(call):
        callback_pages(call, 'nike', 'air95', data.Nike.air95_price, data.Nike.air95_name)

    def air720_pages(call):
        callback_pages(call, 'nike', 'air720', data.Nike.air720_price, data.Nike.air720_name)


class Adidas:
    def forum_low_pages(call):
        callback_pages(call, 'adidas', 'forumLow', data.Adidas.forum_low_price, data.Adidas.forum_low_name)

    def ozweego_pages(call):
        callback_pages(call, 'adidas', 'ozweego', data.Adidas.ozweego_price, data.Adidas.ozweego_name)

    def yeezy_boost_350_pages(call):
        callback_pages(call, 'adidas', 'yeezyBoost350', data.Adidas.yeezy_boost_350_price,
                       data.Adidas.yeezy_boost_350_name)

    def ozelia_pages(call):
        callback_pages(call, 'adidas', 'ozelia', data.Adidas.ozelia_price, data.Adidas.ozelia_name)

    def niteball_pages(call):
        callback_pages(call, 'adidas', 'niteball', data.Adidas.niteball_price, data.Adidas.niteball_name)

    def falcon_pages(call):
        callback_pages(call, 'adidas', 'falcon', data.Adidas.falcon_price, data.Adidas.falcon_name)

    def superstar_pages(call):
        callback_pages(call, 'adidas', 'superstar', data.Adidas.superstar_price, data.Adidas.superstar_name)

    def stan_smith_pages(call):
        callback_pages(call, 'adidas', 'stanSmith', data.Adidas.stan_smith_price, data.Adidas.stan_smith_name)

    def supercourt_pages(call):
        callback_pages(call, 'adidas', 'supercourt', data.Adidas.supercourt_price, data.Adidas.supercourt_name)

    def terrex_pages(call):
        callback_pages(call, 'adidas', 'terrex', data.Adidas.terrex_price, data.Adidas.terrex_name)



class Reebok:
    def dmx_1200_pages(call):
        callback_pages(call, 'reebok', 'dmx1200', data.Reebok.dmx_1200_price, data.Reebok.dmx_1200_name)

    def instapump_fury_pages(call):
        callback_pages(call, 'reebok', 'instapumpFury', data.Reebok.instapump_fury_price,
                       data.Reebok.instapump_fury_name)

    def fluffipuff_pages(call):
        callback_pages(call, 'reebok', 'fluffipuff', data.Reebok.fluffipuff_price, data.Reebok.fluffipuff_name)

    def dmx_1000_pages(call):
        callback_pages(call, 'reebok', 'dmx1000', data.Reebok.dmx_1000_price, data.Reebok.dmx_1000_name)

    def classic_legacy_pages(call):
        callback_pages(call, 'reebok', 'classicLegacy', data.Reebok.classic_legacy_price,
                       data.Reebok.classic_legacy_name)

    def daytona_dmx_pages(call):
        callback_pages(call, 'reebok', 'daytonaDmx', data.Reebok.daytona_dmx_price, data.Reebok.daytona_dmx_name)



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



def callback_converse_aeon_active_pages(call):
    callback_pages(call, 'converse', 'aeonActiveCX', data.converse_aeon_active_cx_price,
                                                     data.converse_aeon_active_cx_name)

def callback_converse_all_star_1970_pages(call):
    callback_pages(call, 'converse', 'allStar1970', data.converse_all_star_1970_price, data.converse_all_star_1970_name)

def callback_converse_all_star_bb_prototype_pages(call):
    callback_pages(call, 'converse', 'allStarBBPrototype', data.converse_all_star_bb_prototype_price,
                                                           data.converse_all_star_bb_prototype_name)

def callback_converse_one_star_pages(call):
    callback_pages(call, 'converse', 'oneStar', data.converse_one_star_price, data.converse_one_star_name)

def callback_converse_pro_blaze_strap_pages(call):
    callback_pages(call, 'converse', 'proBlazeStrap', data.converse_pro_blaze_strap_price,
                                                      data.converse_pro_blaze_strap_name)



def callback_nb_530_pages(call):
    callback_pages(call, 'new balance', 'nb530', data.nb_530_price, data.nb_530_name)

def callback_nb_725_pages(call):
    callback_pages(call, 'new balance', 'nb725', data.nb_725_price, data.nb_725_name)

def callback_nb_827_pages(call):
    callback_pages(call, 'new balance', 'nb827', data.nb_827_price, data.nb_827_name)

def callback_nb_452_pages(call):
    callback_pages(call, 'new balance', 'nb452', data.nb_452_price, data.nb_452_name)

def callback_nb_327_pages(call):
    callback_pages(call, 'new balance', 'nb327', data.nb_327_price, data.nb_327_name)

