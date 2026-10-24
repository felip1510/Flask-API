#RESPONSÁVEL PELA APLICAÇÃO FLASK
#E PELOS ENDPOINTS

import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from db import db
from models.book import Book
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/hello", methods=["GET"])
def hello():
    return "API está funcionando!"

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

#http://127.0.0.1:5000/hello