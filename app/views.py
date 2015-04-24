from flask import Blueprint, render_template



main = Blueprint('main', __name__)

@main.route("/")
@main.route("/<string:name>")
def index(name="Unknown"):
	return render_template(
		"index.html",
		title="Mi kewl website",
		page_title="Index"

	)