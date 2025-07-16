from flask import Flask, g, request,current_app

app = Flask(__name__)
count = 0
@app.before_request
def store_ip():
    global count
    count+=1
    g.user_ip = request.remote_addr  # Store the IP in `g`
    g.user = current_app.logger.info(f'user login {count}')

@app.route('/')
def home():
    return f"<h1>Hello! Your IP is: {g.user_ip } user {g.user}</h1>"

if __name__ == '__main__':
    app.run(debug=True)