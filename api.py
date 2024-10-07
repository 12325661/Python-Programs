import requests
import json 
 
# URL of the JSON file 
url = "https://api.example.com/data.json" 
 
# Send a GET request to the URL 
response = requests.get(url) 
 
# Check if the request was successful (status code 200) 
if response.status_code == 200: 
    # Parse the JSON content 
    data = response.json()  # or json.loads(response.text) 
     
    # Print the JSON data 
    print(data) 
else: 
    print(f"Failed to retrieve data: {response.status_code}")