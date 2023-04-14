from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    return response('Hello World!')

def response(name: str) -> str:

    return name