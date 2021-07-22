# B站未读消息提示器
通过一个 python 脚本，查询B站未读消息，当有未读消息时，让 LED 灯亮，没有时则灯灭。

## ESP8266

将  [main.py](https://raw.githubusercontent.com/powersee/bilibili_unread/master/main.py)  传入 已经刷了 micropython 的 esp8266 ，开机时会自动执行这个脚本。

我设置了一通电灯就亮，如果你的未读消息是 0 的话，那么等连接好 wifi 并联网查询后，灯就会灭。我通过计时器发现，从通电到灯灭的时间是 13 秒左右。

经过测试发现，cookie 并不需要全部，通过排查，我发现如果只查询未读消息的话，只需要 cookie 中的 `SESSDATA` 和 `_uuid` 这两个值就行。当然，用完整的 cookie 也不影响功能。

## 玩客云

将 [bili-for-wky.py](https://raw.githubusercontent.com/powersee/bilibili_unread/master/bili-for-wky.py) 放进刷了第二版固件的玩客云

然后自己填写好 cookie ，自己手动执行一下

```
python3 bili-for-wky.py
```

看看有没有效果，有的话再去添加到 crontab 任务。

## 香橙派

请使用 [bili-orangepione.py](https://raw.githubusercontent.com/powersee/bilibili_unread/master/bili-orangepione.py) ，需要自己先安装 GPIO 库。

https://github.com/duxingkei33/orangepi_PC_gpio_pyH3

步骤：

1

```
git clone https://github.com/duxingkei33/orangepi_PC_gpio_pyH3.git
cd orangepi_PC_gpio_pyH3
apt install -y python python-dev
python setup.py install
```
2
```
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python get-pip.py
pip install requests
```
3
```
orangepione:~:# python bili-for-orangepione.py 
No message.
```


