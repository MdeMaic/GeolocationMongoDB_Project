import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getLocation(radius=1500,lat=37.772323,lng=-122.214897,place="school",keyword="school"):
    authToken = os.getenv("API_KEY")
    params=f"location={lat},{lng}&radius={radius}&type={place}&&keyword={keyword}"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?{params}&key={authToken}"
    
    res = requests.get(url)
    return res.json()

