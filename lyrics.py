﻿#Lyrics.py
#Designed to just echo out the lyrics to the console while in sync with the music.
#Lets start!
import time
import os
import pygame
import sys
import network
#from __future__ import print_function
print("")
file = 'stillalivehq.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
def heard(phrase):
  print "them:" + phrase
network.wait(whenHearCall=heard)
time.sleep(10)

def lyric( str , tme):
  	"Lyrics printed out through this command should be orange"
	#time.sleep(1)
	for c in str:
		#Ok timing works by calculating length of string, getting old timing removing 0.1 second from it and then calculating time per char.
		num = len(str)
		timee = tme - 0.3
		timeperchar = timee/num
		#print(timeperchar)
		sys.stdout.write( '%s' % c )
		sys.stdout.flush()
		time.sleep(timeperchar)
		
	
	sys.stdout.write("\n")
        sys.stdout.flush()
	time.sleep(0.3)

	

os.system("clear")
pygame.mixer.music.play()
network.say("0")
lyric("This was a triumph.",4)
#time.sleep(4)
lyric("I'm making a note here:",2)
#time.sleep(2)
lyric("HUGE SUCCESS.",3)
#time.sleep(3)
lyric("It's hard to overstate ",2)
#time.sleep(2)
lyric("my satisfaction.",5)
#time.sleep(5)
network.say("1")
lyric("Aperture Science ",4)
#time.sleep(4)
lyric("We do what we must",2.2)
#time.sleep(2.2)
lyric("because we can.",3)
#time.sleep(3)
lyric("For the good of all of us.",3)
#time.sleep(3)
network.say("4")#Radioactive
lyric("Except the ones who are dead.",2)
#time.sleep(2)
network.say("1")
lyric("But there's no sense crying",2.5)
#time.sleep(2.5)
lyric("over every mistake.",2)
#time.sleep(2)
lyric("You just keep on trying ",2)
#time.sleep(2)
network.say("3")#Science
lyric("till you run out of cake.",2)
#time.sleep(2)
lyric("And the Science gets done.",2)
network.say("1")
#time.sleep(2)
lyric("And you make a neat gun.",2)
#time.sleep(2)
lyric("For the people who are",2)
#time.sleep(2)
lyric("still alive.",2)
time.sleep(5)
#page2
os.system("clear")
#time.sleep(7)
lyric("I'm not even angry.",4)
#time.sleep(4)
lyric("I'm being so sincere right now.",5)
#time.sleep(5)
network.say("6") # Heart
lyric("Even though you broke my heart.",3)
#time.sleep(3)
lyric("And killed me.",3.5)
#time.sleep(3.5)
network.say("4") # Kaboom
lyric("And tore me to pieces.",3.5)
#time.sleep(3.5)
network.say("8") # Fire
lyric("And threw every piece into a fire.",5)
#time.sleep(5)
lyric("As they burned it hurt because",3)
#time.sleep(3)
network.say("7") # Tick
lyric("I was so happy for you!",2.5)
#time.sleep(2.5)
lyric("Now these points of data",2)
#time.sleep(2)
lyric("make a beautiful line",2)
#time.sleep(2)
lyric("And we're out of beta. ",2)
#time.sleep(2) #30
lyric("We're releasing on time.",2)
#time.sleep(2)
network.say("4") # Kaboom
lyric("So I'm GLaD. I got burned.",2)
#time.sleep(2)
network.say("3") # Science
lyric("Think of all the things we learned",1.7)
#time.sleep(1.7)
network.say("1") # Ap
lyric("For the people who are",2)
#time.sleep(2)
lyric("still alive.",2)
time.sleep(2)
#pg3
os.system("clear")
time.sleep(6)
lyric("Go ahead and leave me.",3.8)
#time.sleep(3.8)
lyric("I think I prefer to stay inside.",5)
#time.sleep(5)
lyric("Maybe you'll find someone else",4)
#time.sleep(4)
lyric("to help you.",3.5)
#time.sleep(3.5)
network.say("5") # Mesa
lyric("Maybe Black Mesa,",3)
#time.sleep(3)
lyric("THAT WAS A JOKE. FAT CHANCE.",4.8)
#time.sleep(4.6)
network.say("2") # Cake
lyric("Anyway, this cake is great.",3)
#time.sleep(3)
lyric("It's so delicious and moist.",2.5)
#time.sleep(2.5)
network.say("9")# Glados
lyric("Look at me still talking ",2.5)
#time.sleep(2.5) 
network.say("4")# Radiation
lyric("When there's Science to do.",2.5)
#time.sleep(2.5)
network.say("1") # Ap
lyric("When I look out there,",2)
#time.sleep(2)
lyric("It makes me GLaD I'm not you.",2)
#time.sleep(2)
network.say("3") # Science
lyric("I've experiments to run.",2)
#time.sleep(2)
lyric("There is research to be done.",2)
#time.sleep(2)
network.say("1") # Aperture
lyric("On the people who are",2)
#time.sleep(2)
lyric("still alive.",2)
#time.sleep(2)
os.system("clear")
time.sleep(1)
#pg4
lyric("PS: And believe me I am",1.5)
#time.sleep(1.5)
lyric("still alive.",1.5)
#time.sleep(1.5)
lyric("PPs: I'm doing science and I'm",1.8)
#time.sleep(1.8)
lyric("still alive.",1.8)
#time.sleep(1.8)
lyric("PPPS: I feel FANTASTIC and I'm",1.8)
#time.sleep(1.8)
lyric("still alive.",1.8)
#time.sleep(1.8)
lyric("While you're dying I'll be",1.8)
#time.sleep(1.8)
lyric("still alive.",1.8)
#time.sleep(1.8)
lyric("FINAL THOUGHT PS:",1.8)
#time.sleep(1.8)
lyric("And when you're dead I will be",1.8)
#time.sleep(1.8)
lyric("still alive.",2)
#time.sleep(2)
lyric("STILL ALIVE",1)
#time.sleep(1)
os.system("clear")
network.say("0") # Raspi
while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(10)

