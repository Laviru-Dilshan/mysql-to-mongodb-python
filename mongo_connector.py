from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def find_data(self, query):
        return self.collection.find(query)

    def update_data(self, query, new_data):
        result = self.collection.update_one(query, {'$set': new_data})
        return result.modified_count

    def delete_data(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

    def close_connection(self):
        self.client.close()

# # Example usage
# connector = MongoDBConnector('mongodb://localhost:27017/', 'your_database_name', 'your_collection_name')

# data = {
#     'name': 'Jane Doe',
#     'age': 25,
#     'email': 'janedoe@example.com'
# }

# # Insert data
# inserted_id = connector.insert_data(data)
# print(f"Data inserted with id: {inserted_id}")

# # Find data
# query = {'name': 'Jane Doe'}
# result = connector.find_data(query)
# for doc in result:
#     print(doc)

# # Update data
# query = {'name': 'Jane Doe'}
# new_data = {'age': 26}
# modified_count = connector.update_data(query, new_data)
# print(f"Modified {modified_count} document(s)")

# # Delete data
# delete_query = {'name': 'Jane Doe'}
# deleted_count = connector.delete_data(delete_query)
# print(f"Deleted {deleted_count} document(s)")

# # Close connection
# connector.close_connection()
