import sqlite3

def get_diseases():
    """Devuelve todas las enfermedades disponibles en la base de datos."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM diseases")
    diseases = [row[0] for row in cursor.fetchall()]
    conn.close()
    return diseases

def get_symptoms(disease):
    """Devuelve los síntomas asociados a una enfermedad."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT symptoms FROM diseases WHERE name = ?", (disease,))
    result = cursor.fetchone()
    conn.close()
    return result[0].split(", ") if result else []

def find_possible_diseases(input_symptoms):
    """Encuentra enfermedades posibles basadas en los síntomas ingresados."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()

    # Lista para almacenar las enfermedades posibles junto con la cantidad de coincidencias
    possible_diseases = []

    # Itera sobre todas las enfermedades y sus síntomas en la base de datos
    for disease, symptoms in cursor.execute("SELECT name, symptoms FROM diseases"):
        symptoms_list = symptoms.split(", ")
        match_count = sum(1 for symptom in input_symptoms if symptom in symptoms_list)
        
        # Si hay al menos una coincidencia, añade la enfermedad a la lista
        if match_count > 0:
            possible_diseases.append((disease, match_count))
    
    conn.close()
    
    # Ordena las enfermedades por la cantidad de síntomas coincidentes de mayor a menor
    return sorted(possible_diseases, key=lambda x: x[1], reverse=True)