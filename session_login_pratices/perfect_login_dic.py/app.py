from flask import Flask, g, session, redirect, render_template, current_app, url_for, request, jsonify
import subprocess

app = Flask(__name__)
app.secret_key = "konda"
user_code = {}
user_gmail = {}

# Home terminal route (requires login)
@app.route('/')
def terminal():
    if 'user' in session:
        return render_template("terminal.html", user=session['user'])
    return redirect(url_for("login"))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["username"]
        code = request.form["password"]
        if user in user_code and user_code[user] == code:
            session['user'] = user  # ✅ Store user in session
            return redirect(url_for("terminal"))
        else:
            return redirect(url_for("register"))
    return render_template("login.html")

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form["username"]
        email = request.form["email"]
        code = request.form["password"]
        user_gmail[user] = email
        user_code[user] = code
        return redirect(url_for("login"))
    return render_template("register.html")

# Execute shell commands route
@app.route('/execute', methods=['POST'])
def execute():
    if 'user' not in session:
        return jsonify({'output': 'Unauthorized'}), 401

    data = request.get_json()
    command = data.get('command', '')

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=5)
        output = result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        output = e.output.decode('utf-8')
    except Exception as e:
        output = str(e)

    return jsonify({'output': output})

if __name__ == "__main__":
    app.run(debug=True)