import pymongo 

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["survey"]

mydict = { "thumbnail": "photo.jpg", "description": "Best area and Land",  "location": "Ahmedabad", "date": "25-08-2000"}

x = mycol.insert_one(mydict)

print(x.inserted_id)