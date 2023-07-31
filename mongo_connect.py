from streamlit.connections import ExperimentalBaseConnection
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

class MongoConnection(ExperimentalBaseConnection[pymongo.MongoClient]):
    def __init__(self, db_name:str, collection_name:str = None, **kwargs):
        super().__init__(**kwargs)
        self.db_name = db_name
        self.collection_name = None

    def _connect(self, **kwargs) -> MongoClient:
        if 'url' in kwargs:
            url = kwargs.pop('url')
        else:
            url = st.secrets.get("url")
            client = MongoClient(url)
        return client
    
    #call current collection or change collection
    def collection(self, collection_name):
        db = self._instance[self.db_name]
        self.collection_name = collection_name
        return db[collection_name]

    #switch to another database
    def database(self, db_name):
        self.db_name = db_name

    #returns collection names
    def list_collections(self):
        db = self._instance[self.db_name]
        return db.list_collection_names()

    #Insert one document to the collection
    def insert_one(self, data):
        collection = self.collection(self.collection_name)
        collection.insert_one(data)

    #Insert many documents into the collections
    def insert_many(self,data):
        collection = self.collection(self.collection_name)
        collection.insert_many(data)

    #Display all documents in the collection
    def find(self, query = None):
        collection = self.collection(self.collection_name)
        return collection.find(query)

    #Display the first document
    def find_one(self, query = None):
        collection = self.collection(self.collection_name)
        return collection.find_one(query)

    def dynamic_query(self, select_command, query = None):
        if select_command == "find":
            self.display(self.find(eval(query)))
        elif select_command == "find_one":
            st.write(self.find_one(eval(query)))
        elif select_command == "list_collections":
            value = self.list_collections()
            self.display(value)
        elif select_command == "database":
            return

    def display(self, data):
        for x in data:
            st.write(x)
