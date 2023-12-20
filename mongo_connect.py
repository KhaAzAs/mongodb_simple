from pymongo import MongoClient
user='root'
password = 'MTMyNDEta2hhaXJp'
host='localhost'

# Create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user, password,host)

# Connect to monggodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# Get database list
print("Getting list of database")
dbs = connection.list_database_names()

# Print the database names
for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")

# Close the server connection
connection.close()