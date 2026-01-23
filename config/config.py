from dotenv import load_dotenv, find_dotenv
import os 
import pymongo

load_dotenv(find_dotenv())
mongo_db = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(mongo_db)

db = client.get_database("FastAPIDB")

def get_db_connection() : 
    return db
