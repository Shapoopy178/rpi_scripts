from time import sleep
from picamera import PiCamera
import datetime


camera = PiCamera(resolution=(640,480), framerate=2)
record_time = 5
timestamp = str(datetime)
fname = 'recording.h264'
camera.start_preview()
camera.start_recording(fname, format='h264')
sleep(record_time)
camera.stop_recording()
camera.stop_preview()
