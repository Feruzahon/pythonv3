import telebot 

bot = telebot.TeleBot('7729372179:AAFNv0812Xp_b9wDh6vgSSKp5ziWg6EOAtg')

@bot.message_handler(commands=['hello','start'])
def start_messege(message):
    bot.send_message(message.chat.id,'Hello, I am bot!')

@bot.message_handler(func=lambda message: message.text.lower() in ['привет', 'hello'])
def handle_greetings(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, я бот!')
    else:
        bot.send_message(message.chat.id, 'Hello, I am bot!')

bot.polling(non_stop=True, interval=0)