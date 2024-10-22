import pymongo
import json
from typing import Any, List, Dict
import os
import pandas as pd
from pymongo import MongoClient

class MongoOperation:
    _collection = None
    _database = None
    
    def __init__(self, client_url: str, database_name: str, collection_name: str = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = self.create_mongo_client()

    def create_mongo_client(self) -> MongoClient:
        """Creates a MongoDB client."""
        return MongoClient(self.client_url)

    def create_database(self):
        """Creates and returns the MongoDB database."""
        if MongoOperation._database is None:
            MongoOperation._database = self.client[self.database_name]
        return MongoOperation._database
    
    def create_collection(self) -> pymongo.collection.Collection:
        """Creates and returns the MongoDB collection."""
        if MongoOperation._collection is None or self.collection_name != MongoOperation._collection.name:
            database = self.create_database()
            MongoOperation._collection = database[self.collection_name]
        return MongoOperation._collection
    
    def insert_record(self, record: Dict[str, Any] | List[Dict[str, Any]]) -> None:
        """Inserts a single or multiple records into the collection."""
        collection = self.create_collection()
        if isinstance(record, list):
            if all(isinstance(data, dict) for data in record):
                collection.insert_many(record)
            else:
                raise TypeError("All items in the record list must be dictionaries.")
        elif isinstance(record, dict):
            collection.insert_one(record)
        else:
            raise TypeError("Record must be either a dictionary or a list of dictionaries.")
    
    def bulk_insert(self, datafile: str) -> None:
        """Inserts multiple records from a CSV or Excel file into the collection."""
        if datafile.endswith('.csv'):
            dataframe = pd.read_csv(datafile, encoding='utf-8')
        elif datafile.endswith('.xlsx'):
            dataframe = pd.read_excel(datafile, encoding='utf-8')
        else:
            raise ValueError("File must be a CSV or Excel file.")

        data_json = json.loads(dataframe.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(data_json)

