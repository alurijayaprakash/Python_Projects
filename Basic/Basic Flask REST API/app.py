import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({"name":"Jayaprakash", "email":"example@gmail.com"})


if __name__ == '__main__':
	app.run()