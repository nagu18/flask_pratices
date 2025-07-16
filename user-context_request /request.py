from flask import Flask
from flask import request
app =Flask(__name__)

'''
@app.route('/')
def index():
    # This 'request' is only visible to the user who made the request
    user_agent = request.headers.get('User-Agent')
    return f"<p>Your browser is {user_agent}</p>"

if __name__ == "__main__":
    app.run(debug=True)
'''
@app.route('/')

def index():
    user_agent=request.headers.get('User_Agent')
    return f'<h1>your user data:- <h1>/n{user_agent}'


if __name__ == '__main__':
    app.run(debug=True)
