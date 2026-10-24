"""Shop API - a small sample service used to test WebSentinel code reviews."""
import sqlite3

from flask import Flask, abort, g, jsonify, request

app = Flask(__name__)
DB_PATH = "shop.db"


def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


def current_user():
    """The signed-in user from the session token (set by the auth middleware)."""
    return getattr(g, "user", None)


def require_login():
    if current_user() is None:
        abort(401)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/products/<int:product_id>")
def product(product_id):
    row = db().execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,)).fetchone()
    if row is None:
        abort(404)
    return jsonify(dict(row))


if __name__ == "__main__":
    app.run()
