'''
from bson.objectid import ObjectId
from bson.son import SON
from pprint import pprint
from pymongo import MongoClient

class MongoDbSampleScript():
    def __init__(self):
        self.host   = "localhost"
        self.port   = 27017
        self.client = MongoClient(self.host, self.port)

        self.database   = self.client.bookstore # dun know how to solve this problem
        self.collection = self.database.books   # dun know how to solve this problem

    """
    # Initialize client for MongoDB
    def initialize_mongo_db(self):
        host = self.host
        port = self.port

        client = MongoClient(host, port)

        return client
        
    # List all the databases
    def list_all_db_names(self):
        db_names = client.list_database_names()

        return db_names

    # Initialize single database
    def initialize_single_db(self):
        client = self.client

        database   = client.database
        # collection = database.collection

        return database, collection

    # List all the collections
    def list_all_collections(self):
        database = self.database

        collections = database.list_collection_names()

        return collections

    # Initialize single database and collections
    def initialize_single_db_and_collection(self):
        database   = client.database
        collection = database.collection
        
        neuraldb = client.neuraldb
        people   = neuraldb.people
        
        return database, collection
        """

    # Insert one document into collection
    def insert_one_document_into_collection(self):
        collection = self.collection

        test_document = {
            "name" : "Mike",
            "age"  : 30
        }

        collection.insert_one(test_document) # sample_db = neuraldb, sample_collection = people

        test_document = {
            "name"     : "Lisa",
            "age"      : 20,
            "interest" : ["C++", "Python", "Piano"]
        }

        collection.insert_one(test_document)

    # Get id of the inserted document
    def get_id_of_the_inserted_document(self):
        collection = self.collection

        test_document = {
            "name" : "Mike",
            "age"  : 30
        }

        mike_id = collection.insert_one(test_document).inserted_id

        return mike_id

    # Get all the documents in the collection
    def get_all_documents(self):
        collection = self.collection

        data_cursor = collection.find() # pymongo cursor object instead of list

        return data_cursor

    # Get all the documents fulfilling the condition in the collection
    def get_all_documents_fulfilling(self):
        data_cursor = people.find({"name": "Mike"})
        # data_list = people.find({"_id": ObjectId("651d346df022ea0c77c928a5")})
        # data_list = people.find({"age": {"$lt": 25}})

        return data_cursor

    # Count the documents fulfilling the condition in the collection
    def count_documents_fulfilling(self):
        count = people.count_documents({"name": "Mike"})

        return count

    # Update one document in the collection
    def update_one_document_into_collection(self):
        collection = self.collection

        collection.update_one({"_id": ObjectId("651d3474d1589584bb13a5a3")}, {"$set": {"age": 27}})

        # Delete multiple documents in the collection
        # collection.delete_many({"age": {"$lt": 37}})

        pipeline = [
            {
                "$group": {
                    "_id"        : "$name",
                    "averageAge" : {"$avg": "$age"}
                }
            },
            {
              "$sort": SON([("averageAge", -1), ("_id", -1)])
            }
        ]

        results = people.aggregate(pipeline)

        for result in results:
            print(result)

def main():
    mongo_db = MongoDbSampleScript()

    data_list   = []
    data_cursor = mongo_db.get_all_documents()

    for data in data_cursor:
        data_list.append(data)

    pprint(data_list)

if __name__ == "__main__":
    main()

'''