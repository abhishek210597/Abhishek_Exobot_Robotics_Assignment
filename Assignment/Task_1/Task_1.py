import machine  # Import the machine module to interact with hardware components like GPIO pins.
import dht      # Import the dht module to work with DHT11 or DHT22 sensors.
import time     # Import the time module to add delays in the code execution.

dht_pin = machine.Pin(6)  # Initialize GPIO pin 6

dht_sensor = dht.DHT22(dht_pin)  # Create a DHT22 sensor object using the initialized pin.

while True:  # Start an infinite loop to continuously read data from the sensor.
    try:
        dht_sensor.measure()  # Trigger the sensor to take a measurement (temperature and humidity).

        temperature_celsius = dht_sensor.temperature()  # Get the temperature reading in Celsius.
        humidity_percent = dht_sensor.humidity()        # Get the humidity reading as a percentage.

        print("Temperature: {:.2f}°C".format(temperature_celsius),  # Print the temperature
              "Humidity: {:.2f}%".format(humidity_percent))         # Print the humidity

    except Exception as e:  # Catch any errors that occur during the sensor reading process.
        print("Error reading DHT22:", str(e))  # Print an error message if an exception occurs.

    time.sleep(2)  #2 seconds deley
