# Model Rail Environment
Code and files for the Model Rail Environment project for the Raspberry Pi

## Overview
I created this project as I wanted a way to enhance my N gauge model railway with ambient sounds and backdrop lighting effects. The project is built around a Raspberry PI model Model B (Version 1). A python program controls the sound and lighting effects to create a sequence of events from sunrise to sunset.

The events play in order and take about 30 mins to complete a full cycle. At present the events, in order, are:
- Bird song sound with morning sunrise
- Church choir sound during full daylight
- Bird song during full daylight
- Church bells during full daylight
- Sunset with bird song 
- Thunderstorm
- Firework display

The sounds are designed for two speakers placed at differing positions on the model railway layout. The two stereo channels are then used allowing each to carry independent sound effects. This is used to play the church sounds from a speaker placed inside the church, using one of the stereo channels.

The lighting effects are achieved by controlling an RGB LED strip that is connected to the GPIO pins via a small control board.

## Schematics
Included are schematics for the LED control board. The board uses 3 IRLZ34N MOSFETs to control the voltage level on each of the red, green and blue supply lines of an LED strip fitted to the backscene.

The schematics were produced in KiCad and a PDF version is also provided.

## Python program
The python program requires the pigpio library to be installed on the host pi. Typically this can be installed with:
```
sudo apt-get install pigpio
```
Once installed the pigpio daemon needs to be running before the python program is started. The pigpio daemon can be started with:
```
sudo pigpiod
```
The python program also needs the following python modules:
- pigpio (may need to be installed with pip, see below)
- pygame (may need to be installed with pop, see below)
- time
- random

Non default modules can usually be installed using the python package manger, pip. For example:
```
pip install pigpio pygame
```
When installed on a Raspberry Pi running OS Lite it may also be necessary to install the libsdl2-mixer-2.0-0 library in order for the pygame module to work successfully. This can be installed with:
```
sudo apt-get install libsdl2-mixer-2.0-0
``` 
## Sounds
The project includes a number of sound files in mp3 format. These were mixed using audacity, primarily to set the stereo balance and make use of the placement of the two speakers on the layout.
