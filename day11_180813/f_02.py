﻿from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return "Home"

if __name__ == '__main__':
    app.run()
