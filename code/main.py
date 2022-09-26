import sys
import telebot
import os
import random
import numpy as np
from utils import *


def del_env():
    del os.environ['TELEGRAM_BOT_TOKEN']
    for i in range(len(sys.argv)):
        sys.argv[i] = ''


def send_welcome(message):
        bot.send_message(message.chat.id, "Hello, " + message.from_user.username + "!")


def help(message):
        bot.send_message(message.chat.id,   "WARNING: This is a NSFW bot!\n" \
                                            "This bot has the following commands:\n" \
                                            "/start -- start the bot\n" \
                                            "/help -- view documentation\n" \
                                            "/maza -- faza\n" \
                                            "/faza -- maza\n" \
                                            "/joke -- hear a joke\n" \
                                            "/eval -- evaluate a mathematical expression\n" \
                                            "/exec -- exec a python script\n" \
                                            f"Maximal length of a message is {str(max_len_in)} symbols\n")


def maza(message):
        bot.send_message(message.chat.id, 'faza')


def faza(message):
        bot.send_message(message.chat.id, 'maza')


def joke(message):
        bot.send_message(message.chat.id, "your mom gay")


def bot_eval(message):
        if len(message.text) > max_len_in:
            bot.send_message(message.chat.id, "Too long command")
        else:
            result = calc_func(eval, strip_text(message.text, '/eval'))
            if result != None:
                if len(str(result)) <= max_len_out:
                    bot.send_message(message.chat.id, result)
                else:
                    bot.send_message(message.chat.id, "The answer is too long to send you back")
            else:
                bot.send_message(message.chat.id, "Invalid input or too slow to evaluate")


def bot_exec(message):
        if len(message.text) > max_len_in:
            bot.send_message(message.chat.id, "Too long command")
        else:
            result = calc_func(exec, strip_text(message.text, '/exec'))
            if result != None:
                if len(str(result)) <= max_len_out:
                    bot.send_message(message.chat.id, result)
                else:
                    bot.send_message(message.chat.id, "The answer is too long to send you back")
            else:
                bot.send_message(message.chat.id, "Invalid input or too slow to evaluate")


if __name__ == '__main__':
    bot = telebot.TeleBot(sys.argv[1], parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    del_env()

    max_len_in = 5000
    max_len_out = 5000

    bot.message_handler(commands=['start'])(send_welcome)
    bot.message_handler(commands=['help'])(help)
    bot.message_handler(commands=['maza'])(maza)
    bot.message_handler(commands=['faza'])(faza)
    bot.message_handler(commands=['joke'])(joke)
    bot.message_handler(commands=['eval'])(bot_eval)
    bot.message_handler(commands=['exec'])(bot_exec)    

    bot.infinity_polling()
