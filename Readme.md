# MySQL to MongoDB Data Converter

This Python script allows you to convert data from a MySQL database to a MongoDB database.

## Getting Started

1. **Clone the project repository:**

    ```bash
    git clone https://github.com/Laviru-Dilshan/mysql-to-mongodb-python.git
    cd mysql-to-mongodb-python
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file in the project directory and add your environment variables:**

    ```
    SQL_HOST=your_sql_host
    SQL_USER=your_sql_user
    SQL_PASSWORD=your_sql_password
    SQL_DATABASE=your_sql_database
    MONGO_URI=your_mongo_uri
    MONGO_DATABASE=your_mongo_database
    ```

    (important: after add mongo uri add '/', example - "www.mongodb.com/")

## Convert MySQL Database To MongoDB

Using This You Can Convert Your Full MYSQL Database To MongoDB

1. **Open `mysql_to_mongo.py` and add your sql config ,mongo uri and call functions:**

    ```python
    # Create MYSQL Config
    sql_config = {
        "host": os.getenv('SQL_HOST'),
        "user": os.getenv('SQL_USER'),
        "password": os.getenv('SQL_PASSWORD'),
        "database": os.getenv('SQL_DATABASE'),
    }

    #add mondo db uri
    mongo_uri = os.getenv('MONGO_URI')

    # call functions
    converter = MySQLToMongoConverter(sql_config, mongo_uri)
    converter.convert()
    ```

2. **Run the script:**

    ```bash
    python mysql_to_mongo.py
    ```


## Convert MySql Single Table To Single Mongo Collection

It retrieves data from a specified table in MySQL and inserts it into a specified collection in MongoDB, based on a mapping of fields between the two databases.


1. **Open `table_to_collection.py` and add your data mapping and collection name:**

    ```python
    # Define your field mappings for each table
    province_mapping = {
        "id": 0,
        "name_en": 1,
        "name_si": 2,
        "name_ta": 3,
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
        'provinces',
        province_mapping
    )
    converter.convert()
    ```

2. **Run the script:**

    ```bash
    python table_to_collection.py
    ```

# COPYRIGHT

All rights reserved by Laviru Dilshan Jr. 2024

Connect with me:
- GitHub: [https://github.com/Laviru-Dilshan](https://github.com/Laviru-Dilshan)
- Twitter: [https://x.com/laviru_dilshan](https://x.com/laviru_dilshan)
- LinkedIn: [https://www.linkedin.com/in/laviru-dilshan](https://www.linkedin.com/in/laviru-dilshan)
- Facebook: [https://www.facebook.com/LaviruD](https://www.facebook.com/LaviruD)
- Instagram: [https://www.instagram.com/lavirudilshan](https://www.instagram.com/lavirudilshan)
