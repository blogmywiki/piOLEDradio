# piOLEDradio

Recycling an ancient Raspberry Pi Model B Rev 2 to make a simple internet radio with OLED display and 4 push buttons to change channel and volume.

## Re-requistes
There are many, including but probably not limited to:
- generic I2C OLED display connected to I2C pins on the Pi
- push buttons connected to on one side to pins 17, 27, 22 and 10 and on the other to GND
- I2C enabling on the Pi using raspi-config
- install MPC / MPD and add a bunch of online radio stations 
- install pip3
- install this OLED Python library: https://github.com/rm-hull/luma.oled 
- install guizero Python library
- move the ChiKareGo.ttf font to the same directory as radio.py, in this case specified as /home/pi/
- Use systemd to start the script after the Pi has network:

`sudo nano /lib/systemd/system/myscript.service`

add these lines:
`
[Unit]

Description=OLED display radio

After=network-online.target

[Service]

Type=idle

ExecStart=/usr/bin/python3 /home/pi/radio.py

[Install]

WantedBy=network-online.target
`

Save and exit with Ctrl+x,Y and ENTER.

Change the permissions on the configuration file to 644:

`sudo chmod 644 /lib/systemd/system/myscript.service`

Now tell systemd to start the process on boot:

`sudo systemctl daemon-reload`

`sudo systemctl enable myscript.service`

Reboot the Pi and it should start up.

## To do
- Add volume progress bar
- Maybe add graceful shut down
- Perhaps add display IP address option
- Improve clock placement so wider dates don't cause it to move around
