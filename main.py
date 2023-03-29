import telebot
from telebot import types

from menues import main_menu, katalog_menu, menu_nike, menu_adidas, menu_reebok
from menues import menu_converse, menu_jordan, menu_nb
from config import BOT_TOKEN, team_id, error_message, admin_id, send_error

import random

import callback_pages
import text_pages

bot = telebot.TeleBot(BOT_TOKEN)

def send_to_adm_chat_buy(call):
    id_buying = random.randint(10000000, 99999999)
    try:
        bot.forward_message(chat_id=team_id, from_chat_id=call.message.chat.id,
                            message_id=call.message.id)

        bot.send_message(chat_id=team_id,
                         text=f'Уникальный id <b>{id_buying}</b>.\n'
                              f'Клиент - @{call.from_user.username}',
                         parse_mode='html')

        bot.send_message(call.message.chat.id,
                         text=f'Заявка на заказ успешно оформлена!\n'
                              f'Уникальный id <b>{id_buying}</b>. С Вами свяжутся в ближайшее время\n'
                              '\n'
                              'Если у Вас возникли проблемы, обратитесь в тех. поддержку',
                         parse_mode='html')

    except:
        send_error(call, 'Возникла ошибка в создании заказа')


# Запись информации юзера в файл
def file_user_info(username, uid):
    file = open('info_users/users_repeation.txt', 'a', encoding="utf-8")
    file.write(f"Username: {username}, id: {uid}\n")

    file.close()


def delete_repeation():
    outputFile = open('info_users/users.txt', "w", encoding="utf-8")

    inputFile = open('info_users/users_repeation.txt', "r", encoding="utf-8")

    lines_seen_so_far = set()

    for line in inputFile:

        if line not in lines_seen_so_far:
            outputFile.write(line)

            lines_seen_so_far.add(line)

    inputFile.close()
    outputFile.close()


@bot.message_handler(commands=['start'])
def start(message):
    # Запись инфы о пользователях бота
    file_user_info(message.from_user.username, message.from_user.id)
    delete_repeation()

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

        callback_pages.Crocs.crocs_pages(call)

        callback_pages.Nike.force_pages(call)
        callback_pages.Nike.dunk_high_pages(call)
        callback_pages.Nike.dunk_low_pages(call)
        callback_pages.Nike.monarch_pages(call)
        callback_pages.Nike.m2k_pages(call)
        callback_pages.Nike.plus_pages(call)
        callback_pages.Nike.vapormax_pages(call)
        callback_pages.Nike.air97_pages(call)
        callback_pages.Nike.air95_pages(call)
        callback_pages.Nike.air720_pages(call)

        callback_pages.Adidas.forum_low_pages(call)
        callback_pages.Adidas.ozweego_pages(call)
        callback_pages.Adidas.yeezy_boost_350_pages(call)
        callback_pages.Adidas.ozelia_pages(call)
        callback_pages.Adidas.niteball_pages(call)
        callback_pages.Adidas.falcon_pages(call)
        callback_pages.Adidas.superstar_pages(call)
        callback_pages.Adidas.stan_smith_pages(call)
        callback_pages.Adidas.supercourt_pages(call)
        callback_pages.Adidas.terrex_pages(call)

        callback_pages.Reebok.dmx_1200_pages(call)
        callback_pages.Reebok.instapump_fury_pages(call)
        callback_pages.Reebok.question_low_pages(call)
        callback_pages.Reebok.fluffipuff_pages(call)
        callback_pages.Reebok.dmx_1000_pages(call)
        callback_pages.Reebok.classic_legacy_pages(call)
        callback_pages.Reebok.daytona_dmx_pages(call)

        callback_pages.Jordan.air_1_high_pages(call)
        callback_pages.Jordan.air_1_mid_pages(call)
        callback_pages.Jordan.air_1_low_pages(call)
        callback_pages.Jordan.retro_3_pages(call)
        callback_pages.Jordan.retro_4_pages(call)
        callback_pages.Jordan.retro_5_pages(call)
        callback_pages.Jordan.ultra_fly_2_low_pages(call)
        callback_pages.Jordan.legacy_312_pages(call)

        callback_pages.Converse.aeon_active_pages(call)
        callback_pages.Converse.aeon_active_pages(call)
        callback_pages.Converse.all_star_bb_prototype_pages(call)
        callback_pages.Converse.one_star_pages(call)
        callback_pages.Converse.pro_blaze_strap_pages(call)

        callback_pages.NewBalance.nb_530_pages(call)
        callback_pages.NewBalance.nb_725_pages(call)
        callback_pages.NewBalance.nb_827_pages(call)
        callback_pages.NewBalance.nb_452_pages(call)
        callback_pages.NewBalance.nb_327_pages(call)

        if call.data == "buy":
            send_to_adm_chat_buy(call)


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
                                               '@asphxxk', parse_mode='html', reply_markup=helping)

    if message.text == '📩Ваши предложения':
        bot.send_message(message.chat.id, text='<b>Здесь Вы можете оставить ВСЕ свои пожелания по улучшению '
                                               'качества работы\n'
                                               'Это могут быть варианты улучшения магазина, '
                                               'добавление новых товаров или устранение ошибок\n'
                                               '\n'
                                               'Нам важно Ваше мнение!\n'
                                               '\n'
                                               'https://t.me/+3D4fwse-TApjMDIy</b>', parse_mode='html')

    if message.text == '🔗Наша группа':
        bot.send_message(message.chat.id, text='<b>Подписывайся на наш канал!!!\n'
                                               '\n'
                                               'Тут мы публикуем новости и красивые видео с обзорами товаров\n'
                                               '\n'
                                               'https://t.me/plusrepeat</b>',
                         parse_mode='html')

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
        # bot.delete_message(message.chat.id, message.message_id - 1)
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

    if message.text == '👟Jordan':
        photo = open('pages/Jordan/jordan.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_jordan())

    if message.text == 'Converse':
        photo = open('pages/Converse/converse.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_converse())

    if message.text == 'New Balance👟':
        photo = open('pages/New balance/new balance.png', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=menu_nb())



    if message.text == '🐤Crocs':
        text_pages.Crocs.crocs_pages(message)



    if message.text == 'Air Force 1 Low':
        text_pages.Nike.force_pages(message)

    if message.text == 'Dunk High':
        text_pages.Nike.dunk_high_pages(message)

    if message.text == 'Dunk Low':
        text_pages.Nike.dunk_low_pages(message)

    if message.text == 'Air Monarch':
        text_pages.Nike.monarch_pages(message)

    if message.text == 'Air M2K Tekno':
        text_pages.Nike.m2k_pages(message)

    if message.text == 'Air Max Plus':
        text_pages.Nike.plus_pages(message)

    if message.text == 'Air Vapormax':
        text_pages.Nike.vapormax_pages(message)

    if message.text == 'Air Vapormax':
        text_pages.Nike.vapormax_pages(message)

    if message.text == 'Air Max 97':
        text_pages.Nike.air97_pages(message)

    if message.text == 'Air Max 95':
        text_pages.Nike.air95_pages(message)

    if message.text == 'Air Max 720':
        text_pages.Nike.air720_pages(message)



    if message.text == 'Forum Low':
        text_pages.Adidas.forum_low_pages(message)

    if message.text == 'Ozweego':
        text_pages.Adidas.ozweego_pages(message)

    if message.text == 'Yeezy Boost 350':
        text_pages.Adidas.yeezy_boost_350_pages(message)

    if message.text == 'Ozelia':
        text_pages.Adidas.ozelia_pages(message)

    if message.text == 'Niteball':
        text_pages.Adidas.niteball_pages(message)

    if message.text == 'Falcon':
        text_pages.Adidas.falcon_pages(message)

    if message.text == 'Superstar':
        text_pages.Adidas.superstar_pages(message)

    if message.text == 'Stan Smith':
        text_pages.Adidas.stan_smith_pages(message)

    if message.text == 'Supercourt':
        text_pages.Adidas.supercourt_pages(message)

    if message.text == 'Terrex':
        text_pages.Adidas.terrex_pages(message)



    if message.text == 'DMX Series 1200':
        text_pages.Reebok.dmx_1200_pages(message)

    if message.text == 'Instapump Fury':
        text_pages.Reebok.instapump_fury_pages(message)

    if message.text == 'Question Low':
        text_pages.Reebok.question_low_pages(message)

    if message.text == 'Fluffipuff':
        text_pages.Reebok.fluffipuff_pages(message)

    if message.text == 'DMX Series 1000':
        text_pages.Reebok.dmx_1000_pages(message)

    if message.text == 'Classic Legacy':
        text_pages.Reebok.classic_legacy_pages(message)

    if message.text == 'Daytona DMX':
        text_pages.Reebok.daytona_dmx_pages(message)



    if message.text == 'Air Jordan 1 High':
        text_pages.Jordan.air_1_high_pages(message)

    if message.text == 'Air Jordan 1 Mid':
        text_pages.Jordan.air_1_mid_pages(message)

    if message.text == 'Air Jordan 1 Low':
        text_pages.Jordan.air_1_low_pages(message)

    if message.text == 'Jordan 3 Retro':
        text_pages.Jordan.retro_3_pages(message)

    if message.text == 'Jordan 4 Retro':
        text_pages.Jordan.retro_4_pages(message)

    if message.text == 'Jordan 5 Retro':
        text_pages.Jordan.retro_5_pages(message)

    if message.text == 'Ultra Fly 2 Low':
        text_pages.Jordan.ultra_fly_2_low_pages(message)

    if message.text == 'Legacy 312':
        text_pages.Jordan.legacy_312_pages(message)



    if message.text == 'Aeon Active CX':
        text_pages.Converse.aeon_active_pages(message)

    if message.text == 'All Star 1970s':
        text_pages.Converse.all_star_1970_pages(message)

    if message.text == 'All Star BB Prototype':
        text_pages.Converse.all_star_bb_prototype_pages(message)

    if message.text == 'One Star':
        text_pages.Converse.one_star_pages(message)

    if message.text == 'Pro Blaze Strap':
        text_pages.Converse.pro_blaze_strap_pages(message)



    if message.text == 'NB 530':
        text_pages.NewBalance.nb_530_pages(message)

    if message.text == 'NB 725':
        text_pages.NewBalance.nb_725_pages(message)

    if message.text == 'NB 827':
        text_pages.NewBalance.nb_827_pages(message)

    if message.text == 'NB 452':
        text_pages.NewBalance.nb_827_pages(message)

    if message.text == 'NB 327':
        text_pages.NewBalance.nb_827_pages(message)


bot.polling(none_stop=True)
