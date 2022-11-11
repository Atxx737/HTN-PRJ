import datetime
import time
import pytz
import uuid
import requests
import json

#import DHTRasp

# main function to call
def main():
#    t,humidity=DHTRasp.sensread(DHTRasp.sensorid)
    tzone = pytz.timezone("Asia/Ho_Chi_Minh")
    url = "http://127.0.0.1:5000/api/sensor"
    
    data = {}
   
    headers = {'Content-Type': 'application/json'}
    payload = {}
    while True:
        data["id"]=str(uuid.uuid4().fields[-1])[:5]
        data["sensor_id"] = "DHT01"
        data["room_id"] = "STR01"
    
        data["temperature"] = '-273'
        data["humidity"] = '0'
        data["date"] = datetime.datetime.now(tzone).strftime("%d-%m-%Y %H:%M:%S")
        payload = json.dumps(data)
        
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        # print(data)
        print("\n")
        time.sleep(5)
    
    
if __name__ == "__main__":
    main()
