# coding=utf-8
__author__ = "4N"
import requests
from lxml import etree
url = "https://web.immomo.com/live/29399418"
response = requests.get(url=url).content
html = etree.HTML(response)

print html.xpath('/html/body/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/strong/text()')