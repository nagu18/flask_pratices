from flask import Flask,g,current_app,redirect,url_for,render_template,request,session
app = Flask(__name__)
app.secret_key ="kondanagendar"
user_info={
    'konda':'nagu@2004',
    'mouli':'bhai',
    'vikas':'bahibolthe',
}
@app.route('/') #sesstion is mainly used for user login info 
def home():
    if 'user' in session:
        tem_user=session.get('user') #how to pass varible to templates
        return render_template("home.html",tem_user=tem_user) #where just mention
    else:
        return "<h2>INVALID<h2>"


@app.route('/login',methods=['GET','POST']) #must needed
def login():
    if request.method == "POST": # must neeed 
        user = request.form['username'] 
        password = request.form['password']
        if user in user_info and user_info[user] == password:
            session['user']=user
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    return render_template("html.html")




if __name__ == "__main__":
    app.run(debug=True)