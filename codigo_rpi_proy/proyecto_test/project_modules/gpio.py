import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(16,GPIO.OUT)#led R
GPIO.setup(20,GPIO.OUT)#led G
GPIO.setup(21,GPIO.OUT)#led B

led_r=GPIO.PWM(16,100)#pin,frecuencia
led_g=GPIO.PWM(20,100)
led_b=GPIO.PWM(21,100)
