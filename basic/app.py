from flask import Flask
app = Flask(__name__)
@app.route('/user/<name>') # url request 
def index(name): # function 
    return f'<h1>hello{name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)