
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
servoPIN = 18 # slider
rotatePIN = 12
vibePIN = 17
GPIO.setup(vibePIN, GPIO.OUT)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(rotatePIN, GPIO.OUT)

while True:
    input_state = GPIO.input(switchRightPIN)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)



# while True:
#   GPIO.output(vibePIN, True)
#   print 'vibe high'
#   time.sleep(0.5)
#   GPIO.output(vibePIN, False)
#   print 'vibe low'
#   time.sleep(0.5)

pwmFreq = 50
servo = GPIO.PWM(servoPIN, pwmFreq)

end1, end2 = 3,11
servo.start(end1)

duty = end1
dduty=0.2
sleepTime = 0.5

def driveServo(duty):
  duty = float(duty) # try

  print(['duty', duty])
  # if duty<end1:
  #   print('cancel')
  #   return
  # if duty>end2:
  #   print('cancel')
  #   return

  print(['setting duty to:', duty])
  servo.ChangeDutyCycle(duty)
  time.sleep(sleepTime)


print('>>>')

while(True):
  for line in fileinput.input():
    duty = line.rstrip()
    driveServo(duty)
    print('>>>')

servo.stop()
GPIO.cleanup()

