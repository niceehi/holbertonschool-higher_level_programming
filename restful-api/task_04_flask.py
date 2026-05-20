#!/usr/bin/python3
"""A first Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Return welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_json_data():
    """Return a list of usernames in JSON format"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return status message"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def user_profile(username):
    """Return the user object for the given username"""

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the dictionary"""

    user_data = request.get_json()

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
