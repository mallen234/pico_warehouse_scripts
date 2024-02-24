import time
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
import json
from utime import sleep
import ubinascii

def connect(ssid,password):
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    mac_address = ubinascii.hexlify(wlan.config('mac'), ':').decode()
    print(f'Connected on {wlan.ifconfig()[0]}, MAC Address: {mac_address}')
    
    return ip

def main():
    # load the config file to get Wifi Credentials 
    #with open("config.json") as f:
    #    config = json.load(f)
    #    ssid = config["SSID"]
    #    password = config["PW"]


    # Connect to network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]



    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
       raise RuntimeError('network connection failed')
    else:
      print('connected')
      status = wlan.ifconfig()
      #print('ip = ' + status[0])

    # Example 1. Make a GET request for google.com and print HTML
    # Print the html content from google.com
    print("1. Querying google.com:")
    r = urequests.get("http://www.google.com")
    print(r.content)
    r.close()

    # Example 2.  Let's get the current time from a server
    print("\n\n2. Querying the current GMT+0 time:")
    r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
    print(r.json())

if __name__ == '__main__':
    main()
