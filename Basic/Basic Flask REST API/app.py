import json
from os import abort
from urllib import response
from flask import Flask, jsonify, request
app = Flask(__name__)

mydict = {"cat":{"age":2, "country":"India"},\
    "dog":{"age":4, "country":"UK"},\
    "cow":{"age":5, "country":"Srilanka"},
    "cow":{"age":5, "country":"Srilanka"}}


# # end point : http://localhost:5000/?name=cat
# # Examples of Flask URL Parameters -> ?name=cat

# @app.route('/', methods=["GET"])
# def getAnimalData():
#     name = request.args.get('name')
#     print("getAnimalData() -->", name)
#     if name in mydict:
#         return jsonify({"data":mydict[name]})
#     return abort(404)


# end point : http://localhost:5000/cat
# Examples of Flask URL Variables -> cat

# another ex : http://localhost:5000/student/11
#     route('/student/<int:id>')

@app.route('/<string:name1>', methods=["GET"])
def getAnimalData(name1):
    # name = request.args.get('name')
    print("getAnimalData() -->", name1)
    if name1 in mydict:
        return jsonify(mydict[name1])
    response = jsonify({'Status':'Not in Database','Item':name1})
    response.status_code = 404
    return response


# DELETE Method
# end point : http://localhost:5000/cat

@app.route('/<string:name>', methods=["DELETE"])
def deleteAnimalData(name):
    print("deleteAnimalData() -->" , name )
    if name in mydict :
        mydict.pop(name)
        response = jsonify(mydict)
        # response.status_code = 200
        return response
    response = jsonify({'Status':'Not in Database','Item':name})
    response.status_code = 404
    return response

# POST Method
# end point : http://localhost:5000/
# body ==>
# {
#     "dell": {
#         "age": 5,
#         "country": "China"
#     }
# }
@app.route('/', methods=["POST"])
def addAnimalData():
    print("addAnimalData() -->")
    data = request.get_json()
    print("Data -->", data)
    key = list(data.keys())[0]
    mydict[key]=data[key]
    # response = jsonify({'Status':'Successfully Stored','Item':mydict})
    return mydict


# PUT Method
# end point : http://localhost:5000/
# body:-
# {
#     "dog": {
#         "age": 444,
#         "country": "Pak"
#     }
# }

@app.route('/', methods=["PUT"])
def updateAnimalData():
    print("addAnimalData() -->")
    data = request.get_json()
    print("Data -->", data)
    print("Hello", list(data.keys())[0])
    key = list(data.keys())[0]
    # mydict[key]=data[key]  #anotherway
    mydict[key]["age"]=data[key]["age"]
    mydict[key]["country"]=data[key]["country"]


    # response = jsonify({'Status':'Successfully Stored','Item':mydict})
    return mydict

if __name__ == '__main__':
	app.run()