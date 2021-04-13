from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
import datetime
from gpiozero import Button
import os
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

btn_ch_down = Button(17)
btn_ch_up = Button(27)
btn_vol_down = Button(10)
btn_vol_up = Button(22)
today_last_time = "Unknown"
station_list = ["off", "fip", "Scala", "GHR", "Radio 4", "4 Extra", "6music", "BBC WS"]
station = 0
volume = 50
os.system("mpc volume 50")
font_path = '/home/pi/ChiKareGo.ttf'
font2 = ImageFont.truetype(font_path, 32)
font3 = ImageFont.truetype(font_path, 16)

while True:
    now = datetime.datetime.now()
    today_date = now.strftime("%d %b %y")
    today_time = now.strftime("%H:%M:%S")
    if today_time != today_last_time:
        today_last_time = today_time
        with canvas(device) as draw:
            now = datetime.datetime.now()
            today_date = now.strftime("%d %b %y")
            draw.text((0,0), station_list[station], font=font2, fill="white")
            draw.text((0,30), "volume " +  "O"*int(volume/10), font=font3, fill="white")
            draw.text((0,51), today_date+"     "+today_time, font=font3, fill="white")
    if btn_ch_up.is_pressed:
        station += 1
        if station > 7:
            station = 0
            os.system("mpc stop")
        else:
            os.system("mpc play " + str(station))
    if btn_ch_down.is_pressed:
        station -= 1
        if station == 0:
           os.system("mpc stop")
        elif station < 0:
           station = 7
           os.system("mpc play 7")
        else:
           os.system("mpc play " + str(station))
    if btn_vol_down.is_pressed:
        volume -= 10
        os.system("mpc volume " + str(volume))
    if btn_vol_up.is_pressed:
        volume += 10
        os.system("mpc volume " + str(volume))

    time.sleep(0.1)
