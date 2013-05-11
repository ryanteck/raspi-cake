#Lyrics.py
#Designed to just echo out the lyrics to the console while in sync with the music.
#Lets start!
import time
from subprocess import Popen
import pygame

file = 'stillalivehq.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

def lyric( str ):
  	"Lyrics printed out through this command should be orange"
	time.sleep(1)
	print "\033[38;5;208m" + str + "\033[0;00m"
	return
lyric("Forms FORM-29827281-12:")
pygame.mixer.music.play()
lyric("This was a triumph.")
time.sleep(1)
lyric("I'm making a note here:")
time.sleep(1)
lyric("HUGE SUCCESS.")
time.sleep(2)
lyric("It's hard to overstate") 
time.sleep(1)
lyric("my satisfaction.")
time.sleep(1)
lyric("Aperture Science")
time.sleep(1)
lyric("We do what we must")
time.sleep(1)
lyric("because we can.")
time.sleep(1)
lyric("For the good of all of us.")
time.sleep(1)
lyric("Except the ones who are dead.")

while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick(10)

