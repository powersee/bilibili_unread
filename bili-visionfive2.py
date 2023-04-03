import requests
import time
import gpio as GPIO

# 设置引脚
gpio_num = 44
# 将引脚设置为输出端
GPIO.setup(gpio_num, GPIO.OUT)

# 通过浏览器的 F12 获取　cookie，只需 SESSDATA 和 _uuid 这两个值就行。
cookie = ""
url_mes = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/single_unread?unread_type=0&build=0&mobi_app=web'
headers = {'cookie': cookie}

# 获取未读消息数量
unread = requests.get(url_mes, headers=headers).json()
unfollow_unread = unread['data']['unfollow_unread']
follow_unread = unread['data']['follow_unread']
num = unfollow_unread + follow_unread

if num:
    # 如果有未读消息，将未读数量打印出来
    print("unread", num)
    GPIO.output(gpio_num, GPIO.HIGH)
    # 引脚输出高电平，LED灯亮起
    print(time.asctime(time.localtime(time.time())))
else:
    GPIO.output(gpio_num, GPIO.LOW)
    # 引脚设置为低电平，LED灯熄灭
