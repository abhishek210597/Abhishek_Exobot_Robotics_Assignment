from machine import Pin # Import the machine module to interact with hardware components like GPIO pins.
import time # Import the time module to add delays in the code execution.

Led_Alarm = Pin(7, Pin.OUT) # Initialize led Alarm at PIN GP7
pir_sensor = Pin(10, Pin.IN) # Initialize PIR signal PIN at GP10


while True: # infinite loop to get continuous data
   if pir_sensor.value() == 1: # condition of PIR sensors to set led alarm
       print("Motion Detected") # printing detected condition
       Led_Alarm.value(1) # Led Alarm
       time.sleep(0.5) # 500 milli second delay
   else:
       print("No Motion") # printing detected condition
       Led_Alarm.value(0) # Led Alarm
       time.sleep(0.5) # 500 milli second delay
