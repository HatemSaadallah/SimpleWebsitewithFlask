from flask import Flask, render_template, url_for, request, redirect, session, flash
import database

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		user = request.form['nm']
		password = request.form['pwd']
		if database.checkIdentity('user', user, password):
			session["user"] = user
			session["password"] = password
			return redirect(url_for('user'))
		else:
			flash("You have either entered a wrong username or password")
			return redirect(url_for("login"))
	else:
		if 'user' in session:
			return redirect(url_for("user"))
		else:
			return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session and "password" in session:
		user = session["user"]
		password = session["password"]
		return render_template("loggedin.html")
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop('user')
	return redirect(url_for("login"))

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
	if request.method == "POST":
		user = request.form['nm']
		password = request.form['pwd']
		email = request.form['email']
		database.insertRow('user', 1, user, password, email)
		session["user"] = user
		session["password"] = password
		return redirect(url_for('login'))
	else:
		return render_template("register.html")


if __name__ == "__main__":
	app.run(debug=True, port=5000)
