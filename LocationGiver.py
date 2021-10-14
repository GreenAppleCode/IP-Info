import json
import requests

def ip():
    url = requests.get("https://freegeoip.app/json/")
    json_url = url.json()
    print("Country Name: " + json_url["country_name"])
    print("State Name: " + json_url["region_name"])
    print("City Name: " + json_url["city"])
    print("Zip Code: " + json_url["zip_code"])
    print("Latitude: " + str(json_url["latitude"]))
    print("Longitude: " + str(json_url["longitude"]))
ip()