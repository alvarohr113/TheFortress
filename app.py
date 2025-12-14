from flask import Flask,request,render_template, jsonify,redirect, url_for
from markupsafe import escape

app = Flask(__name__) ## Constructor

@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/home", methods=['POST'])
def home():
    name = request.form.get("name")
    password = request.form.get("password")
    return render_template('home.html', name=escape(name), password=escape(password))

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/returnjson", methods=['POST'])
def returnjson():
    if request.method == 'POST':
        name = request.form.get("name_id")
        passw = request.form.get("password_id")
        data = {name : passw}
        return jsonify(data)












