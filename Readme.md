# MySQL to MongoDB Data Converter

This Python script allows you to convert data from a MySQL database to a MongoDB database. It retrieves data from a specified table in MySQL and inserts it into a specified collection in MongoDB, based on a mapping of fields between the two databases.

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

4. **Open `main.py` and add your data mapping and collection name:**

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

5. **Run the script:**

    ```bash
    python main.py
    ```

