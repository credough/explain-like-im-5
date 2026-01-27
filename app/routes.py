from flask import Blueprint, request, jsonify
from .services.hf_client import simplify_text


main = Blueprint("main", __name__)


@main.route("/api/eli5", methods=["POST"])
def eli5():
    data = request.get_json()
    text = data.get("text")
    level = data.get("level", "eli5")


    if not text:
         return jsonify({"error": "Text is required"}), 400


    simplified = simplify_text(text, level)
    return jsonify({"result": simplified})