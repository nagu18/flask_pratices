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
    if 'user' in session:
        IDuser = session.get("user")
        return f"{IDuser}"
    else:
        return 'error'
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        user_id=request.form["username"]
        passd = request.form["password"]
        if user_id in user_password and user_password[user_id] == passd:
            session['user'] = user_id
            return redirect(url_for("home"))
        else:
            return "<h1>Login failed</h1>"
    return render_template("html.html")
if __name__ == "__main__":
    app.run(debug=True)
