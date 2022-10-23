import os

os.system("clear")
print ("Starting weather system, please wait ...")

import RPi.GPIO as GPIO
import pigpio
import time
import random
import pygame

red = 2
green = 3
blue = 4
pi = pigpio.pi()

def sunrise():
  print("- sunrise")
  bright = 1
  while bright < 256 and GPIO.input(17) == 0:
    pi.set_PWM_dutycycle(red, bright)
    pi.set_PWM_dutycycle(green, bright/4)
    pi.set_PWM_dutycycle(blue, 0)
    bright = bright + 1
    print(".", end="", flush=True)
    time.sleep(1)
  print(" done")

def sunset():
  print("- sunset")
  bright = 255
  redshift = 0
  while bright > 0 and GPIO.input(17) == 0:
    if bright == 32:
      pygame.mixer.music.fadeout(10000)
    pi.set_PWM_dutycycle(red, bright)
    pi.set_PWM_dutycycle(green, bright/(redshift+4))
    pi.set_PWM_dutycycle(blue, 0)
    bright = bright - 1
    redshift = redshift + 0.25
    print(".", end="", flush=True)
    time.sleep(1)
  print(" done")

def daylightsky():
  print("- daylightsky")
  pi.set_PWM_dutycycle(red, 255)
  pi.set_PWM_dutycycle(green, 255/4)
  pi.set_PWM_dutycycle(blue, 0)

def darksky():
  pi.set_PWM_dutycycle(red, 0)
  pi.set_PWM_dutycycle(green, 0)
  pi.set_PWM_dutycycle(blue, 0)

def fullwhite():
  pi.set_PWM_dutycycle(red, 255)
  pi.set_PWM_dutycycle(green, 255)
  pi.set_PWM_dutycycle(blue, 255)

def randomcolour():
  random.seed()
  if random.random() > 0.5:
    redlight = 255
  else:
    redlight = 0
  if random.random() > 0.5:
    greenlight = 255
  else:
    greenlight = 0
  if random.random() > 0.5:
    bluelight = 255
  else:
    bluelight = 0
  pi.set_PWM_dutycycle(red, redlight)
  pi.set_PWM_dutycycle(green, greenlight)
  pi.set_PWM_dutycycle(blue, bluelight)

def buttoncheck():
  while GPIO.input(17) == 1:
    pygame.mixer.music.stop()
    continue

def waitifbusy():
  while pygame.mixer.music.get_busy() == True and GPIO.input(17) == 0:
    continue

def thunder():
  print("- thunder starts")
  pygame.mixer.music.load("thunder.mp3")
  pygame.mixer.music.set_volume(0.4)
  pygame.mixer.music.play()
  random.seed()
  darksky()
  while pygame.mixer.music.get_busy() == True and GPIO.input(17) == 0:
    print(".", end="", flush=True)
    n = random.random() * 15 + 5
    time.sleep(n)
    i = int( random.random() * 2.9 + 1 )
    for x in range(0, i):
      fullwhite()
      n = random.random() * 0.05 + 0.05
      time.sleep(n)
      darksky()
      n = random.random() * 0.3 + 0.1
      time.sleep(n)
      print("+", end="", flush=True)
  print(" done")

def fireworks():
  print("- fireworks start")
  pygame.mixer.music.load("fireworks.mp3")
  pygame.mixer.music.set_volume(0.4)
  pygame.mixer.music.play()
  random.seed()
  darksky()
  time.sleep(5)
  while pygame.mixer.music.get_busy() == True and GPIO.input(17) == 0:
    print(".", end="", flush=True)
    randomcolour()
    n = random.random() * 0.2
    time.sleep(n)
    darksky()
    n = random.random() * 0.6
    time.sleep(n)
  print(" done")

# Start dynamic weather and lighting effects
print("Starting dynamic weather and sound")
pygame.mixer.init()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:

  # Bird song sound with morning sunrise, continues with brid song until done
  print("- birdsong with sunrise")
  pygame.mixer.music.load("dawnchorus.mp3")
  pygame.mixer.music.set_volume(0.25)
  pygame.mixer.music.play()
  sunrise()
  waitifbusy()
  buttoncheck()

  # Church chior sound during full daylight
  print("- choir during daytime")
  pygame.mixer.music.load("churchchoir.mp3")
  pygame.mixer.music.set_volume(0.20)
  pygame.mixer.music.play()
  daylightsky()
  waitifbusy()
  buttoncheck()

  # Birdsong during full daylight
  print("- bridsong during daytime")
  pygame.mixer.music.load("birdsong.mp3")
  pygame.mixer.music.set_volume(0.20)
  pygame.mixer.music.play()
  daylightsky()
  waitifbusy()
  buttoncheck()

  # Church bells during full daylight
  print("- church bells during daytime")
  pygame.mixer.music.load("churchbells.mp3")
  pygame.mixer.music.set_volume(0.20)
  pygame.mixer.music.play()
  daylightsky()
  waitifbusy()
  buttoncheck()

  # Sunset with bird song
  print("- birdsong during sunset")
  pygame.mixer.music.load("birdsong.mp3")
  pygame.mixer.music.set_volume(0.25)
  pygame.mixer.music.play()
  sunset()
  waitifbusy()
  buttoncheck()

  # Start a thunderstorm
  print("- thunderstorm during the night")
  thunder()
  buttoncheck()

  # Start a firework display
  fireworks()
  buttoncheck()

  continue

# End all dynamic weather and lighting
darksky()
print("Ending all dynamic weather and lighting")
pi.stop()

