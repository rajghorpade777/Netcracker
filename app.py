from flask import Flask, request, jsonify
from collections import Counter
import re

app = Flask(__name__)

def analyze_logs(log_content):
    words = re.findall(r'\b\w+\b', log_content)
    word_counts = Counter(words)
    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        log_content = request.form.get("logs", "")
        result = analyze_logs(log_content)
        return jsonify(result)
    return '''
        <form method="post">
            <textarea name="logs" rows="10" cols="50"></textarea>
            <br><input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
