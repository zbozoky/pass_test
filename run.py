from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return os.get_env("MY_ENV517")


if __name__ == "__main__":
    app.run()