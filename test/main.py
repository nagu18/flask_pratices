from flask import Flask
from helper import say_hi

app = Flask(__name__)

@app.route('/')
def index():
    return say_hi()

if __name__ == '__main__':
    app.run(debug=True)