from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app,resources={r'/*': {'origins': '*'}})

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/ping", methods=['POST'])
def ping():
    print(request.data)
    return 'pong'



if(__name__ == "__main__"):
    app.run(debug=True)
