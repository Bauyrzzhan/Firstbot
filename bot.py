import telebot
import config
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-актобе/10-дней')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)

for el in html.select('#weather10'):
	t_min = el.select('.temperature .min')[0].text
	t_max = el.select('.temperature .max')[0].text
	text = el.select('.rSide .description')[0].text
	print(t_min + ',' + t_max + '\n' + text)

@bot.message_handler(commands=['start', 'help'])
def main(message):
	bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" + t_min + ',' + t_max + '\n' + text)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALnUF7YLW14VW_plHoECirHhCy8rrtsAAK9CQACeVziCb18AAG8_iwmuhoE')
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
    	bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALnVF7YLmfM4GbErjfCzNWctvisgLrnAAJlAANZu_wlOlxDJwFGvGcaBA')
    	bot.send_message(message.chat.id, 'Прощай')
    elif message.text.lower() == 'спасибо':
    	bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALngV7Y1DKD7hCLMNJJVyEZ-SjSFVH8AALCAQACVp29Cpl4SIBCOG2QGgQ')
    	bot.send_message(message.chat.id, 'Не за что.')
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling()
if __name__ == '__main__':
	bot.polling(none_stop=True)