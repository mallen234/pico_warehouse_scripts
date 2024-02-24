import machine
import time
from machine import I2C
from bme280 import BME280

def main():
    # povered with 3.3V 
    i2c = I2C(1,  sda=machine.Pin(2),scl=machine.Pin(3))
    # print(i2c.scan())
    bme = BME280(i2c=i2c, address=0x77)
    try:
        temperature, pressure, humidity = bme.read_compensated_data()
        print("Temperature: {:.2f}°C".format(temperature / 100))
        print("Pressure: {:.2f} hPa".format(pressure / 2560))
        print("Humidity: {:.2f}%".format(humidity / 1024))
    
    except Exception as e:
        print("Error reading data:", str(e))
        
    result_string = f'{{"temperature": {temperature/100}, "pressure": {pressure/2560}, "humidity": {humidity/1024}}}'
    return result_string

if __name__ == "__main__":
    main()
