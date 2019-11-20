import alsaaudio
import sys
import time

mix = alsaaudio.Mixer()
vol = mix.getvolume()

while True:
	for n in range(10, 101, 1):
		mix.setvolume(n, 0)
		mix.setvolume(100 - n, 1)
		time.sleep(0.1)
	for n in range(100, 10, -1):
		mix.setvolume(n, 0)
		mix.setvolume(100 - n, 1)
		time.sleep(0.2)
