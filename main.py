from typing import List
from flask import Flask, request, jsonify
from app.chat_bot import generate_idea_suggestions, expand_idea_details
from app.utils import rank_ideas

app = Flask(__name__)

@app.route("/generate_ideas/", methods=["POST"])
def generate_ideas():
    """
    API endpoint to generate 3 unique ideas based on the user's query.
    """
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' in request body"}), 400

    query = data["query"]
    ideas = generate_idea_suggestions(query)
    ranked_ideas = rank_ideas(query, ideas)

    return jsonify({"ideas": ranked_ideas})
    # return jsonify({"ideas": ideas})

@app.route("/expand_ideas/", methods=["POST"])
def expand_ideas():
    """
    API endpoint to expand on the selected ideas.
    """
    data = request.get_json()
    if not data or "selected_ideas" not in data:
        return jsonify({"error": "Missing 'selected_ideas' in request body"}), 400

    selected_ideas = data["selected_ideas"]
    if not isinstance(selected_ideas, list) or len(selected_ideas) != 2:
        return jsonify({"error": "Please provide exactly 2 selected ideas as a list."}), 400

    detailed_suggestions = expand_idea_details(selected_ideas)
    return jsonify({"detailed_suggestions": detailed_suggestions})

if __name__ == "__main__":
    app.run(debug=True)
