import machine
import time
import dht
from machine import Pin, PWM

# Pin setup
motor_pin1 = Pin(3, Pin.OUT)  # Motor direction pin 1
motor_pin2 = Pin(2, Pin.OUT)  # Motor direction pin 2
pwm = PWM(Pin(4))  # PWM for motor speed
pwm.freq(1000)

encoder_pin = Pin(5, Pin.IN, Pin.PULL_UP)  # Encoder pin
dht_sensor = dht.DHT22(Pin(22))

# PID constants
Kp = 1.0
Ki = 0.1
Kd = 0.05

# Initialize variables
target_position = 0
current_position = 0
last_error = 0
integral = 0

# Interrupt handler for encoder
def encoder_handler(pin):
    global current_position
    current_position += 1  # Adjust based on encoder ticks

encoder_pin.irq(trigger=Pin.IRQ_RISING, handler=encoder_handler)

def set_motor(speed):
    if speed > 0:
        motor_pin1.high()
        motor_pin2.low()
    elif speed < 0:
        motor_pin1.low()
        motor_pin2.high()
    else:
        motor_pin1.low()
        motor_pin2.low()
    pwm.duty_u16(abs(speed))

def pid_control():
    global last_error, integral
    
    error = target_position - current_position
    integral += error
    derivative = error - last_error
    output = Kp * error + Ki * integral + Kd * derivative
    
    set_motor(int(output))
    last_error = error

def update_target_position(temperature):
    global target_position
    if temperature > 25:  # Example threshold
        target_position = 100  # Close blinds
    else:
        target_position = 0  # Open blinds

while True:
    # Read temperature
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    
    # Update target position based on temperature
    update_target_position(temp)
    
    # Run PID control loop
    pid_control()
    
    # Wait 100 ms
    time.sleep(0.1)
