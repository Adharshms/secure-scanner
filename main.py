from flask import Flask, request, render_template
from scanner import scan_website

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = scan_website(url)
    return render_template("index.html", result=result)

app.run(host="0.0.0.0", port=81)
