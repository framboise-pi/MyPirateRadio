# MyPirateRadio
[EN] mp3 player from NAS,or else; play random or not
Made with Pimoroni Pirate Radio and Raspberry Zero W
<br>[FR] lecteur mp3, développé pour une utilisation avec NAS avec le module pHAT BEAT de Pimoroni (pimoroni pirate radio kit) et un Raspberry zero W. Avec le système de mise en veille, pour permettre une utilisation - pas très écologique il est vrai - de la radio 24/24 7/7 par les utilisateurs, sans avoir à relancer de script par exemple.

<p align="center">
<img src="https://cdn.shopify.com/s/files/1/0174/1800/products/zero-w-kits-square-1_1024x1024.jpg?v=1606227996" width="200px">
  <img src="https://sha256systems.eu/WebRoot/Store27/Shops/5b7c8826-3528-4d6f-bd2d-c024fcdbd435/5EAF/3F55/6C80/BE99/F0D3/0A48/3570/4BF9/DEV-15749-4.jpeg" width="200px">
</p>

# How and What ?
- ON/OFF button dont stop the program ! = SLEEP MODE
- OFF mode will blink VUmeter every X seconds until power ON is set back
- 2 play modes : random or track after track
- builds a tracklist based on a directory and subdirectories
- every action is displayed on console
- playing track displayed in console
<br>Maybe I was not 'lucky' enough, but I did not find any script to fill my needs/hardware around a network mp3 player with .php and some functions like a ON/OFF button that don't quit the main program.

# Comment et pourquoi ?
- le bouton ON/OFF ne quitte pas le programme
- clignotement du VUmetre pour indiquer le mode veille (OFF)
- 2 modes de lecture : aléatoire ou simple
- construit une playlist à partir d'un dossier et ses sous repertoires
- toute action est affichée en console
- titre mp3 en lecture/chargé est affiché sur la consolle
<br>Je n'ai pas trouvé sur github ou ailleurs un programme python qui corresponde à mes besoins/matériels. Ce qui explique la création et le partage de celui ci.



# PERMISSIONS FOR .php (when launching python, web user name will be "www-data", not "root" or "pi")
## edit sudoers permissions
- `sudo visudo`
###  under the # User privilege specification
- `www-data ALL=(ALL) NOPASSWD: /usr/bin/python`
## add user www-data to gpio
- `sudo adduser www-data gpio`
## reboot/restart
- running mypirateradio.py with button on web page should work

# Future
- .php to supervise playing and ressources
- use of holding button to change within different directories/internet source/etc. or run other pyhton script
- .php explore tracklist

# Remove pulseaudio (high CPU load on raspberry zero)
- `sudo apt remove --purge pulseaudio`
# Alsa config of VUmeters (brightness, decay, peak)
- `sudo nano /etc/asound.conf`

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
