import requests, telebot, random, plot_panorama
from bs4 import BeautifulSoup
from datetime import datetime, date
import matplotlib.pyplot as plt
import rbc_meduza


def count(soup, REL):
    i = 0
    while True:
        try:
            soup('a', rel = REL)[i]['href']
            i += 1
        except:
            return i
    


def panorama_article(user):
    home_url = 'https://panorama.pub'
    page = requests.get(home_url)
    unpretty_text = page.text
    soup = BeautifulSoup(unpretty_text, 'html.parser')
    article_url = soup('a', rel = 'bookmark')[random.randrange(count(soup, 'bookmark'))]['href']
    stop = 100  #to not have endless cicle if a user has gotten all articles
    while article_url in notthesame[user] and stop:
        stop -= 1
        article_url = soup('a', rel = 'bookmark')[random.randrange(count(soup, 'bookmark'))]['href']
    notthesame[user].append(article_url)
    return article_url
    

opb_token = '1034547759:AAFr2tHhzuccOW3IhS-UQ29kvskqgomkWGs'    #Oleg_Panorama_Bot
bot = telebot.TeleBot(opb_token)
notthesame = {}
plots_per_day = {}

@bot.message_handler(commands = ['start', 'help', 'random_article', 'freq_pie'])
def get_text_messages(message):
    if message.text == '/random_article':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True)
        keyboard.row('panorama', 'meduza', 'rbc')
        bot.send_message(message.chat.id, 'What article do u want to see?', reply_markup = keyboard)
    elif message.text == '/freq_plot':
        if datetime.now().date() not in plots_per_day.keys():
            plots_per_day[datetime.now().date()] = plot_panorama.today()
        labels = []
        vals = []
        for item in plots_per_day[datetime.now().date()]:
            labels.append(item[0])
            vals.append(item[1])
        ax = plt.subplots()[1]
        ax.pie(vals, labels=labels, autopct='%1.1f%%')
        ax.axis("equal")
        plt.savefig('C:/Users/админ/Desktop/Новая папка/haha.png')
        with open('C:/Users/админ/Desktop/Новая папка/haha.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, str(datetime.now().date()))


@bot.message_handler(content_types = ['text'])
def answer_to_text(message):
    user = message.from_user.id
    if message.text.lower() == 'panorama':
        if user not in notthesame.keys():
            notthesame[user] = []
        bot.send_message(message.chat.id, panorama_article(user))  
    elif message.text.lower() == 'meduza':
        bot.send_message(message.chat.id, rbc_meduza.meduza())
    elif message.text.lower() == 'rbc':
        bot.send_message(message.chat.id, rbc_meduza.rbc())



bot.polling(none_stop = True, interval = 0)