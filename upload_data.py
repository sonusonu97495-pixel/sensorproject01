from  pymongo.mongo_client import MongoClient
import pandas as pd
import json

# URL
url = 'mongodb+srv://sonusonu97495_db_user:Myntra_Cloud0918@cluster0.img2grq.mongodb.net/'

# Create new client and connevct to server
client = MongoClient(url)

# create database name and collection name
DATABASE_NAME = 'pwskills'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv('C:\Users\sonus\Downloads\sensor_project\notebooks\wafer_23012020_041211.csv')

df = df.drop('Unnamed: 0', axis = 1)

# Pandas DataFrame ke data ko JSON format se Python dictionaries ki list mein convert karna
json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

