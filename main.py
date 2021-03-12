# coding=utf-8
import os
import telebot
import urllib
import json

bot=telebot.TeleBot("1668310826:AAES5z_lNYGr2QHZEHHs08gGa3a2vWfSOao")
@bot.message_handler(commands=['start','help'])
def send_start_message(message):
    bot.reply_to(message, "Envie o comando /people para saber quem está no espaço hoje!")

@bot.message_handler(commands=['people'])
def send_people(message):
    bot.reply_to(message, get_reply_message())

def get_reply_message():
    n_people, people = get_people()
    message = "Existem " \
        + str(n_people) + \
        "pessoas no espaço neste momento. São elas:\n\n"

    for person in people:
        message += person["name"] + \
            "na espaçonave " + person["craft"] + "\n\n"
    return message

def get_people():
    req = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(req)
    obj = json.loads(response.read())

    return obj["number"], obj["people"]

bot.polling()