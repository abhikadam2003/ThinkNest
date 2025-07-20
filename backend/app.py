from flask import Flask, request, jsonify
from model_utils import create_vector_index, search_from_index

app = Flask(__name__)
vector_index = None

def load_vector_index():
    global vector_index
    vector_index = create_vector_index("data/")  # your folder with .txt files

@app.route("/ask", methods=["POST"])
def ask():
    global vector_index
    if not vector_index:
        return jsonify({"error": "Index not loaded"}), 500

    data = request.get_json()
    query = data.get("question", "")
    if not query:
        return jsonify({"error": "No question provided"}), 400

    answer = search_from_index(vector_index, query)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    load_vector_index()
    app.run(debug=True)
