from flask import Flask, render_template

app = Flask(__name__)

####### Front page #######
@app.route("/")
def homepage():
	"""Displays homepage"""
	return render_template("homepage.html")

##############################################
if __name__ == "__main__":
	app.run(port=5000, host="0.0.0.0", debug=True)