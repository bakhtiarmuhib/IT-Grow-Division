import pymongo
from bson import ObjectId

connection_string = "mongodb://localhost:27017"

try:
    client = pymongo.MongoClient(connection_string)
except Exception:
    print("Error:" + Exception)

database =  client["user_info"]

user_collection = database["user"]

user_doc = {
    "name" : "Md. Bakhtiar Muhib",
    "email": "muhibanik1@gmail.com",
    "phone" : "01304194712"
}

# create Data
res = user_collection.insert_one(user_doc)
print(res.inserted_id)
print(res)

# Read Data

user_date = user_collection.find_one({"_id" : ObjectId("6555a5ec387ba9d4272d896b")})
print(user_date)

# update data

user_collection.update_one({"_id" : ObjectId("6555a5ec387ba9d4272d896b")},{"$set":{"phone" : "+8801304194712"}})

user_date = user_collection.find_one({"_id" : ObjectId("6555a5ec387ba9d4272d896b")})
print("After Updating:",user_date)

# delete data

user_collection.delete_one({"_id" : ObjectId("6555a5ec387ba9d4272d896b")})

user_date = user_collection.find_one({"_id" : ObjectId("6555a5ec387ba9d4272d896b")})
print("After deleting",user_date)