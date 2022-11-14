import datetime
import time
import pytz
import random
import requests
import json

#import DHTRasp

# main function to call
def main():
#    t,humidity=DHTRasp.sensread(DHTRasp.sensorid)
    tzone = pytz.timezone("Asia/Ho_Chi_Minh")
    url = "http://127.0.0.1/api/sensor"
    
    data = {}
    room_id=['STR01','STR02','DRY01','DAI02','CTL01']

    headers = {'Content-Type': 'application/json'}
    payload = {}
    while True:
        data["sensor_id"] = "DHT01"
        data["room_id"] = random.choice(room_id)
    
        data["temperature"] = random.choice(range(0, 90))
        data["humidity"] = random.choice(range(10, 100))
        data["date"] = datetime.datetime.now(tzone).strftime("%Y-%m-%d %H:%M:%S")
        payload = json.dumps(data)
        
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        # print(data)
        print("\n")
        time.sleep(5)
    
    
if __name__ == "__main__":
    main()
