from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "NaguKonda"

# Dummy user database
user_password = {
    'kond': '123',
    'nagu': '134',
}

@app.route('/')
def home():
    if "user" in session:
        return f"<h1>Welcome, {session['user']}!</h1><br><a href='/logout'>Logout</a>"
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["username"]
        passw = request.form["password"]

        if user in user_password and user_password[user] == passw:
            session['user'] = user
            return redirect(url_for("home"))
        else:
            return "<h1>Invalid username or password</h1>"

    return render_template('html.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)