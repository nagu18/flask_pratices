

from flask import Flask, request
# this the way we use the fome:- 
app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST': # this line is mostly used 
        username = request.form['username']
        return f"Hello, {username}!"
    return '''
        <form method="POST">
            <input name="username">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)