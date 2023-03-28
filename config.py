import telebot

BOT_TOKEN = '5873814230:AAGfDLmGCzWNFexqkAmPNm4pvEIv2GTYy9M'

bot = telebot.TeleBot(BOT_TOKEN)

team_id = '-1001812110960'
admin_id = '577235663'

error_message = 'Error 404\n'\
                'Приносим свои извинения, наша команда уже занимается данной проблемой\n' \
                '\n' \
                'С уважением +repeat team'

#отправка ошибки в чат и админам
def send_error(call, adm_mess):
    bot.send_message(call.message.chat.id, text=error_message)

    bot.send_message(chat_id=admin_id, text=adm_mess)


