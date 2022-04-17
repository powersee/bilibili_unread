import os
import RPi.GPIO as GPIO
import requests
import time

GPIO.setmode(GPIO.BCM)


# 使用哪一个针脚 GPIO Num，21 对应 40 号
# 可以在终端输入 pinout 来查看 gpio 针脚定义信息
ioNum = 21
GPIO.setwarnings(False)
# 将引脚设置为输出端
GPIO.setup(ioNum, GPIO.OUT)

# 通过浏览器的 F12 获取　cookie
cookie = ""

url_mes = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/single_unread?unread_type=0&build=0&mobi_app=web'
headers = {'cookie': cookie}


# 获取未读消息数量
unread = requests.get(url_mes, headers=headers).json()
unfollow_unread = unread['data']['unfollow_unread']
follow_unread = unread['data']['follow_unread']
num = unfollow_unread + follow_unread

# 如果有未读消息，将未读数量打印出来
if num:
    print(num)
    GPIO.output(ioNum, GPIO.HIGH)
    print(time.asctime(time.localtime(time.time())))
    # GPIO引脚输出高电平，LED灯亮起
else:
    # print("No message.")
    GPIO.output(ioNum, GPIO.LOW)
    # GPIO引脚设置为低电平，LED灯熄灭
