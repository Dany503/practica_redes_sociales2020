#!/usr/bin/python
# importamos el modulo de GPIO
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD) # definimos la numeracion 
GPIO.setup(7, GPIO.OUT) # definimos el pin como salida
#GPIO.output(7, GPIO.LOW) # ponemos a 0 el pin
GPIO.output(7, GPIO.HIGH) # ponemos a 0 el pin



    
        






