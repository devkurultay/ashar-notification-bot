import telebot
from decouple import config
import telebot.types
import json

bot = telebot.TeleBot(config("TOKEN"))


data =  """{
        "telegram_users": [
            537210841, 12324, 4234234, 13425, 123123
        ]

}"""

data_js = json.loads(data)

@bot.message_handler(commands=['start'])
def get_notifications(message):
    bot.send_message(message.chat.id, 'Вы были успешно авторизованы!')
    if data_js['telegram_users']:
        for i in data_js['telegram_users']:
            return i

    
    

@bot.message_handler(content_types=['text'])
def send_notifications(message):
    if message.text == 'refresh': 
        chat_id = get_notifications(message)
        bot.send_message(chat_id, 'Помогите нам с переводом https://github.com/AktanKasymaliev/Weather_bot')
















bot.polling()