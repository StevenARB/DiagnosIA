from flask import Flask, render_template, request
from diagnosis_engine import diagnose

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = ""
    if request.method == "POST":
        symptoms = request.form["symptoms"].strip().lower().split(", ")
        diagnosis = diagnose(symptoms)
    return render_template("index.html", diagnosis=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)