# MyPimoroni-PirateRadio
mp3 player from NAS,or else; play random or not
Made with Pimoroni Pirate Radio and Raspberry Zero W

# How and What ?
- ON/OFF button dont stop the program
- OFF mode will blink VUmeter every X seconds until power ON is set back
- 2 play modes : random or track after track
- builds a tracklist based on a directory and subdirectories
- every action is displayed on console
- playing track displayed in console
- 

# Future
- .php to supervise playing and ressources
- use of holding button to change within different directories/internet source/etc. or run other pyhton script
- .php explore tracklist

# Remove pulseaudio (high CPU load on raspberry zero)
- `sudo nano /etc/asound.conf` for alsa config of VUmeters (brightness, decay, peak)

# Performances on Raspberry zero
- pulseaudio by itself was using 30/40% without any program running. Versus 1% for Alsa.
- better performances with Alsa, and ON/OFF button use in MyPirateRadio to PAUSE music and unload CPU.
- phatbeat uses 100% for playing a track... as a simple mp3 player...., there may be a way to reduce that no !?

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
