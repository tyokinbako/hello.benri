from flask import Flask
haru = Flask(__name__)
@haru.route("/")
def hello():
    return "こんにちは！"
haru.run(host="0.0.0.0")