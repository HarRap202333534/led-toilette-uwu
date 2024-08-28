import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

continuer = True

while continuer:
    choix = input("tapez 1 pour ouvrir la led ou 2 pour fermer")
    if choix == '1':
        GPIO.output(17,GPIO.HIGH)
        print("Lumiere allumer")
    elif choix == '2':
        GPIO.output(17,GPIO.LOW)
        print("Lumiere eteinte")
    else :
        continuer = False
