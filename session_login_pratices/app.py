from flask import Flask,url_for,redirect,request,g,current_app,session
app=Flask(__name__)
app.secret_key='Konda'
@app.route('/')
def home():
    if 'user_name' in session:
        user = session.get('user_name')
        return f'<h1> User:{user}'
    else:
        return f'<h1> NO USER FOUND</h1>'
    

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        session['user_name'] = request.form['username']
        return redirect(url_for('home'))

    return '''
    <form method="post">
        <lable for="username">Username:</lable>
        <input type="text" name="username" Placeholder="Enter user name"></input>
        <button type="submit">Login</button>
    </form>
    '''







if __name__ == '__main__':
    app.run(debug=True)