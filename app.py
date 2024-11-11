from flask import Flask, render_template, request
from diagnosis_engine import diagnose

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = ""  # Inicializamos el diagnóstico como vacío
    if request.method == "POST":
        symptoms = request.form["symptoms"].strip().lower().split(", ")  # Obtenemos los síntomas
        diagnosis = diagnose(symptoms)  # Llamamos a la función de diagnóstico
    return render_template("index.html", diagnosis=diagnosis)  # Devolvemos la página con el diagnóstico

if __name__ == "__main__":
    app.run(debug=True)