import sqlite3

def get_diseases():
    """Devuelve todas las enfermedades disponibles en la base de datos."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM diseases")
    diseases = [row[0] for row in cursor.fetchall()]
    conn.close()
    return diseases

def get_all_symptoms():
    """Devuelve una lista de todos los síntomas disponibles desde la base de datos."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT symptoms FROM diseases")
    result = cursor.fetchall()
    conn.close()
    
    # Suponiendo que cada enfermedad tiene una lista de síntomas, los extraemos y los devolvemos en formato de lista.
    symptoms = []
    for row in result:
        symptoms.extend(row[0].split(", "))  # Separamos los síntomas por coma
    return list(set(symptoms))  # Devolvemos los síntomas únicos

def get_symptoms(disease):
    """Devuelve los síntomas asociados a una enfermedad en minúsculas."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT symptoms FROM diseases WHERE name = ?", (disease,))
    result = cursor.fetchone()
    conn.close()
    
    # Convertir los síntomas a minúsculas si existen
    return [symptom.lower() for symptom in result[0].split(", ")] if result else []


def find_possible_diseases(input_symptoms):
    """Encuentra enfermedades posibles basadas en los síntomas ingresados."""
    conn = sqlite3.connect("symptoms_db.sqlite")
    cursor = conn.cursor()

    # Convertir los síntomas de entrada a minúsculas
    input_symptoms = [symptom.lower() for symptom in input_symptoms]
    print(input_symptoms)

    # Lista para almacenar las enfermedades posibles junto con la cantidad de coincidencias
    possible_diseases = []

    # Itera sobre todas las enfermedades y sus síntomas en la base de datos
    for disease, symptoms in cursor.execute("SELECT name, symptoms FROM diseases"):
        # Convertir los síntomas de la base de datos a minúsculas
        symptoms_list = [symptom.lower() for symptom in symptoms.split(", ")]
        
        # Contar las coincidencias entre los síntomas ingresados y los de la base de datos
        match_count = sum(1 for symptom in input_symptoms if symptom in symptoms_list)
        
        # Si hay al menos una coincidencia, añade la enfermedad a la lista
        if match_count > 0:
            possible_diseases.append((disease, match_count))
    
    conn.close()
    
    # Ordena las enfermedades por la cantidad de síntomas coincidentes de mayor a menor
    return sorted(possible_diseases, key=lambda x: x[1], reverse=True)
