# BASICS NETWORKING DATA TRANSFER
# API
# HTTP MODULES
# NETWORKING PROTOCALLS (HTTP, TCP, UDP)
# API METHODS
# FLASK 



# MAIN DIFF BETWEEN DATA TRANSFER PROTOCALLS

# TCP is connection-oriented; use it when reliable data transmission is required.
# UDP is connectionless; use it for faster but less reliable communication (e.g., real-time apps).
# The requests library simplifies working with HTTP requests, providing methods for GET, POST, PUT, DELETE, etc.











# HTTP REQUESTS USING requests LIBRARY

# {*****when we are performing any api methods we simply get response from port server and client server in general methods we store this response in an variables******}


# JSON is simply like an key value pair as DICTIONARY in PYTHON 
#JSON DATA FORMAT JSON_DATA = {'KEY':'VALUE','KEYS':'VALUES'}

import requests

GET request
response_get = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response_get.json())

#POST request
data = {'title':'BLANKNKNKNKNKNKN','body':'MAIN BODYYYYYY','userID':'BLAH BLAH'}
response_post = requests.post('https://jsonplaceholder.typicode.com/posts/1',json=data)
print(response_post.json())

# PUT request
update_data = {'id': 1, 'title': 'foo updated', 'body': 'bar updated', 'userId': 1}
response_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=update_data)
print("PUT Response:", response_put.json())

# DELETE request
response_del = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("DELETE Response:", response_del.status_code)














# Basics of Networks

# Key Networking Concepts   ::::----->>>>>

# IP Address: Unique address identifying a device on a network.
# Ports: Virtual endpoints for communication (e.g., HTTP: 80, HTTPS: 443).
# Protocols:
# TCP: Reliable, connection-oriented communication.
# UDP: Fast, connectionless communication.
# HTTP/HTTPS: Hypertext Transfer Protocol for web communication.
# REST: Representational State Transfer, a design principle for APIs.


#BASIC FLASK SERVER

from flask import Flask,jsonify,request

#initialising APPP
app = Flask(__name__)

# In-memory data store/ OR DATABASSED CONNECTIONNNNNN
data_store = {"1": {"name": "Alice"}, "2": {"name": "Bob"}}


#setting up routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message':'HELLO THIS IS AN MESSAGE IN JSON FORMAT','USER':'WELCOME TO FLASK SERVER'})

#ACCEPTS AN PARA FROM URL
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

#POST ROUTE 
@app.route('/add', methods=['POST','GET'])
def add_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "num1 and num2 are required"}), 400
    return jsonify({"result": num1 + num2})

# PUT route: Update or add a record
@app.route('/update/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    data_store[item_id] = data
    return jsonify({"message": "Item updated", "data": data_store[item_id]}), 200

# DELETE route: Delete a record
@app.route('/delete/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404

    deleted_item = data_store.pop(item_id)
    return jsonify({"message": "Item deleted", "data": deleted_item}), 200


## FOR RUNNNNNING THE SERVER
if __name__ == '__main__':
    app.run(debug=True)
    
###### DEFAULT PORT AS ON :5000 ########




#TESTING server using 

# Breakdown:
# -X PUT: Specifies the HTTP method.
# -H "Content-Type: application/json": Sets the header to specify JSON data.
# -d '{"name": "Charlie"}': Sends the data in JSON format.
# http://127.0.0.1:5000/update/3: Target URL.

# GET Request:
# curl http://127.0.0.1:5000/

# Dynamic GET Request
# curl http://127.0.0.1:5000/greet/VIVEKKKKK

#POST request
#curl -X POST -H "Content-Type: application/json" -d '{"num1": 10, "num2": 20}' http://127.0.0.1:5000/

#PUT request
# curl -X PUT -H "Content-Type: application/json" \
# -d '{"name": "Charlie"}' \
# http://127.0.0.1:5000/update/3

#OR USE POSTMAN :)

#DELETE request
# curl -X DELETE http://127.0.0.1:5000/delete/1