from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf, sys, time
import dht

pix_res_x = 128
pix_res_y = 64

def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev

def display_anima(oled, ldr, led, dht_sensor, pir_sensor, led_alarm):
   

    while True:
        
        ldr_value = ldr.read_u16()
        light_percentage = (ldr_value / 65535) * 100
        print(ldr_value)
        # Control LED based on LDR value (threshold can be adjusted)
        if ldr_value > 50000:
            led.on()
        else:
            led.off()

        try:
            dht_sensor.measure()
            temperature_celsius = dht_sensor.temperature()
            humidity_percent = dht_sensor.humidity()
        except Exception as e:
            print("Error reading DHT22:", str(e))
            temperature_celsius = humidity_percent = 0.0
        
        motion_status = "No Motion"
        if pir_sensor.value() == 1:
            motion_status = "Motion Detected"
            led_alarm.value(1)
        else:
            led_alarm.value(0)

        # Clear the specific lines by drawing a filled black rectangle
        oled.fill_rect(5, 5, oled.width - 5, 55, 0)


        oled.text("LDR: {:.1f}%".format(light_percentage), 5, 5)
        oled.text("Temp: {:.2f}C".format(temperature_celsius), 5, 20)
        oled.text("Hum: {:.2f}%".format(humidity_percent), 5, 30)
        oled.text(motion_status, 5, 50)
        oled.show()
        time.sleep(2)

def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    
    ldr = ADC(Pin(28))  # Initialize LDR on GP26 (ADC0)
    led = Pin(9, Pin.OUT)  # Initialize LED on GP5
    
    dht_pin = Pin(13)
    dht_sensor = dht.DHT22(dht_pin)

    pir_sensor = Pin(20, Pin.IN)  # PIR sensor on GP10
    led_alarm = Pin(22, Pin.OUT)   # Alarm LED on GP7
    
    display_anima(oled, ldr, led, dht_sensor, pir_sensor, led_alarm)

if __name__ == '__main__':
    main()
