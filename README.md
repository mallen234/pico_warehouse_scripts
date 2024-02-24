# Code to read data from raspberry pi pico w and send to webserver on VM

All code is written in microPython so for testing and debugging be aware

## fetch

Takes a REST command, body and url. Although, it currently only has functionaltiy for POST and GET. It should return the JSON or simply print an error to the terminal

## ConnectToWifi

Does as expected. Currently the connect function works well and should be used

## read_data_bme

This connects to the raspberry pi and reads the temperature data
The following lines (8,9) can be fiddly and you should try different pins if it is giving and IO ERROR
Use the print(i2c.scan()) to make sure the address matches - it will be need to be converted to hex

```
i2c = I2C(1,  sda=machine.Pin(2),scl=machine.Pin(3))
bme = BME280(i2c=i2c, address=0x77)
```

## ping_server_with_data

This collates all the other pieces of code together. It should
