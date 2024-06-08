from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from datetime import datetime
from bson import ObjectId
import math
import pytz


app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Test"
mongo = PyMongo(app)

def ObjectIdToStr(o):
    if isinstance(o, ObjectId):
        return str(o)
    raise TypeError

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/items')
def get_items():
    items = mongo.db.items.find()
    item_list = [{"name": item["name"]} for item in items]
    return jsonify(item_list)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.json.get('name', 'NewItem')
        created_at = datetime.now(pytz.utc)
        result = mongo.db.items.insert_one({'name': item_name, 'created_at': created_at})
        item_id = result.inserted_id
        return jsonify({'msg': 'Item added successfully', 'item_id': str(item_id)}), 201
    else:  # For GET request
        return 'This route expects a POST request.'


@app.route('/collections')
def get_collections():
    collections = mongo.db.list_collection_names()
    return jsonify(collections)

@app.route('/collection_data/<collection_name>')
def get_collection_data(collection_name):
    collection_data = mongo.db[collection_name].find()
    data_list = list(collection_data)

    # Convert to a serializable format and handle NaN values
    for item in data_list:
        for key, value in item.items():
            if isinstance(value, float) and math.isnan(value):
                item[key] = None  # or 'N/A', 0, or remove the key
        item["_id"] = str(item["_id"])

    return jsonify(data_list)

@app.route('/collection_data2/<collection_name>')
def get_collection_data2(collection_name):
    collection_data = mongo.db[collection_name].find()
    data_list = list(collection_data)
    names = []
    # Convert to a serializable format and handle NaN values
    for item in data_list:
        names.append(item['name'])
    names.sort()
    return jsonify(names)

@app.route('/search/<category>/<name>')
def search(category, name):
    collection = mongo.db[category]
    filtered_results = collection.find({"name": {"$regex": name, "$options": "i"}})
    results = list(filtered_results)
    for result in results:
        for key, value in result.items():
            if isinstance(value, float) and math.isnan(value):
                result[key] = None  # or 'N/A', 0, or remove the key
        result['_id'] = str(result['_id'])
    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)
