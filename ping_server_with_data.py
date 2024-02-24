import fetch
import ConnectToWifi
import read_data_bme as read_data
from utime import sleep


def main():
    ssid = 'THG_Guest'              #Your network name
    ConnectToWifi.connect(ssid,None)
    
    while True:
        new_data = read_data.main()
        print(new_data)
        data = fetch.main(url="http://",body=new_data,method="POST")
        sleep(1)
        print(data)
        

def debugger():
    data = fetch.main(url="https://api.carbonintensity.org.uk/intensity",body = None,method="GET")

    
if __name__ == "__main__":
    main()
