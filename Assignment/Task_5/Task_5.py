import machine
import time
import dht
from machine import Pin, PWM

# Pin setup for motor control
motor_pin1 = Pin(3, Pin.OUT)  # Motor direction pin 1
motor_pin2 = Pin(2, Pin.OUT)  # Motor direction pin 2
pwm = PWM(Pin(4))  # PWM for motor speed
pwm.freq(1000)

# Pin setup for encoder
clk = Pin(19, Pin.IN, Pin.PULL_UP)
dt = Pin(20, Pin.IN, Pin.PULL_UP)

# Pin setup for temperature sensor
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
last_clk_value = clk.value()

# Motor control function
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
    pwm.duty_u16(abs(int(speed * 65535 / 100)))

# PID control function
def pid_control():
    global last_error, integral
    
    error = target_position - current_position
    integral += error
    derivative = error - last_error
    output = Kp * error + Ki * integral + Kd * derivative
    
    set_motor(output)
    last_error = error

# Update target position based on temperature
def update_target_position(temperature):
    global target_position
    if temperature > 25:  # Example threshold
        target_position = 100  # Close blinds
    else:
        target_position = 0  # Open blinds

# Encoder reading function
def read_encoder():
    global current_position, last_clk_value
    
    clk_value = clk.value()
    dt_value = dt.value()
    
    if clk_value != last_clk_value:
        if dt_value != clk_value:
            current_position += 1  # Clockwise
        else:
            current_position -= 1  # Counter-clockwise
    
    last_clk_value = clk_value

# Main loop
while True:
    # Read temperature
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    
    # Update target position based on temperature
    update_target_position(temp)
    
    # Read encoder
    read_encoder()
    
    # Run PID control loop
    pid_control()
    
    # Wait 100 ms
    time.sleep(0.1)
