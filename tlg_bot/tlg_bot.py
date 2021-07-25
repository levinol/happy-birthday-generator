import telebot
from telebot import types
from socket import *
import os

bot = telebot.TeleBot(str(os.getenv('TOKEN')), parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembt = types.KeyboardButton('Сгенерируй поздравление 🎉')
    itembt2 = types.KeyboardButton('Сгенерируй кастомное поздравление 🎉')
    markup.add(itembt, itembt2)
    bot.reply_to(message, "Ну и зачем ты меня запустил", reply_markup = markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Команда /generate генерирует поздравления с днем рождения. \nЕсли что-то сломалось пишите @lev1ne")

#@bot.message_handler(func=lambda m: True)
def echo_dropped(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembt = types.KeyboardButton('Сгенерируй поздравление 🎉')
    itembt2 = types.KeyboardButton('Сгенерируй кастомное поздравление 🎉')
    markup.add(itembt, itembt2)
    bot.send_message(message.chat.id, "Не тыкай на кнопку", reply_markup = markup) 

#@bot.message_handler(commands=['generate'])
#def generate_msg(message):
#    bot.send_message(message.chat.id, "текст еще не доехал")   

@bot.message_handler(commands=['generate'])
@bot.message_handler(regexp='Сгенерируй поздравление 🎉')
def generate_msg(message):
    #tcp

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)
    data = 'Проза'
    data = str.encode(data)
    tcp_socket.send(data)
    data = bytes.decode(data)
    data = tcp_socket.recv(1024)
    print('sendin data', data)
    bot.send_message(message.chat.id, data) 
    tcp_socket.close() 


@bot.message_handler(regexp='Сгенерируй кастомное поздравление 🎉')
def generate_custom_msg(message):
    bot.send_message(message.chat.id, 'Введите начало поздравления')
    bot.register_next_step_handler(message, custom_msg_hadnler) 

def custom_msg_hadnler(message):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)
    data = message.text
    print(data)
    data = str.encode(data)
    tcp_socket.send(data)
    data = bytes.decode(data)
    data = tcp_socket.recv(1024)
    print('sendin data', data)
    bot.send_message(message.chat.id, data) 
    tcp_socket.close() 

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Ну и зачем ты это сказал")


host = str(os.getenv('HOST'))
port = int(os.getenv('PORT'))
addr = (host,port)

if __name__ == "__main__":
    bot.polling()
    