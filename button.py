import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    etat = GPIO.input(27)
    if etat == 0:
        print('Bouton appuyé!')
    else:
        print('Bouton relaché!')

    time.sleep(0.5)