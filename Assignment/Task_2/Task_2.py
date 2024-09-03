from machine import Pin # Import the machine module to interact with hardware components like GPIO pins.
import time ## Import the time module to add delays in the code execution.
 
led = Pin(5, Pin.OUT) # Initialize led at PIN GP5
ldr = Pin(12, Pin.IN, Pin.PULL_DOWN) ## Initialize LDR at PIN GP12
 
while True: # infinite loop to get continuous
    if ldr.value(): # condition of LDR to give command to the LED
        led.value(1) 
        time.sleep(1) #  delay of 1 sec
    else:
        led.value(0)
        time.sleep(1) #   delay of 1 sec
