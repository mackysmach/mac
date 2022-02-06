from unittest import result
from pymongo import MongoClient
client = MongoClient('mongodb://localhost',27017)

db = client["mackydatabase"]
menu_collection = db["user"]

mylist= client.list_database_names()

#print(mylist)

orange ={
    "name" : "Orange",
    "price" : 40
}
banana = {
    "name" : "Banana",
    "price" : 50
}

#fruit_list=[]
#fruit_list.append(orange)
#fruit_list.append(banana)
#x=menu_collection.insert_many(fruit_list)
#print(x.inserted_ids)
#menu_collection.insert_one(orange)

# result = menu_collection.find({},{"_id": 0 , "name" : 1, "price": 1})
# for i in result:
#     print(i)

 #query = {"name":"Orange"}
# result = menu_collection.find(query)
# for i in result:
#     print(i)
# results = menu_collection.find_one(query)
# print(results)

# query = {"price": {"$gte":40}}
# result= menu_collection.find(query)
# for i in result:
#     print(i)

# query = {"name" : "chicken"}
# menu_collection.delete_many(query)
# menu_collection.delete_one(query)

# query = {"name": "Apple"}
# newvalue = {"$set":{"price" : 100}}
# menu_collection.update_one(query,newvalue)
# menu_collection.update_many(query,newvalue)

