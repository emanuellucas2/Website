#!flask/bin/python
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/vida-pessoal')
def pessoal():
	return render_template("Pessoal.html")

@app.route('/vida-academica')
def profissional():
	return render_template("Profissional.html")		

if __name__ == '__main__':
	app.run(debug=True)