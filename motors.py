
import RPi.GPIO as GPIO
import time
import fileinput

GPIO.setmode(GPIO.BCM)

# setup input pins
switchLeftPIN = 27
switchRightPIN = 22
GPIO.setup(switchLeftPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchRightPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setup output pins
sliderPIN = 18 # slider
rotatePIN = 12
vibePIN = 17
GPIO.setup(vibePIN, GPIO.OUT)
GPIO.setup(sliderPIN, GPIO.OUT)
GPIO.setup(rotatePIN, GPIO.OUT)

pwmFreq = 50
slider = GPIO.PWM(sliderPIN, pwmFreq)
rotate = GPIO.PWM(rotatePIN, pwmFreq)
sliderDutyDefault = 6.8


end1, end2 = 3,11

duty = end1
dduty=0.2
sleepTime = 0.5
sliderPosition = 100 

def initialize():
  slider.start(end1)
  rotate.start(end1)
  print('initialized')

def finalize():
  slider.stop()
  GPIO.cleanup()
  print('finalized')
 
def driveSlider(duty):
  duty = float(duty) # try

  print(['slider duty to:', duty])
  slider.ChangeDutyCycle(duty)
  time.sleep(sleepTime)

def vibe():
   GPIO.output(vibePIN, True)
   print 'vibe high'
   time.sleep(0.5)
   GPIO.output(vibePIN, False)
   print 'vibe low'
   time.sleep(0.5)

def rotateTo(duty):
  duty = float(duty) # try

  print(['rotate to', duty])
  if duty<end1:
    print('cancel')
    return
  if duty>end2:
    print('cancel')
    return

  print(['rotate duty to:', duty])
  rotate.ChangeDutyCycle(duty)
  time.sleep(sleepTime)
  vibe()
  time.sleep(sleepTime)


def adjustLeft():
  print('adjusting left')
  status = True
  while(status):
    status = GPIO.input(switchLeftPIN)
    print(status)
    driveSlider(6)
  driveSlider(sliderDutyDefault)
  print('adjusting left')

def adjustRight():
  global sliderPosition
  print('adjusting right')
  status = True
  while(status):
    status = GPIO.input(switchRightPIN)
    print(['switch right', status])
    driveSlider(8)
  sliderPosition = 100
  driveSlider(sliderDutyDefault)
  print('adjusted right')
 
def slideTo(destination):
  global sliderPosition
  print('sliding to', destination)
  print ('sleepTime', sleepTime)
  while(sliderPosition > destination):
    time.sleep(sleepTime)
    sliderPosition -= 10
    print ('sliderPosition', sliderPosition)
    driveSlider(6)
  driveSlider(sliderDutyDefault)
  # driveSlider(6.2)
  # driveSlider(6.4)
  # driveSlider(6.6)
  # driveSlider(6.8)
  # driveSlider(7)
  # driveSlider(7.2)
  # driveSlider(7.4)
  # driveSlider(7.6)
  # driveSlider(7.8)

initialize()
while True:
  print ('sliderPosition', sliderPosition)
  adjustRight()
  print ('sliderPosition', sliderPosition)
  time.sleep(0.1)

  # slideTo(90)
  time.sleep(0.1)

  slideTo(80)
  rotateTo(3.8)
  rotateTo(4.8)
  rotateTo(5.8)
  rotateTo(6.8)
  rotateTo(7.8)
  rotateTo(8.8)
  rotateTo(9.8)
  rotateTo(10.8)
  time.sleep(0.1)

  # slideTo(70)
  time.sleep(0.1)

finalize()

   










