#need to learn all about current_app mostly used for cyber-security for debuging :- 
#in terminal 
from flask import Flask, current_app, session
from flask import request

app = Flask(__name__)
app.secret_key = 'YourSecretKey'

user_count = 0

@app.route('/')

def test():
    global user_count
    user_count += 1
    current_app.logger.info(f'[VISIT] User count: {user_count}, IP: {request.remote_addr}')
    return f'<h1>Welcome user {user_count}</h1>'



if __name__ == '__main__':
    app.run(debug=True)
    
