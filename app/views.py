from flask import (Blueprint, render_template,
request, redirect, url_for)

from forms import SlamForm, SlamForm2


main = Blueprint('main', __name__)

@main.route("/")
def index(name="Unknown"):
	return render_template(
		"index.html",
		title="Mi kewl website",
		page_title="Index"

	)

@main.route("/form", methods=["POST", "GET"])
def slam_form():
	form = SlamForm2()
	if form.validate_on_submit():
		data = [{key:value} for key, value in request.form]
		print data

		return redirect(url_for("main.index"))
	else:
		return render_template(
			"form.html",
			title="Formulario Slam",
			form=form

			)