import pandas as pd
import csv
import os
from firebase_admin import credentials, firestore, initialize_app

# Replace with the path to your Firebase Admin SDK key
cred = credentials.Certificate('pcbuilder-8616d-firebase-adminsdk-8xt0d-fa576201a0.json')
initialize_app(cred)
db = firestore.client()

# Path to the directory containing your CSV files
csv_dir_path = '../pc-part-dataset/data/csv/'

# Loop through each CSV file in the directory
for csv_file in os.listdir(csv_dir_path):
    if csv_file.endswith('.csv'):
        with open(os.path.join(csv_dir_path, csv_file), mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # for row in reader:
            #     # Assuming 'name' is the field you want to use as the document ID
            #     doc_id = row.get('name')
            #     if doc_id:  # Make sure 'name' exists and is not empty
            #         # Check if the document already exists
            #         doc_ref = db.collection(csv_file.split(".")[0]).document(doc_id)
            #         doc = doc_ref.get()
            #         if not doc.exists:
            #             # Document does not exist, add it to the collection
            #             doc_ref.set(row)  # Use `set` to create a new document with the specified ID
            #         else:
            #             print(f'Document with ID {doc_id} already exists.')
            #     else:
            #         print('Row does not have a `name` field or it is empty.')
            print(reader.fieldnames)
        # print(csv_file.split(".")[0], "processing complete.")
        print(f'{csv_file.split(".")[0]}  processing complete.')