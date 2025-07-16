from flask import Flask
app = Flask(__name__)
@app.route('/facebook/<user>')
def index(user):
    return '<h1> hello </h1> {}'.format(user)
    

if __name__ == '__main__':
    app.run(debug=True)
