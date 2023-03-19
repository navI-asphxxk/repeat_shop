import telebot
from telebot import types
from menues import main_menu, katalog_menu, menu_nike, menu_adidas, menu_reebok
from menues import menu_converse, menu_jordan, menu_nb
from config import BOT_TOKEN, team_id, error_message, admin_id

import random

import callback_pages
import text_pages

bot = telebot.TeleBot(BOT_TOKEN)

#отправка ошибки в чат и админам
def send_error(call, adm_mess):
    bot.send_message(call.message.chat.id, text=error_message)

    bot.send_message(chat_id=admin_id, text=adm_mess)

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
def file_user_info(username, uid, name):
    file = open('info_users/users_repeation.txt', 'a')
    file.write(f"Username: {username}, id: {uid}, name: {name}\n")

    file.close()


def delete_repeation():
    outputFile = open('info_users/users.txt', "w")

    inputFile = open('info_users/users_repeation.txt', "r")

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
    file_user_info(message.from_user.username, message.from_user.id, message.from_user.first_name)
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

        callback_pages.callback_crocs_pages(call)

        callback_pages.callback_nike_force_pages(call)
        callback_pages.callback_nike_dunk_high_pages(call)
        callback_pages.callback_nike_dunk_low_pages(call)
        callback_pages.callback_nike_monarch_pages(call)
        callback_pages.callback_nike_m2k_pages(call)
        callback_pages.callback_nike_plus_pages(call)
        callback_pages.callback_nike_vapormax_pages(call)
        callback_pages.callback_nike_air97_pages(call)
        callback_pages.callback_nike_air95_pages(call)
        callback_pages.callback_nike_air720_pages(call)

        callback_pages.callback_adidas_forum_low_pages(call)
        callback_pages.callback_adidas_ozweego_pages(call)
        callback_pages.callback_adidas_yeezy_boost_350_pages(call)
        callback_pages.callback_adidas_ozelia_pages(call)
        callback_pages.callback_adidas_niteball_pages(call)
        callback_pages.callback_adidas_falcon_pages(call)
        callback_pages.callback_adidas_superstar_pages(call)
        callback_pages.callback_adidas_stan_smith_pages(call)
        callback_pages.callback_adidas_supercourt_pages(call)
        callback_pages.callback_adidas_terrex_pages(call)

        callback_pages.callback_reebok_dmx_1200_pages(call)
        callback_pages.callback_reebok_instapump_fury_pages(call)
        callback_pages.callback_reebok_fluffipuff_pages(call)
        callback_pages.callback_reebok_dmx_1000_pages(call)
        callback_pages.callback_reebok_classic_legacy_pages(call)
        callback_pages.callback_reebok_daytona_dmx_pages(call)


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
        text_pages.text_crocs_pages(message)



    if message.text == 'Air Force 1 Low':
        text_pages.text_nike_force_pages(message)

    if message.text == 'Dunk High':
        text_pages.text_nike_dunk_high_pages(message)

    if message.text == 'Dunk Low':
        text_pages.text_nike_dunk_low_pages(message)

    if message.text == 'Air Monarch':
        text_pages.text_nike_monarch_pages(message)

    if message.text == 'Air M2K Tekno':
        text_pages.text_nike_m2k_pages(message)

    if message.text == 'Air Max Plus':
        text_pages.text_nike_plus_pages(message)

    if message.text == 'Air Vapormax':
        text_pages.text_nike_vapormax_pages(message)

    if message.text == 'Air Vapormax':
        text_pages.text_nike_vapormax_pages(message)

    if message.text == 'Air Max 97':
        text_pages.text_nike_air97_pages(message)

    if message.text == 'Air Max 95':
        text_pages.text_nike_air95_pages(message)

    if message.text == 'Air Max 720':
        text_pages.text_nike_air720_pages(message)



    if message.text == 'Forum Low':
        text_pages.text_adidas_forum_low_pages(message)

    if message.text == 'Ozweego':
        text_pages.text_adidas_ozweego_pages(message)

    if message.text == 'Yeezy Boost 350':
        text_pages.text_adidas_yeezy_boost_350_pages(message)

    if message.text == 'Ozelia':
        text_pages.text_adidas_ozelia_pages(message)

    if message.text == 'Niteball':
        text_pages.text_adidas_niteball_pages(message)

    if message.text == 'Falcon':
        text_pages.text_adidas_falcon_pages(message)

    if message.text == 'Superstar':
        text_pages.text_adidas_superstar_pages(message)

    if message.text == 'Stan Smith':
        text_pages.text_adidas_stan_smith_pages(message)

    if message.text == 'Supercourt':
        text_pages.text_adidas_supercourt_pages(message)

    if message.text == 'Terrex':
        text_pages.text_adidas_terrex_pages(message)



    if message.text == 'DMX Series 1200':
        text_pages.text_reebok_dmx_1200_pages(message)

    if message.text == 'Instapump Fury':
        text_pages.text_reebok_instapump_fury_pages(message)

    if message.text == 'Fluffipuff':
        text_pages.text_reebok_fluffipuff_pages(message)

    if message.text == 'DMX Series 1000':
        text_pages.text_reebok_dmx_1000_pages(message)

    if message.text == 'Classic Legacy':
        text_pages.text_reebok_classic_legacy_pages(message)

    if message.text == 'Daytona DMX':
        text_pages.text_reebok_daytona_dmx_pages(message)


bot.polling(none_stop=True)
