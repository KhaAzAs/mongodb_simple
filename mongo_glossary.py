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

# select the 'mongodb_glossary' collection
collection = db.mongodb_glossary

# Create a documents
doc1 = {"database":"a database contains colllections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form or key value pairs"}

# Insert a sample document
print("Inserting a document into collection")
db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)

# Query for all documents in 'training' database and 'python' collection
docs = db.collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)

# Close the server connection
connection.close()