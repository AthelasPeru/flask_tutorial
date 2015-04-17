from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/equipo")
def equipo():
	team = ["Polo", "Gerald", "Karel", "Esen", "Pedro"]

	return render_template("equipo.html", team=team)


@app.route("/codepit")
def codepit():
	
	team = ["sujumayas", "darkzar", "ondoheer", "kalligos", "dpolo27"]
	fighters = []

	for member in team:
		req = requests.get("http://www.codeivate.com/users/{}.json".format(member))
		character = req.json()
		fighters.append(character)

	print fighters

	return render_template("codepit.html", title="Code Pit", fighters=fighters)

if __name__ == '__main__':
    app.run(debug=True)
