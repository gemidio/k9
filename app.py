from flask import Flask

app = Flask(__name__)
app.config.from_object("config.py")


@app.route("/")
def hello_world() -> str:
    return response("Hello World!")


def response(name: str) -> str:
    return name
