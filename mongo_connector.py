from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self, uri, db_name, collection_name=None):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name] if collection_name else None

    def set_collection(self, collection_name):
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        if self.collection is not None:
            result = self.collection.insert_one(data)
            return result.inserted_id
        else:
            raise ValueError("Collection is not set")

    def find_data(self, query):
        if self.collection is not None:
            return self.collection.find(query)
        else:
            raise ValueError("Collection is not set")

    def update_data(self, query, new_data):
        if self.collection is not None:
            result = self.collection.update_one(query, {'$set': new_data})
            return result.modified_count
        else:
            raise ValueError("Collection is not set")

    def delete_data(self, query):
        if self.collection is not None:
            result = self.collection.delete_one(query)
            return result.deleted_count
        else:
            raise ValueError("Collection is not set")

    def close_connection(self):
        self.client.close()
