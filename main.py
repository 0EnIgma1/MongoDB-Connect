import streamlit as st
from mongo_connect import MongoConnection

page = st.sidebar.radio("Pages", ["Homepage", "Form Demo"])

#Connection Establishment
client = st.experimental_connection("mongoDB", type = MongoConnection, db_name = "my_database")

if page == "Homepage":
    st.markdown("""
    # Streamlit Connections Hackathon
    ### This Application demonstrates on how to connect to MongoDB Database through Streamlit.
    The Connection is done and established through st.experimental_connection

    This Application uses MongoConnection class which inherits 'ExperimentalBaseConnection' class of Streamlit that allows to connect to data sources.

    Try Form Demo, which contains a basic user form and pushes the data to the document in the collections database.

    ## Functionalities:
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
    select_command = col1.selectbox("Commands", options = ["None", "find", "find_one", "list_collections", "collection"])
    query_command = col2.text_input("Enter your query")
    if select_command and query_command:    
        client.dynamic_query(select_command, query_command)
    """)

    st.text(" ")
    st.text(" ")

    client.collection("test")

    st.markdown("""
    ## Dynamic Query
    
    #### Key Points:
    - For this demo app, The app is connected with 'my_database' in my atlas cluster
    - Default collection is test
    - Default Value in query is 'None'
    - Whenever entering a Query, enclose it in curly Brackets '{}'
    - to check the data format in test collection, run 'find'
    - Irrelevent query will return an error and a warning.
    
    Example Query:
    _command : find, query : {"country" : "India"}_
    """)

    st.text(" ")
    st.text(" ")

    col1, col2 = st.columns([1,3])

    select_command = col1.selectbox("Commands", options = ["None", "find", "find_one", "list_collections", "collection"])

    if select_command == "collection":
        change_collection = col2.selectbox("collections", options = list(client.list_collections()))
        client.collection(change_collection)
        st.write("Collection Changed to {} Successfully !".format(change_collection))

    else:
        query_command = col2.text_input("Enter your query", value = None, placeholder = "default Value is None")
        
        if st.button("Submit"):
            try:
                output = client.dynamic_query(select_command, query_command)
            except:
                st.error("Enter a Valid Query")
                st.warning("Check whether the query follows the keypoints")

    if st.button("refresh"):
        st.experimental_rerun()


        
    st.text(" ")
    st.text(" ")

if page == "Form Demo":

    st.markdown("""
    #### A sample form that collects user data and pushes into the database as a document.

    """)

    st.text(" ")

    with st.form("Data Form", clear_on_submit = True):
        name = st.text_input("Enter your Name")
        gender = st.text_input("Enter your Gender")
        age = st.slider("Enter your Age", 0,100)
        country = st.text_input("Enter your Country")
        submit = st.form_submit_button("Submit")
        
    if submit:
        data = {
        "name" : name, 
        "gender" : gender,
        "age" : age,
        "country" : country
        }
        client.insert_one(data)

    st.text(" ")

    st.markdown("""
    When View all data button is clicked, all the documents in the collections are displayed using display() method.
    """)
    if st.button("View All Data"): 
        client.display(client.find())

    if st.button("refresh"):
        st.experimental_rerun()

st.markdown("""
Made by **Naveen kumar S**
""")
