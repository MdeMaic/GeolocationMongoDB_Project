import json
import requests
from IPython.display import Image
import os
from dotenv import load_dotenv

#COMANDO PARA OBTENER EL TOKEN del .env
#Si está en diferentes carpetas, dentro del paréntesis crear la estructura "../../"
load_dotenv()

#estraer tokens
tokenID = os.getenv("CLIENT_ID")
tokenSCRT = os.getenv("CLIENT_SECRET")

#Para ver que hay cerca
def exploreForesquare (query,limit,distance,latitude=40.7243,longitude=-74.0018,):
    
    #configurar url y parámetros token
    url = 'https://api.foursquare.com/v2/venues/explore'
    tokenID = os.getenv("CLIENT_ID")
    tokenSCRT = os.getenv("CLIENT_SECRET")
    if not tokenID or not tokenSCRT:
        raise ValueError("Auth Fail. Check process please")

    #configurar parámetros de requests.
    params = dict(
    client_id=tokenID,
    client_secret=tokenSCRT,
    v='20180323',
    ll=f'{latitude},{longitude}',
    # Para especificar el nombre del sitio buscado
    query=query,
    limit=limit,
    radius=distance
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data
