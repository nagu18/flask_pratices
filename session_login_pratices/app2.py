from flask import Flask,redirect,url_for,g,current_app,session,request,render_template
app=Flask(__name__)
app.secret_key = "Nagu"
@app.route('/')
def home():
    if 'tem_user' in session:
        user_tem = session.get('tem_user')
        return f"<h1>{user_tem}</h1>"
    else:
        return "<h2> user not found </h1>"
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        session['tem_user'] = request.form['username']
        return redirect(url_for("home"))
    return render_template("html.html")
if __name__ == '__main__':
    app.run(debug=True)
    