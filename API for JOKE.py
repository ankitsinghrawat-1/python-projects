import requests 
import time

url = 'https://official-joke-api.appspot.com/random_joke'


response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print(f"Setup: {joke['setup']}")
    time.sleep(5)
    print(f"punchline: {joke['punchline']}")
else:
    print("Failed to retrieve a joke. Please try again later.")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

