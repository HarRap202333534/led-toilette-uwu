import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

compteur = 0

while True:
    etat = GPIO.input(27)
    while etat == 0:
        time.sleep(1)
        etat = GPIO.input(27)
        compteur +=1
        print(compteur)
    
    if compteur <= 2 and compteur >= 1:
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)
    elif compteur <= 4 and compteur >= 3:
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
    elif compteur >= 5:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(17,GPIO.LOW)

    compteur = 0