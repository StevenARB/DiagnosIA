from flask import Flask, render_template, request
from api_gpt import get_diagnosis  # Importamos la función para conectarnos a la API
from symptoms_data import get_all_symptoms  # Asumimos que tienes esta función para obtener todos los síntomas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Obtenemos todos los síntomas posibles
    symptoms_list = get_all_symptoms()
    diagnosis = ""  # Inicializamos el diagnóstico como vacío

    if request.method == "POST":
        # Obtenemos los síntomas seleccionados por el usuario
        selected_symptoms = request.form.getlist("symptoms")  
        # Convertimos la lista de síntomas seleccionados a una cadena separada por comas
        symptoms_text = ", ".join(selected_symptoms)
        # Llamamos a la función `get_diagnosis` para obtener el diagnóstico de OpenAI
        diagnosis = get_diagnosis(symptoms_text)

    return render_template("index.html", symptoms_list=symptoms_list, diagnosis=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)
