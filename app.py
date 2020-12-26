from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

