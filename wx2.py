# coding=utf-8
__author__ = "4N"

from wxpy import *

bot = Bot()
my_friend = bot.friends().search("Micheal")[0]
my_friend.send('Hello WeChat!')


@bot.register(my_friend)
def print_others(msg):
    print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
    return 'bb'

# 最后，堵塞线程，让程序持续运行下去
embed()

