import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#Mendefinisikan pin output
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#Mendefinisikan pin input
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
while True:
    i=GPIO.input(2)
    j=GPIO.input(3)
    if i==1 and j==0:
        GPIO.output(14,1)  # led merah nyala
        GPIO.output(15,1)  # led kuning nyala
        GPIO.output(23,0) # led hijau mati
        GPIO.output(24,0) # led biru mati
    elif i==0 and j==1:
        GPIO.output(14,0) # led merah mati
        GPIO.output(15,0) # led kuning mati
        GPIO.output(23,1)  # led hijau nyala
        GPIO.output(24,1)  # led biru nyala
    elif i==1 and j==1:
        GPIO.output(14,1)  # led merah nyala
        GPIO.output(15,1)  # led kuning nyala
        GPIO.output(23,1)  # led hijau nyala
        GPIO.output(24,1)  # led biru nyala
    else:
        GPIO.output(14,0)  # led merah mati
        GPIO.output(15,0)  # led kuning mati
        GPIO.output(23,0)  # led hijau mati
        GPIO.output(24,0)  # led biru mati
