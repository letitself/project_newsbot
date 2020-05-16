# encoding='utf-8'
import requests
from bs4 import BeautifulSoup
import telebot
import random
from random import get_random_article



def count(soup, REL):
    i = 0
    while True:
        try:
            new_url = soup('a', rel = REL)[i]['href']
            i += 1
        except:
            return i
    


def panorama_article(user):
    home_url = 'https://panorama.pub'
    page = requests.get(home_url)
    unpretty_text = page.text
    soup = BeautifulSoup(unpretty_text, 'html.parser')
    article_url = soup('a', rel = 'bookmark')[random.randrange(count(soup, 'bookmark'))]['href']
    while article_url in notthesame[user]:
        article_url = soup('a', rel = 'bookmark')[random.randrange(count(soup, 'bookmark'))]['href']
    notthesame[user].append(article_url)
    new_page_text = requests.get(article_url).text
    new_soup = BeautifulSoup(new_page_text, 'html.parser')
    article = list(map(str, new_soup.findAll('p')))[2:-1]
    article = '\n'.join([i[3:-4] for i in article])
    return article
    

opb_token = '1034547759:AAFr2tHhzuccOW3IhS-UQ29kvskqgomkWGs'    #Oleg_Panorama_Bot
bot = telebot.TeleBot(opb_token)
notthesame = {}

@bot.message_handler(commands = ['start', 'help'])
def get_text_messages(message):
    bot.reply_to(message, 'text me PANORAMA if u want to see a meme or MEDUZA or RBK if u suriezniy')

@bot.message_handler(content_types = ['text'])
def get_text_messages2(message):
    if (message.text).upper() == 'PANORAMA':
        user = message.from_user.id
        if user not in notthesame.keys():
            notthesame[user] = []
        bot.send_message(message.chat.id, panorama_article(user))
    elif: 
        re.fullmatch('[А-Яа-я¸¨]+', ()):
        bot.send_message(message.chat.id, panorama_suitable_articles('https://panorama.pub/?s=' + message.text.replace(' ', '+')))
    else:
        bot.reply_to(message, 'text me PANORAMA')

def panorama_suitable_articles(url):
    url = 'https://panorama.pub'
    unpretty_text= page.text
    soup = BeautifulSoup(unpretty_text, 'html.parser')
    page = requests.get(home_url)
    ads = soup.find("nav", class_="main-mnu hidden-md hidden-sm hidden-xs").find("ul").find_all("li")
    links=[]
    for ad in ads:
        urls = ad.find("a").get("href")
        link = "https://panorama.pub" + urls
        print(link)
        links.append(link)
    return link
bot.polling(none_stop = True, interval = 0)
