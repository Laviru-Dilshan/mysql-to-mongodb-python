"""
All rights reserved by Laviru Dilshan Jr. 2024

Connect with me:
- GitHub: https://github.com/Laviru-Dilshan
- Twitter: https://x.com/laviru_dilshan
- LinkedIn: https://www.linkedin.com/in/laviru-dilshan
- Facebook: https://www.facebook.com/LaviruD
- Instagram: https://www.instagram.com/lavirudilshan

"""

from sql_connector import connect_to_mysql
from mongo_connector import MongoDBConnector
from dotenv import load_dotenv
import os
load_dotenv()

class MySQLToMongoConverter:
    def __init__(self, sql_config, mongo_uri, mongo_db, collection_name, field_mapping):
        self.sql_config = sql_config
        self.mongo_connector = MongoDBConnector(mongo_uri, mongo_db, collection_name)
        self.field_mapping = field_mapping
        self.collection_name = collection_name  # Add this line

    def convert(self):
        cnx = connect_to_mysql(self.sql_config, attempts=3)

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM {self.collection_name}")
                rows = cursor.fetchall()
                items = []
                for row in rows:
                    item = {}
                    for field, index in self.field_mapping.items():
                        item[field] = row[index]
                    items.append(item)

                for item_data in items:
                    inserted_id = self.mongo_connector.insert_data(item_data)
                    print(f"Data inserted with id: {inserted_id}")

            self.mongo_connector.close_connection()
            cnx.close()
        else:
            print("Could not connect")

# Define your field mappings for each table
province_mapping = {
    "id": 0,
    "district_id": 1,
    "name_en": 2,
    "name_si": 3,
    "name_ta": 4,
    "sub_name_en": 5,
    "sub_name_si": 6,
    "sub_name_ta": 7,
    "postcode": 8,
    "latitude": 9,
    "longitude": 10
}

# Example usage
converter = MySQLToMongoConverter(
    {
        "host": os.getenv('SQL_HOST'),
        "user": os.getenv('SQL_USER'),
        "password": os.getenv('SQL_PASSWORD'),
        "database": os.getenv('SQL_DATABASE'),
    },
    os.getenv('MONGO_URI'),
    os.getenv('MONGO_DATABASE'),
    'cities',
    province_mapping
)
converter.convert()

