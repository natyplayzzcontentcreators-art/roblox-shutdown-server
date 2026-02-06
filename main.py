from flask import Flask, request, jsonify
import os

app = Flask(__name__)

game_state = {
    "shutdown": False,
    "reason": ""
}

@app.route("/status", methods=["GET"])
def status():
    return jsonify(game_state)

@app.route("/toggle", methods=["POST"])
def toggle():
    data = request.json or {}
    game_state["shutdown"] = not game_state["shutdown"]
    game_state["reason"] = data.get("reason", "Game is shut down.")
    return jsonify(game_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
