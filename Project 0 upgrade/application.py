from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
	return render_template("index.html")

@app.route("/forms.html")
def forms():
	return render_template("forms.html")

@app.route("/lookup_customers.html")
def lookup_customers():
	return render_template("lookup_customers.html")

@app.route("/check_class_attendees.html")
def check_class_attendees():
	return render_template("check_class_attendees.html")