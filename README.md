# 🎆🚀 Unified Database Connector Package 🎆

## Overview  ..

**DB Crud Automated** is a powerful tool designed to simplify and automate database operations, especially for MongoDB. This library enables developers to connect to a MongoDB database effortlessly and perform Create, Read, Update, and Delete (CRUD) operations with minimal setup and code. Database Automator is built to streamline database interactions and boost productivity for developers working with databases.

## Goal

The primary goal of Database Automator is to automate functionalities for connecting to MongoDB and executing CRUD operations efficiently. The library offers a user-friendly interface that abstracts the complexities of database interactions, making development smoother and more accessible.

### 🎇 Future Improvements 🎇

- Support for additional databases, including **MySQL**, **Cassandra**, and others.
- Enhanced error handling and logging features.
- Expanded documentation and examples coming soon.


## Installation

To install Database Automator, you can use pip. Run the following command in your terminal:

```bash
pip install db-crud-automated
```

## Features

- ✅ **Easy Connection:** Simplifies the process of connecting to MongoDB.
- 🔄 **CRUD Operations:** Provides straightforward methods to perform Create, Read, Update, and Delete operations.
- 🌱 **Extensibility:** Future support for other databases such as MySQL and Cassandra.

## Usage

Here’s a quick example of how to use the `mongo_operation` class to connect to a MongoDB database and perform CRUD operations:

### Example

```bash
from mongodb_connect.mongo_crud import mongo_operation

# Initialize the MongoDB operation class
mongo_client = mongo_operation(client_url='your_mongodb_uri', 
                               database_name='your_database_name', 
                               collection_name='your_collection_name')

# Create a new record
record = {'name': 'John Doe', 'age': 30}
mongo_client.insert_record(record, collection_name='your_collection_name')

# Bulk insert records from a CSV file
mongo_client.bulk_insert('path_to_your_file.csv', collection_name='your_collection_name')

# You can also use a list of records for insertion
records_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 28}
]
mongo_client.insert_record(records_list, collection_name='your_collection_name')
```

## 🎉 Contributing 🎉

🤝 Contributions are welcome! If you have suggestions or improvements, please [open an issue](https://github.com/shaheennabi/Unified-Database-Connector-Package/issues) or submit a pull request.

---

## 🎆 License 🎆

📝 This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## ✉️ Contact ✉️

📧 For questions or support, feel free to reach out via email at [mailmessage30@gmail.com](mailto:mailmessage30@gmail.com).

---

### 🚀✨ Package or Repo will be updated soon ✨🚀

