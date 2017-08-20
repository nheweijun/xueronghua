# coding=utf-8
__author__ = "4N"

import requests
import re
import time


uid = "17801035352"
ucode = "25f9e794323b453885f5181f1b624d0b"
first_time = str(int(time.time()*1000))
#

oauth_url = "https://oauth.immomo.com/oauth/authorize?response_type=code&client_id=mm14833cdab154eaf7&scope=name,avatar&state=" + first_time
oauth_header = {
    "Host": "oauth.immomo.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://web.immomo.com/",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0"
}

oauth_response = requests.get(url=oauth_url)

#################################################################
code_hash = re.findall('"hash":"([^"]*)"', oauth_response.text)[0]

code_url = "https://oauth.immomo.com/user/code?username=" + uid + "&time=" + str(int(time.time()*1000))
code_headers = {
    "Host": "oauth.immomo.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://oauth.immomo.com/oauth/authorize?response_type=code&client_id=mm14833cdab154eaf7&scope=name,avatar&state=1496121600989",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive"
}
code_data = {
    "client": "pc",
    "client_id": "mm14833cdab154eaf7",
    "code": "",
    "hash": code_hash,
    "password": ucode,
    "redirect_uri":"",
    "response_type":"code",
    "scope": "name,avatar",
    "state": first_time,
    "token": "",
    "token": "",
    "username": uid
}

code_response = requests.post(url=code_url, data=code_data, headers=code_headers)

#####################################################################
# need hash



user_check_hash = re.findall('"hash":"([^"]*)"', oauth_response.text)[0]

duanxin = ""

user_check_hash = 'momo_check_592d16ed9d97b9.24310775'


user_check_url = "https://oauth.immomo.com/user/check?username=" + uid + "&time=" + str(int(time.time()*1000))
user_check_headers = {
    "Connection": "keep-alive",
    "Origin": "https://oauth.immomo.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Referer": "https://oauth.immomo.com/oauth/authorize?response_type=code&client_id=mm14833cdab154eaf7&scope=name,avatar&state=" + first_time,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
}
user_check_data = {
    "username":	uid,
    "password":	ucode,
    "client_id": "mm14833cdab154eaf7",
    "redirect_uri": "",
    "state"	: first_time,
    "scope": "name,avatar",
    "hash": user_check_hash,
    "identity": "",
    "iconurl": "",
    "response_type": "code",
    "client": "pc",
    "code": duanxin,
    "token": ""
}
# user_check_data_encode = urllib.urlencode(user_check_data)
user_check_response = requests.post(url=user_check_url, data=user_check_data, headers=user_check_headers)
momo_session = ""
momo_csrf_token = ""
###################################################################################################################################
# need cookie
sure_url = "https://oauth.immomo.com/oauth/authorize?response_type=code&client_id=mm14833cdab154eaf7&redirect_uri=&scope=name,avatar&state=" + str(int(time.time()*1000))
sure_headers = {
    "Host": "oauth.immomo.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": momo_session + "; " + momo_csrf_token
}
sure_response = requests.get(url=sure_url, headers=sure_headers)
##################################################################################
#need hash cookie
check_hash = re.findall('name="hash" value="([^"]*)"', sure_response.text)[0]
check_data = {
"hash":	check_hash,
"scope": "name,avatar",
"advanced_scope": ""	,
"decide": "确认登录"
}
check_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": momo_session + "; " + momo_csrf_token
}
check_url = "https://oauth.immomo.com/oauth/check"
check_response = requests.post(url=check_url, data=check_data, headers=check_headers)
location_url = dict(check_response.history[0].headers)["Location"]
# location_url = "https://web.immomo.com/oauth/cb?code=D6A6618E-AE11-F694-0131-25EF4E01A97C&state="+str(int(time.time()*1000))
location_headers = {
    "Host": "web.immomo.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer: https": "//oauth.immomo.com/oauth/authorize?response_type=code&client_id=mm14833cdab154eaf7&redirect_uri=&scope=name,avatar&state=1496035070375",
    "Cookie": "momo_session=53d6e1a7b0ca4d48561a3949f79c15a1; momo_csrf_token=fa0a05a7bd1a36f1cb0037613a4d9e71",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
location_response = requests.get(location_url)
header = dict(location_response.headers._store)
webmomo = re.findall('webmomo=([^;]*);', header.get("set-cookie")[1])[0]
print webmomo




dd=2
