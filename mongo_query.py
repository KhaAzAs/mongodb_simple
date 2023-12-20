from pymongo import MongoClient
user='root'
password = 'MTMyNDEta2hhaXJp'
host='localhost'

# Create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user, password,host)

# Connect to monggodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# Select the "training" database
db = connection.training

# select the 'python' collection
collection = db.python

# Create a sample document
doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# Insert a sample document
print("Inserting a document into collection")
db.collection.insert_one(doc)

# Query for all documents in 'training' database and 'python' collection
docs = db.collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)

# Close the server connection
connection.close()