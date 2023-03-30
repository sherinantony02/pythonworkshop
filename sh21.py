import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
print("connected")
print(client.list_database_names())
db=client["record"]
col=db["class"]
user=[{
   "name":"Sherin",
   "age":21,
   "adm":13
},{
  "name":"Abin",
  "age":24,
  "adm":14
}]

#col.insert_one(})
#print(col.find_one())
for doc in col.find({"name":{"$regex":"^A"}}):
	print(doc)
