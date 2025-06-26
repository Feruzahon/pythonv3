import telebot
import wikipedia

bot = telebot.TeleBot('7683589498:AAH0KW0Wug1NM54KmDFn0yBcB2YOAedR15o')

# wikipedia.set_lang('ru')


# keyboard = telebot.types.ReplyKeyboardMarkup()
# button1 = telebot.types.KeyboardButton('Да')
# button2 = telebot.types.KeyboardButton('Нет')
# keyboard.add(button1,button2)

# @bot.message_handler(commands=['start','hello'])
# def start_messag(message):
#     bot.send_message(message.chat.id,'Привет, отправь мне слово и я найду информацию в википедии!')

# @bot.message_handler(content_types=['text'])
# def answer(message):
#     try:
#         text = wikipedia.page(message.text)
#         info_tetx = text.content[:1000]
#         result=info_tetx.split('. ')
#         result.pop(-1)
#         result='. '.join(result)+ '.'
#         bot.send_message(message.chat.id, result, reply_markup=keyboard)
#     except:
#         bot.send_message(message.chat.id, 'Ничего не найдено! Попробуйте еще')



# # библиотека аеграмм
# bot.polling(non_stop= True, interval=0)


wikipedia.set_lang('ru')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton('да')
button2 = telebot.types.KeyboardButton('нет')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    msg = bot.send_message(message.chat.id, 'Привет, отправь мне слово и я найду информацию в википедии!')
    bot.register_next_step_handler(msg, answer)

def answer(message):
    try:
        text = wikipedia.page(message.text)
        info_text = text.content[:1000]
        result = info_text.split('. ')
        result.pop(-1)
        result = '. '.join(result) + '.'
        bot.send_message(message.chat.id, result, reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Хотите продолжить?')
    except:
        bot.send_message(message.chat.id, 'Ничего не найдено!')

@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == 'да':
        msg = bot.send_message(message.chat.id, 'Хорошо, введи слово!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, answer)
    elif message.text == 'нет':
        bot.send_message(message.chat.id, 'Досвидания!', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку!')

bot.polling(non_stop=True, interval=0)