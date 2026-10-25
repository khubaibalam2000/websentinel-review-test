"""User lookup endpoint."""
import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


def db():
    return sqlite3.connect("shop.db")


@app.get("/users/lookup")
def lookup_user():
    email = request.args.get("email", "")
    row = db().execute("SELECT id, name FROM users WHERE email = '" + email + "'").fetchone()
    return jsonify(user=row)
