from flask import Flask,g,session,redirect,render_template,current_app,url_for,request
app=Flask(__name__)
app.secret_key="konda"
user_code={}
user_gmail={}


@app.route('/')
def terminal():
    return render_template("terminal.html")







@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form["username"]
        code = request.form["password"]
        if user in user_code and user_code[user] == code:
            return redirect(url_for("terminal"))
        else:
            return redirect(url_for("register"))
    return render_template("login.html")



@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        user = request.form["username"]
        email = request.form["email"]
        code = request.form["password"]
        user_gmail[user]=email
        user_code[user]=code
        return redirect(url_for("login"))
    return render_template("register.html")

        

if __name__ == "__main__":
    app.run(debug=True)