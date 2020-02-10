import pandas as pd
from pymongo import MongoClient


client = MongoClient()
def connectMongoColl(database, collection):
    client = MongoClient(f"mongodb://localhost/{collection}")
    db = client.get_database()
    coll = db[collection]
    return db, coll


#NOT WORKING, CHECK MÁS TARDE
'''
def getMongodb(collection,query,columns):
    if query == "all":
        query = '{}'
    filt = []
    for i in columns:
        filt.append(i,":1,")
    filt_d = dict(filt)
    client = MongoClient(f"mongodb://localhost/{collection}")
    db = client.get_database()
    companies = list(db[f'{collection}'].find({f'{query}'},filt_d))
    df = pd.DataFrame(companies)
    return df

lst = ['name','office','category_code']
df = getMongodb("companies","all",lst)
df.head()
'''