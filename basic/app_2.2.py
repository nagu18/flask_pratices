from flask import Flask
app = Flask(__name__)
#route one :- 
@app.route('/')
def index():
    return f'<h1>Hello<h1>'

#route two:- 
@app.route('/user/<name>')
def index_2(name):
    return f'<h2>bro it me {name}<h2>'
    


#debuging 
if __name__ == '__main__':
    app.run(debug=True)