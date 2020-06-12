from flask import Flask, redirect, url_for, render_template, request, session, flash 
import random 

from datetime import timedelta



app = Flask(__name__)

app.secret_key = "something" 


@app.route("/casa")
@app.route("/")
def casa():
	return render_template ("casa.html")


if __name__ == "__main__":
	app.run(debug = True)