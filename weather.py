# coding=utf-8
__author__ = "4N"

import requests
from lxml import etree
import time
from wxpy import *

# url = "http://www.weather.com.cn/weather/101010100.shtml"
url = "http://www.weather.com.cn/weather/101280101.shtml"

def message(url):
    response = requests.get(url=url).content
    html = etree.HTML(response)
    dress=html.xpath('//*[@id="chuanyi02"]/a/p/text()')[0]
    situation = html.xpath('//*[@id="7d"]/ul/li[2]/p[1]/text()')[0]
    h_tem = html.xpath('//*[@id="7d"]/ul/li[2]/p[2]/span/text()')[0]
    l_tem = html.xpath('//*[@id="7d"]/ul/li[2]/p[2]/i/text()')[0]
    yue = time.strftime("%m", time.localtime(time.time()+10800))
    ri = time.strftime("%d", time.localtime(time.time()+10800))
    weather = "4N为你带来"+yue+"月"+ri+"日 天气预报:\n明天"+situation.encode("utf-8") + "。温度：" + h_tem.encode("utf-8") + "-" + l_tem.encode("utf-8") + "。" + dress.encode("utf-8")
    return weather
if __name__ == '__main__':
    bot = Bot()
    hanle = bot.friends().search("Timelism")[0]
    Michael = bot.friends().search("Michael")[0]
    huixin = bot.friends().search("半岛铁盒".decode("utf-8"))[0]
    zhouyin = bot.friends().search("小茵 🐳".decode("utf-8"))[0]
    url_bj = "http://www.weather.com.cn/weather/101010100.shtml"
    url_gz = "http://www.weather.com.cn/weather/101280101.shtml"
    while True:
        if time.strftime("%H") == '22' and time.strftime("%M") == "00":
            weather_gz = message(url_gz)
            weather_bj = message(url_bj)
            hanle.send(weather_bj.decode("utf-8"))
            huixin.send(weather_bj.decode("utf-8"))
            Michael.send(weather_gz.decode("utf-8"))
            zhouyin.send(weather_gz.decode("utf-8"))
            time.sleep(500)
