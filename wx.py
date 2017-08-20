# coding=utf-8
__author__ = "4N"
import requests
import time
from wxpy import *
from lxml import etree
import lxml
import urllib
from bs4 import BeautifulSoup
import re
#
def message():
    h2_url = "http://en.weather.com.cn/weather/101010100.shtml?index=2"
    h3_url = "http://en.weather.com.cn/weather/101010100.shtml?index=3"
    pre = requests.get(url=h2_url).content
    advice = requests.get(url=h3_url).content
    pre_content = re.findall('<ul class="hour6 clearfix">(.*)<!--6小时 end -->', pre, re.S)[0]
    h2_tianqi = re.findall('<p class="wea">([^<]*)</p>', pre_content, re.S)
    h2_tem = re.findall('<i class="wC">([^<]*)</i>', pre_content, re.S)
    p_dress = re.findall('<li class="li3">(.*?)</li>', advice, re.S)[0]
    dress = re.findall('<em class="mouseOn">(.*?)</em>', p_dress, re.S)[0]
    p_kongqi = re.findall('<li class="li5">(.*?)</li>', advice, re.S)[0]
    kongqi = re.findall('<em class="mouseOn">(.*?)</em>', p_kongqi, re.S)[0]
    # message2 = "Beijing Weather for Tomorrow\n02:00-08:00 " + h2_tianqi[1].strip() + " High:" + h2_tem[2].strip()  \
    message2 = "Beijing Weather for Tomorrow " + time.strftime("%Y-%m-%d", time.localtime(time.time()+10800)) + "\n\n02:00-08:00 " + h2_tianqi[1].strip() + " " + h2_tem[3].strip()[:-2] + "-" + h2_tem[2].strip()[:-2] + "℃".decode("utf-8") + "\n08:00-14:00 " + h2_tianqi[2].strip() + " " + h2_tem[5].strip()[:-2] + "-" + h2_tem[4].strip()[:-2] + "℃".decode("utf-8") + "\n14:00-20:00 " + h2_tianqi[2].strip() + " " + h2_tem[7].strip()[:-2] + "-" + h2_tem[6].strip()[:-2] + "℃".decode("utf-8") + "\n\n" + dress.strip().decode("utf-8") + "\n\n" + kongqi.strip().decode("utf-8")
    return message2



bot = Bot()
hanle = bot.friends().search("Timelism")[0]
m = bot.friends().search("Michael")[0]
huixin = bot.friends().search("半岛铁盒".decode("utf-8"))[0]

while True:
    if time.strftime("%H") == '22' and time.strftime("%M") == "00":
        weather = message()
        hanle.send(weather)
        huixin.send(weather)
        # m.send(weather)
        time.sleep(70)

