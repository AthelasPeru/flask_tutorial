from flask import Flask 

from flask_zurb_foundation import Foundation

from config import DEBUG, SECRET_KEY

app = Flask(__name__)
Foundation(app)

app.config["DEBUG"] = DEBUG
app.config["SECRET_KEY"] = SECRET_KEY
app.config["CSRF_ENABLED"] = True




from views import main

app.register_blueprint(main)



