import pandas as pd
from pymongo import MongoClient
import os
# from pypartpicker import Scraper


# MongoDB connection string
mongo_uri = "mongodb://localhost:27017/"
# Name of the database
database_name = "Test2"

# Folder path containing your CSV files
folder_path = "../pcpartpicker_data/pc-part-dataset/data1/csv/"

# Create a MongoDB client
client = MongoClient(mongo_uri)

# Select the database
db = client[database_name]

# Function to process each CSV file
def process_csv(file_path, collection_name):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Convert the DataFrame to a dictionary format for MongoDB
    data_dict = data.to_dict("records")

    # Get the collection for this CSV file
    collection = db[collection_name]

    for record in data_dict:
        # Assuming 'id' is your unique identifier
        unique_id = record.get("name")
        if unique_id is not None:
            # Check if the entry already exists
            if collection.find_one({"id": unique_id}) is None:
                # If the entry does not exist, insert it
                collection.insert_one(record)

# Loop through each CSV file in the directory
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Set the collection name based on the filename (without the .csv extension)
        collection_name = filename[:-4]
        process_csv(file_path, collection_name)
        print(f"Processed {filename}")

print("Data insertion complete.")
                

# List all collection names in the database
collection_names = db.list_collection_names()

# Loop through each collection name
for collection_name in collection_names:
    print("Collection:", collection_name)
    # Perform operations on the collection as needed
    # For example, to count documents in the collection:
    count = db[collection_name].count_documents({})
    print(f"Number of documents in {collection_name}: {count}")

    # Retrieve the collection
    collection = db[collection_name]

    # Use the find() method to get all documents in the collection
    documents = collection.find()

     # Loop through each document in the collection
    for document in documents:
        print(document)  # Print the document
        # You can also access specific fields using document['field_name']
