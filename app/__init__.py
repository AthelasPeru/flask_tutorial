from flask import Flask 

from config import DEBUG

app = Flask(__name__)

app.config["DEBUG"] = DEBUG




from views import main

app.register_blueprint(main)



