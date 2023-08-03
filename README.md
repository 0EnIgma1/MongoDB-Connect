# MongoDB-Connect
A Streamlit application made for Streamlit Connections Hackathon. This App contains MongoConnection class that can be used to connect with MongoDB Databases using Streamlit in a easier way.

### This Application demonstrates on how to connect to MongoDB Database through Streamlit.
The Connection is done and established through st.experimental_connection

This Application uses MongoConnection class which inherits 'ExperimentalBaseConnection' class of Streamlit that allows to connect to data sources.

Try Form Demo, which contains a basic user form and pushes the data to the document in the collections database.

## Functionalies:
- **_list_collections()_** - Lists all collections in a Database
- **_database(database_name)_** - Moves to the specified Database
- **_collection(collection_name)_** - Moves to the specified Collection
- **_insert(data)_** - Inserts Single and multiple data(documents) into the collection
- **_find(query)_** - Fetches and returns the data based on the query
- **_find_one(query)_** - Fetches and returns the first document based on the query
- **_dynamic_query(select_command, query)_** = Unique Method that allows to perform MongoDB commands in the streamlit app itself :)

Connection to MongoDB is established by calling **MongoConnection** in **st.experimental_connection()** and mentioning the Database name to which we need to connect.
MongoConnection class uses **_connect()** method to get the connection URL stored in secrets.toml and connect using MongoClient from pymongo

```python
client = st.experimental_connection("mongoDB", type = MongoConnection, db_name = "my_database")
```

You can call the above methods by calling them after the connected object (client)

```python
# display all the collections in the database
client.display(client.list_collections())
# find documents that match the query
client.display(client.find({"name" : "Naveen"}))
```

```python
#Dynamic Query - Pass query Directly from the Streamlit UI
select_command = col1.selectbox("Commands", options = ["None", "find", "find_one", "list_collections", "database", "collection"])
query_command = col2.text_input("Enter your query")
if select_command and query_command:    
    client.dynamic_query(select_command, query_command)
```
[application Link]("https://mongoconnect.streamlit.app/")
