#Lyrics.py
#Designed to just echo out the lyrics to the console while in sync with the music.
#Lets start!
import time

def lyric( str ):
  	"Lyrics printed out through this command should be orange"
	time.sleep(1)
	print "\033[38;5;208m" + str + "\033[0;00m"
	return

lyric("Forms FORM-29827281-12:")
lyric("T")
lyric("e")
