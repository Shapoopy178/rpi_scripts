from time import sleep
from picamera import PiCamera
import datetime


camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 40
record_time = 30
timestamp = str(datetime)
fname = 'recording.h264'
camera.start_preview()
camera.start_recording(fname, format='h264')
sleep(30)
camera.stop_recording()
camera.stop_preview()
