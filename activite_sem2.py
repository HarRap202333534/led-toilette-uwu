import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

continuer = True

while continuer:
choix = input("tapez 1 pour rouge la led ou 2 pour bleu")
    if choix == '1':
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
        print("Lumiere Rouge")
    elif choix == '2':
        GPIO.output(17,GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
        print("Lumiere Bleu")
    else :
        GPIO.output(26, GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        continuer = False
