from telebot import types


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
    jordan = types.KeyboardButton(text='👟Jordan')
    converse = types.KeyboardButton(text='Converse')
    nb = types.KeyboardButton(text='New Balance👟')

    back = types.KeyboardButton(text='🔙Назад в главное меню')

    katalog_menu.add(nike, adidas, reebok)
    katalog_menu.add(jordan, converse, nb)
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

def menu_jordan():
    jordan_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum 84 low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    jordan_menu.add(forum, ozweego, boost)
    jordan_menu.add(back)

    return jordan_menu

def menu_nb():
    nb_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum 84 low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    nb_menu.add(forum, ozweego, boost)
    nb_menu.add(back)

    return nb_menu