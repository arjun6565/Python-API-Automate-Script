import requests
import time
import json
import logging
import random

# Configure logger
logging.basicConfig(filename='api_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_id(base_id):
    random_number = random.randint(100000, 999999)  # Generate a random number between 100000 and 999999
    return f"{base_id}-{random_number}"

def call_api():
    base_id = "177962"  # Base ID
    random_id = generate_random_id(base_id)  # Generate a new random ID
    print(random_id,'random_id')
    url = "http://apid.adfalcon.com/rtb/bid?pid=712"
    payload = {
        "id": random_id,
        "imp": [
            {
                "id": "1",
                "banner": {
                    "w": 320,
                    "h": 50,
                    "format": [
                        {
                            "w": 320,
                            "h": 50
                        }
                    ]
                },
                "bidfloor": 0.9,
                "bidfloorcur": "USD",
                "tagid": "132416635385740185908888_marwen"
            }
        ],
        "app": {
            "id": "177962",
            "name": "Khaleej Times",
            "bundle": "com.khaleejtimes"
        },
        "device": {
            "ua": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
            "ip": "102.177.124.255",
            "geo": {
                "country": "UAE"
            },
            "os": "android",
            "devicetype": 1,
            "ifa": "261aab10-6d1a-22e9-8e05-032b8c2ff362"
        },
        "user": {
            "id": "261ccb10-6d1a-11e9-8e05-032b8c2ff362"
        },
        "at": 2,
        "cur": [
            "USD"
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response,'response testing')
        logging.info("Testing API call...")
        if response.status_code == 204:
            logging.info("No Content")
        else:
            if response.text:  # Check if response is not empty
                data = response.json()
                logging.info(f"Received data: {data}")
            else:
                logging.error("Empty response received")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling API: {e}")

def main():
    while True:
        call_api()
        time.sleep(60)

if __name__ == "__main__":
    main()
