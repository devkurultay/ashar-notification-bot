import telebot
from decouple import config
import telebot.types
import json

bot = telebot.TeleBot(config("TOKEN"))


data =  """{
        "telegram_users": [
            537210841
        ]

}"""

data_js = json.loads(data)

@bot.message_handler(commands=['start'])
def get_notifications(message):
    users = []
    bot.send_message(message.chat.id, 'Вы были успешно авторизованы!')
    for i in data_js['telegram_users']:
        users.append(i)
    return users
    
    

@bot.message_handler(content_types=['text'])
def send_notifications(message):
    if message.text == 'refresh': 
        chat_id = get_notifications(message)
        for id_users in chat_id:
            bot.send_message(id_users, 'Помогите нам с переводом https://github.com/AktanKasymaliev/Weather_bot')
















bot.polling()