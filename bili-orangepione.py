#/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在香橙派 one 上面使用 python2 来运行
# 需要自己先去安装 gpio 库

import requests
import time
import os

# 通过浏览器的 F12 获取　cookie


# 同样的，获取 uuid 和 SESSDATA 就行
# 当然，使用完整的 cookie 也行
cookie = ""
# 多久查询一次，默认为　60　秒
ioNum = 21
url_mes = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/single_unread?unread_type=0&build=0&mobi_app=web'
headers = {'cookie': cookie}


#import the library
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#initialize the gpio module
gpio.init()

led=port.PG9
#setup the port (same as raspberry pi's gpio.setup() function)
gpio.setcfg(led, gpio.OUTPUT)


# 获取未读消息数量
unread = requests.get(url_mes, headers=headers).json()
unfollow_unread = unread['data']['unfollow_unread']
follow_unread = unread['data']['follow_unread']
num = unfollow_unread + follow_unread
# 如果有未读消息，将未读数量打印出来
if num:
    print(num)
    #print(os.system("ledon green"))
    gpio.output(led, gpio.HIGH)
    print(time.asctime(time.localtime(time.time())))
    # LED灯亮起
else:
    print("No message.")
    gpio.output(led, gpio.LOW)
    #print(os.system("ledoff green"))
    # LED灯熄灭

