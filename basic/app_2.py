from flask import Flask
app = Flask(__name__)
def index():
    return '<h1>hello</h1>' 
app.add_url_rule('/','index',index)


if __name__ == '__main__':
    app.run(debug=True)