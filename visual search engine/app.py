from flask import Flask, request, render_template
from search.search_engine import search_by_text, search_by_image
import os
from werkzeug.utils import secure_filename
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        if "query" in request.form and request.form["query"]:
            query = request.form["query"]
            results = search_by_text(query)
        elif "image" in request.files:
            file = request.files["image"]
            if file:
                path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
                file.save(path)
                results = search_by_image(path)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
