#RESPONSÁVEL PELA APLICAÇÃO FLASK
#E PELOS ENDPOINTS

import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from db import db
from models.book import Book
from flask import Flask, jsonify, request

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/hello", methods=["GET"])
def hello():
    return "API está funcionando!"

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    book = Book(
        title=data["title"],
        author=data["author"],
        description=data["description"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({
        "message": "Livro inserido com sucesso"
    }), 201

@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()

    return jsonify([
        book.as_dict()
        for book in books
    ])

@app.route("/books/<uuid:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)

    return jsonify(book.as_dict())

@app.route("/books/<uuid:book_id>", methods=["PATCH"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)

    data = request.get_json()

    for key, value in data.items():
        setattr(book, key, value)

    db.session.commit()

    return jsonify({
        "message": "Livro atualizado com sucesso"
    })    

@app.route("/books/<uuid:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Livro removido com sucesso"
    })

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

#http://127.0.0.1:5000/hello
#http://127.0.0.1:5000/books