from .gpio import led_r,led_g, led_b

def led_rgb(pwmr,pwmg,pwmb):
	print("cambia led rgb")
	led_r.ChangeDutyCycle(pwmr)
	led_g.ChangeDutyCycle(pwmg)
	led_b.ChangeDutyCycle(pwmb)
        
def led_start():
        led_r.start(0)
        led_g.start(0)
        led_b.start(0)
        
def gpio_rgb_stop_and_clean():
        led_r.stop()
        led_g.stop()
        led_b.stop()

