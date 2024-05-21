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
    def __init__(self, sql_config, mongo_uri):
        self.sql_config = sql_config
        self.mongo_uri = mongo_uri
        self.mongo_db_name = self.sql_config['database']
        self.mongo_connector = MongoDBConnector(self.mongo_uri, self.mongo_db_name)

    def connect_mysql(self):
        return connect_to_mysql(self.sql_config, attempts=3)

    def get_mysql_table_names(self, cnx):
        with cnx.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
        return tables

    def get_table_columns(self, cnx, table_name):
        with cnx.cursor() as cursor:
            cursor.execute(f"DESCRIBE {table_name}")
            columns = [column[0] for column in cursor.fetchall()]
        return columns

    def convert_table_to_collection(self, cnx, table_name):
        columns = self.get_table_columns(cnx, table_name)
        field_mapping = {column: index for index, column in enumerate(columns)}

        with cnx.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            items = []
            for row in rows:
                item = {}
                for field, index in field_mapping.items():
                    item[field] = row[index]
                items.append(item)

        self.mongo_connector.set_collection(table_name)

        for item_data in items:
            inserted_id = self.mongo_connector.insert_data(item_data)
            print(f"Data inserted into {table_name} with id: {inserted_id}")

    def convert(self):
        cnx = self.connect_mysql()

        if cnx and cnx.is_connected():
            table_names = self.get_mysql_table_names(cnx)

            for table_name in table_names:
                self.convert_table_to_collection(cnx, table_name)

            cnx.close()
            self.mongo_connector.close_connection()
        else:
            print("Could not connect")

# Example usage
sql_config = {
    "host": os.getenv('SQL_HOST'),
    "user": os.getenv('SQL_USER'),
    "password": os.getenv('SQL_PASSWORD'),
    "database": os.getenv('SQL_DATABASE'),
}

mongo_uri = os.getenv('MONGO_URI')

converter = MySQLToMongoConverter(sql_config, mongo_uri)
converter.convert()
