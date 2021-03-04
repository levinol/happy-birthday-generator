import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembt = types.KeyboardButton('Сгенерируй поздравление 🎉')
    markup.add(itembt)
    bot.reply_to(message, "Ну и зачем ты меня запустил", reply_markup = markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Команда /generate генерирует поздравления с днем рождения. \nЕсли что-то сломалось пишите @lev1ne")

#@bot.message_handler(func=lambda m: True)
def echo_dropped(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembt = types.KeyboardButton('Сгенерируй поздравление 🎉')
    markup.add(itembt)
    bot.send_message(message.chat.id, "Не тыкай на кнопку", reply_markup = markup) 

#@bot.message_handler(commands=['generate'])
#def generate_msg(message):
#    bot.send_message(message.chat.id, "текст еще не доехал")   

@bot.message_handler(commands=['generate'])
@bot.message_handler(regexp='Сгенерируй поздравление 🎉')
def generate_msg(message):
    bot.send_message(message.chat.id, "текст еще не доехал")   

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Ну и зачем ты это высрал")


bot.polling()