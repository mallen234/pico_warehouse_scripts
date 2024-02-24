import requests
import json

def main(url,body,method):
    # url = 'https://api.carbonintensity.org.uk/intensity'
    
    if method == "POST":
        print(body)
        print("posting")
        response = requests.post(url, json = json.loads(body))
    elif method == "GET":
        print("getting")
        response = requests.get(url)
        
    print(response.status_code)
    print(response.text)
    if (response.status_code >= 200 and response.status_code <= 299):
        return json.loads(response.text)
    else:
        print(f"Error: {response.status_code}")
        
    response.close()
    
if __name__ == "__main__":
    main(None,None,"GET")

