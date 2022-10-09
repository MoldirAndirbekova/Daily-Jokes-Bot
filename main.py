import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = 'https://www.anekdot.ru/last/good'
API_Key ='5668421338:AAHojvBLgnzCnN7A94GoEgbE9Qyog_HkdJY'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    aneckdots = soup.find_all('div', class_ ='text')
    clear_jokes = [d.text for d in aneckdots]
    return clear_jokes

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_Key)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы посмеяться введи любое число:')

@bot.message_handler(content_types=['text'])
def joke(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любое число от 1-9')
bot.polling()