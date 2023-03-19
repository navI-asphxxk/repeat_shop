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
    crocs = types.KeyboardButton(text='🐤Crocs')

    back = types.KeyboardButton(text='🔙Назад в главное меню')

    katalog_menu.add(nike, adidas, reebok)
    katalog_menu.add(jordan, converse, nb)
    katalog_menu.add(crocs)
    katalog_menu.add(back)

    return katalog_menu


def menu_nike():
    nike_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    force = types.KeyboardButton(text='Air Force 1 Low')
    dunk_h = types.KeyboardButton(text='Dunk High')
    dunk_l = types.KeyboardButton(text='Dunk Low')

    monarch = types.KeyboardButton(text='Air Monarch')
    m2k = types.KeyboardButton(text='Air M2K Tekno')
    tn = types.KeyboardButton(text='Air Max Plus')

    vap = types.KeyboardButton(text='Air Vapormax')
    m97 = types.KeyboardButton(text='Air Max 97')
    m95 = types.KeyboardButton(text='Air Max 95')
    m720 = types.KeyboardButton(text='Air Max 720')

    back = types.KeyboardButton(text='🔙Назад к категориям')

    nike_menu.add(force, dunk_h, dunk_l)
    nike_menu.add(monarch, m2k, tn)
    nike_menu.add(vap, m97, m95, m720)
    nike_menu.add(back)

    return nike_menu


def menu_adidas():
    adidas_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    forum = types.KeyboardButton(text='Forum Low')
    ozweego = types.KeyboardButton(text='Ozweego')
    boost = types.KeyboardButton(text='Yeezy Boost 350')

    ozelia = types.KeyboardButton(text='Ozelia')
    niteball = types.KeyboardButton(text='Niteball')
    falcon = types.KeyboardButton(text='Falcon')

    supstar = types.KeyboardButton(text='Superstar')
    stansmith = types.KeyboardButton(text='Stan Smith')
    supercourt = types.KeyboardButton(text='Supercourt')

    terrex = types.KeyboardButton(text='Terrex')

    back = types.KeyboardButton(text='🔙Назад к категориям')

    adidas_menu.add(forum, ozweego, boost)
    adidas_menu.add(ozelia, niteball, falcon)
    adidas_menu.add(supstar, stansmith, supercourt)
    adidas_menu.add(terrex)
    adidas_menu.add(back)

    return adidas_menu


def menu_reebok():
    reebok_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    r1 = types.KeyboardButton(text='DMX Series 1200')
    r2 = types.KeyboardButton(text='DMX Series 1000')
    r3 = types.KeyboardButton(text='Fluffipuff')
    r4 = types.KeyboardButton(text='Classic Legacy')
    r5 = types.KeyboardButton(text='Instapump Fury')
    r6 = types.KeyboardButton(text='Daytona DMX')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    reebok_menu.add(r1, r2, r3)
    reebok_menu.add(r4, r5, r6)
    reebok_menu.add(back)

    return reebok_menu


def menu_converse():
    converse_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    c1 = types.KeyboardButton(text='Aeon Active CX')
    c2 = types.KeyboardButton(text='All Star 1970s')
    c3 = types.KeyboardButton(text='All Star BB Prototype')
    c4 = types.KeyboardButton(text='One Star')
    c5 = types.KeyboardButton(text='Pro Blaze Strap')

    back = types.KeyboardButton(text='🔙Назад к категориям')

    converse_menu.add(c1, c2, c3)
    converse_menu.add(c4, c5)
    converse_menu.add(back)

    return converse_menu

def menu_jordan():
    jordan_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    j1 = types.KeyboardButton(text='Air Jordan 1 High')
    j2 = types.KeyboardButton(text='Air Jordan 1 Midle')
    j3 = types.KeyboardButton(text='Air Jordan 1 Low')
    j4 = types.KeyboardButton(text='Jordan 3 Retro')
    j5 = types.KeyboardButton(text='Jordan 4 Retro')
    j6 = types.KeyboardButton(text='Jordan 5 Retro')
    j7 = types.KeyboardButton(text='Ultra Fly 2 Low')
    j8 = types.KeyboardButton(text='Legacy 312')



    back = types.KeyboardButton(text='🔙Назад к категориям')

    jordan_menu.add(j1, j2, j3)
    jordan_menu.add(j4, j5, j6)
    jordan_menu.add(j7, j8)
    jordan_menu.add(back)

    return jordan_menu

def menu_nb():
    nb_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    nb1 = types.KeyboardButton(text='NB 530')
    nb2 = types.KeyboardButton(text='NB 725')
    nb3 = types.KeyboardButton(text='NB 827')
    nb4 = types.KeyboardButton(text='NB 452')
    nb5 = types.KeyboardButton(text='NB 327')
    back = types.KeyboardButton(text='🔙Назад к категориям')

    nb_menu.add(nb1, nb2, nb3)
    nb_menu.add(nb4, nb5)
    nb_menu.add(back)

    return nb_menu