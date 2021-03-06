############################
# MyPimoroni-PirateRadio
# https://github.com/framboise-pi/MyPimoroni-PirateRadio
# Copyright(C) 2021 Cedric Camille Lafontaine http://www.framboise-pi.fr,
# version 0.0.1
#
# [TO MOUNT A NETWORK DRIVE]
# sudo mount -t cifs //XXX.XXX.XXX.XXX/NetworkDrive /mnt/Drive -o user=xxxxxxxx,vers=1.0
#
# [EASY INSTALL for PIMORONI pHAT]
# curl https://get.pimoroni.com/vlcradio | bash
#
# DO NOT FORGET TO EDIT VARIABLES :
# string with your files path : music_directory_1
# (it will include all subdirectories)
# volume - default volume on start
# volume_inc - increment for volume UP/DOWN
#
# phatbeat.set_pixel(x, r, g, b, brightness 0>1, channel 0 or 1)
###########################

######################################################################## DEPENDANCES


from pygame import mixer
import phatbeat, glob
import os, random
import time

######################################################################## VARIABLES

music_directory_1 = '/mnt/XXX/xxx/'
random_mode = True
track = -1
volume_inc = 0.01
volume = 0.01
song_now = ""
player = 'loading'
Run = True

######################################################################## FUNCTIONS

## TO UPDATE
def phatbeat_start():
    phatbeat.clear()
    #phatbeat.set_all(255, 0, 255)
    for p in range(16):
	phatbeat.set_pixel(p, 200, 0, 255, 0.1)
    phatbeat.show()

### NOT USED
def phatbeat_wait():
    #global player
    #player = 'wait'
    phatbeat.clear()
    #phatbeat.set_all(0, 255, 0)
    #for channel in (0,1):
    phatbeat.set_pixel(0, 0, 255, 0, 0.1, 0)
    phatbeat.set_pixel(0, 0, 0, 255, 0.1, 1)
    phatbeat.show()

def song_randomize():
    global tracklist
    global song_now
    global player
    player = 'loading'
    song = random.choice(tracklist)
    tracklist.remove(song)
    mixer.music.load(song)
    song_now = song
    count = str(len(tracklist))
    print("--- there are " + count + " mp3 songs in tracklist")
    print("loaded : " + song_now)

def song_next():
    global tracklist
    global song_now
    global player
    global track
    player = 'loading'
    track = track + 1
    song = tracklist[track]
    mixer.music.load(song)
    song_now = song
    count = str(len(tracklist))
    # as an array start on 0, increment for real track number
    tracknumber = track + 1
    print("--- " + str(tracknumber) + "/" + count + " of mp3 songs in tracklist")
    print("loaded : " + song_now)

######################################################################## START

phatbeat_start()
# mp3 files to array
print ("...reading mp3 folders")
files = glob.glob(music_directory_1 + '/**/*.mp3')
# make a copy of files for preventing dupes
tracklist = files[:]
songs = len(tracklist)

print (".....starting My Pirate Radio")
print ("folder :" + music_directory_1)
print ("--- there are " + str(songs) + " mp3 songs in tracklist")
if songs <= 0:
    print ("ERROR: No mp3 files found !!!")
    exit
if random_mode:
    print ("--- Random mode is ON")
else :
    print ("--- Random mode is OFF")
    
######################################################################## PYGAME

#pygame.init()
mixer.pre_init(44100, -16, 1, 2048) # setup mixer to avoid sound lag
mixer.init()
mixer.music.set_volume(volume)

if random_mode :
    print ("**** loading first random track")
    song_randomize()
else :
    print ("**** playing first track")
    song_next()
    
######################################################################## PLAY/PAUSE button

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin):
    global player
    if player == 'pause':
	mixer.music.unpause()
	player = 'play'
	print("=-=-=- player UNPAUSED")
	print("now playing : " + song_now)
    elif player == 'play':
	mixer.music.pause()
	player = 'pause'
	print("=-=-=- player PAUSED")
    # First play
    else:
	mixer.music.play()
	player = 'play'
	print("now playing : " + song_now)
    time.sleep(1)
		
######################################################################## VOLUME UP button

@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    global volume
    volume = volume + volume_inc
    mixer.music.set_volume(volume)
    print ("volume : " + str(volume))
    
######################################################################## VOLUME DOWN button
@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    global volume
    volume = volume - volume_inc
    mixer.music.set_volume(volume)
    print ("volume : " + str(volume))
    
######################################################################## NEXT TRACK button
@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    global song_now
    if random_mode :
	song_randomize()
    else :
	song_next()
    mixer.music.play()
    player = "play"
    print ("playing next : " + song_now)	

######################################################################## PREVIOUS TRACK button
@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin):
    global song_now
    player = 'loading'
    mixer.music.load(song_now)
    mixer.music.play()
    player = 'play'
    print ("previous : " + song_now)

######################################################################## POWER ON/OFF button

@phatbeat.on(phatbeat.BTN_ONOFF, repeat=False)
def onoff(pin):
    global Run
    phatbeat.clear()
    # invert Run True/False
    Run = not Run
    print ("ON/OFF button: " + str(Run))
    
######################################################################## MAIN
    
while True:
    if Run == True:
	if player != 'loading':
	    # automatic play track after track
	    if(mixer.music.get_busy() == 0 and player != 'pause'):
		if random_mode:
		    song_randomize()
		else :
		    song_next()
		mixer.music.play()
		player = "play"
    if Run == False:
	if player != 'pause':
	    player = 'pause'
	    mixer.music.pause()
	    mixer.init()
	    mixer.music.set_volume(volume)
	phatbeat_wait()
	time.sleep(2)


