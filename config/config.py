import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://deffjob:DAFFA0105@d3ffnet99.cxqex.mongodb.net/?appName=D3ffNet99"
)

db = client.get_database("FastAPIDB")


def get_db_connection() : 
    return db
