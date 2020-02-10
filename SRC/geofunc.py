import requests
import math

#geoCode | Requests a geocode.xyz devolviendo en formato geoindex.
def geoCode(address):
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data['longt']),float(data['latt'])]
    }


#withGeoQuery | Genera una Query $near en pymongo
# https://docs.mongodb.com/manual/reference/operator/query/near/
def withGeoQuery(location,maxDistance=10000,minDistance=0,field="location"):
    return {
       field: {
         "$near": {
           "$geometry": location if type(location)==dict else geoCode(location),
           "$maxDistance": maxDistance,
           "$minDistance": minDistance
         }
       }
    }


#asGeoJSON | Create a geoindex with the latitude and longitude inputs.
def asGeoJSON(lat,lng):
    try:
        #Convierte a float (originalmente son numpy.float64)
        lat = float(lat)
        lng = float(lng)
        #Si el valor es NaN, convierte localización en None (null en lenguaje Mongodb)
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        #print("Invalid data")
        return None
