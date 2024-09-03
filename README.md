# Exobot_Robotics_Assignment

</br>
</br>

## Task 1
Task 1 simulation Link: [wokwi Task 1](https://wokwi.com/projects/407986447908575233)

The wiring of a DHT22 sensor connected to a Raspberry Pi Pico. The DHT22 sensor has four pins, with the first pin (Vcc) connected to the 3.3V power (red wire) on the Pico, the second pin (Data) connected to GPIO 6 (green wire) with a pull-up resistor between GND and Data, and the fourth pin connected to GND (black wire). When you press the green play button in your simulation environment (like in a coding platform), it initiates the code that reads the temperature and humidity data from the DHT22 sensor. These readings are then printed on the Serial monitor during the simulation, allowing you to monitor real-time environmental data.
![](/Image/Task_1.png)
</br>
</br>


## Task 2
Task 2 simulation Link: [wokwi Task 2](https://wokwi.com/projects/407985977638854657)


In this task illustrates the connection of an LDR (Light Dependent Resistor) module with an LED and a Raspberry Pi Pico. The LDR module is connected to the Pico with the Vcc pin going to 3.3V (red wire), GND to GND (black wire), and the DO (Digital Output) pin connected to GPIO 12 (purple wire). The LED is connected to GPIO 5 (yellow wire) and GND (black wire). When you start the simulation by pressing the green play button, the LDR will detect the ambient light level. In a dark environment, the LED will turn on. If the light level exceeds 40%, the LED will automatically turn off, simulating a light-sensitive switch.
![](/Image/Task_2.png)
</br>
</br>


## Task 3
Task 3 simulation Link: [wokwi Task 3](https://wokwi.com/projects/407991045957431297)


This image shows the wiring setup for a PIR (Passive Infrared) sensor and an LED connected to a Raspberry Pi Pico. The PIR sensor's Vcc is connected to 3.3V (red wire), GND to GND (black wire), and the output pin (D) to GPIO 10 (green wire) on the Pico. The LED is connected to GPIO 7 (green wire) and GND (black wire). When you start the simulation by pressing the green play button, the PIR sensor will detect motion in its vicinity. If motion is detected, the LED will turn on, and the message "Motion Detected" eles "No Motion" will be printed on the serial monitor, indicating that the sensor has detected movement.
![](/Image/Task_3.png)
</br>
</br>


## Task 4
Task 4 simulation Link: [wokwi Task 4](https://wokwi.com/projects/408004037875964929)
In this circuit:

    1. LDR (Light Dependent Resistor) is connected to GPIO 28 (ADC) on the Raspberry Pi Pico. It measures the ambient light levels. A corresponding LED is connected to GPIO 9, which likely lights up when the LDR senses low light.
    2. The DHT22 sensor is connected to GPIO 13, which reads temperature and humidity data. A pull-up resistor between GND and the data pin ensures stable communication with the Pico.
    3. The PIR sensor, which detects motion, is connected to GPIO 20. A corresponding LED is connected to GPIO 22, which may light up when motion is detected.
    4. An OLED display is connected via the I2C protocol, with the SCL pin connected to GPIO 27 and the SDA pin connected to GPIO 26.
    5. All sensors share the same power source (VCC) and ground (GND) connections, ensuring that the circuit operates correctly from a single power supply.

    It initializes and operates an OLED display, an LDR sensor, a DHT22 sensor, a PIR sensor, and two LEDs. The script reads light levels, temperature, humidity, and motion status from the sensors, displaying the information on the OLED screen. LEDs are triggered based on LDR readings (for light levels) and PIR readings (for motion detection). The program loops continuously, updating the OLED with sensor data and controlling the LEDs accordingly.
    
![](/Image/Task_4.png)
</br>
</br>

## Task 5
Due unavailability of L298N and motor in wokwi I have not simulated in wokwi. But created circuit diagram in doc and written code witch you can fine in Task 5 dectory Note: Both power sources are connected by a common GND.
![](/Image/Task_5.png)
</br>
</br>
