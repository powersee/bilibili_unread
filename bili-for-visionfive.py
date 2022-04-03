import requests
import time
import os
# 使用time模块的sleep来控制亮灯熄灯时间间隔

# 用使用哪一个针脚，例如 448、450、452 等
gpio = 452
led = '/sys/class/gpio/gpio' + str(gpio)

# 通过浏览器的 F12 获取　cookie
cookie = ""

url_mes = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/single_unread?unread_type=0&build=0&mobi_app=web'
headers = {'cookie': cookie}

if os.path.exists(led):
    pass
else:
    os.system(f'echo {gpio} > /sys/class/gpio/export')

os.system(f'echo out > {led}/direction')
# 将引脚设置为输出端

# 获取未读消息数量
unread = requests.get(url_mes, headers=headers).json()
unfollow_unread = unread['data']['unfollow_unread']
follow_unread = unread['data']['follow_unread']
num = unfollow_unread + follow_unread
# 如果有未读消息，将未读数量打印出来
if num:
    print(num)
    #GPIO.output(ioNum, GPIO.HIGH)
    os.system(f'echo 1 > {led}/value')
    print(time.asctime(time.localtime(time.time())))
    # 引脚输出高电平，LED灯亮起
else:
#    print("No message.")
    #GPIO.output(ioNum, GPIO.LOW)
    os.system(f'echo 0 > {led}/value')
    # 引脚设置为低电平，LED灯熄灭

