# MyPimoroni-PirateRadio
mp3 player from NAS,or else; play random or not
Made with Pimoroni Pirate Radio and Raspberry Zero W

# Remove pulseaudio (high CPU load on raspberry zero)
- `sudo nano /etc/asound.conf` for alsa config

# Performances on Raspberry zero
- alsa dont charge CPU when not used ... pulseaudio uses around 30% minimum, all the time, on Pi0
- pulse audio by itself was using 30/40% without any program running. Versus around nothing for Alsa
- better performances with Alsa, and ON/OFF button use in MyPirateRadio

pHAT-beat
- https://github.com/pimoroni/phat-beat
- https://pinout.xyz/pinout/phat_beat#
- https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-phat-beat

ideas to include :
- https://github.com/MiczFlor/RPi-Jukebox-RFID
- 

I took ideas and code from:
- https://github.com/andywarburton/pirate_jukebox
- https://github.com/ajalexsmith/PirateRadio
- 

use python 2
- python pirateradio.py
