from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'mysecret'  # Needed to use session
#------------------------------------------------------------------------------------
''' in this / when we go to root page  if in username is in session it like dic 
    when we use get(variable,error string) if dic as a value it give the value or 
    it show error
'''

# Home page.      
@app.route('/')
def home():
    if 'username' in session: #it check if username is there in session 
        return f"Welcome back, {session['username']}!"   
    return "You are not logged in."
#---------------------------------------------------------------------------------
''' when we go to parth /login where this funcion run if the user post using form value 
    is take by request.form http <form> <input *((name=variable)> </form> dic[key]=value as
    same session[key]=request.form[value(form value)] 
'''
# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #dic[key]           =     value          
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form method="POST">
            <input name="username" placeholder="Enter name">
            <input type="submit">
        </form>
    '''
#---------------------------------------------------------------------------------
#when the user go to /logout pop the dic[username] = sesstion[username]
#promt to home

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)