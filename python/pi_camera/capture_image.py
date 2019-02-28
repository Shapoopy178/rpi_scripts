from time import sleep
from picamera import PiCamera
import datetime

camera = PiCamera()
camera.resolution = (2592,1944)
camera.start_preview()
#pause for camera warm-up
sleep(2)
timestamp = str(datetime.datetime.now())
fname = timestamp+'.jpg'
camera.capture(fname)
