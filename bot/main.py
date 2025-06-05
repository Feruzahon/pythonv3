import telebot

bot = telebot.TeleBot('7683589498:AAH0KW0Wug1NM54KmDFn0yBcB2YOAedR15o')

@bot.message_handler(commands=['start','hello'])
def start_messag(message):
    bot.send_message(message.chat.id,'Привет я бот!')


# библиотека аеграмм
bot.polling(non_stop= True, interval=0)