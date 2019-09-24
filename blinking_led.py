import RPi.GPIO as GPIO
import time
#Mendefinisikan pin output
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(14,True)   # led merah nyala
    GPIO.output(15,True)   # led kuning nyala
    GPIO.output(23,False) # led hijau mati
    GPIO.output(24,False) # led biru mati
    time.sleep(1) #Selama 1 detik
    GPIO.output(14,False)  # led merah mati
    GPIO.output(15,False)  # led kuning mati
    GPIO.output(23,True)  # led hijau nyala
    GPIO.output(24,True)  # led biru nyala
    time.sleep(1) #Selama 1 detik
