import time
import requests

count = 0
urls = ['https://edwardize.blogspot.com/'] 

while count < 100:
    for url in urls:
        response = requests.get(url)
        print(f"Visited {url}, Status Code: {response.status_code}")
        time.sleep(10)  # Waits for 10 seconds before visiting the next URL
        count += 1
