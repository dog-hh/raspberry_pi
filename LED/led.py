from machine import Pin
import utime
def led_blink():
    led = Pin(28, Pin.OUT)
    led.low()
    while True:
        led.toggle()
        print("Toggle")
        utime.sleep(1)
led_blink()