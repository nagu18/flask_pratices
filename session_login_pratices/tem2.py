from flask import Flask,session,redirect,render_template,current_app,g,url_for,request
app=Flask(__name__)
app.secret_key ="konda"
user_info  = {'nagu':"123"} 
@app.route('/')
def home():
    if 'user_session' in session:
        user_login = session.get('user_session')
        return f"<h1>Hi {user_login}</h1>"
    else:
        return redirect(url_for('login'))



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        if user in user_info and password == user_info[user]:
            session['user_session'] = user
            return redirect(url_for('home'))
        else:
            return f"<h1>error input</h1>"
    return render_template('html.html')
    

        






if __name__ == "__main__":
    app.run(debug=True)