import sqlite3
from symptoms_data import find_possible_diseases

def diagnose(symptoms):
    """Recibe una lista de síntomas y devuelve posibles enfermedades."""
    
    # Asegúrate de que los síntomas estén en minúsculas para evitar problemas con la capitalización.
    symptoms = [symptom.strip().lower() for symptom in symptoms]
    
    # Obtener enfermedades posibles basadas en los síntomas.
    possible_diseases = find_possible_diseases(symptoms)
    
    # Si no se encuentran enfermedades, muestra un mensaje adecuado.
    if not possible_diseases:
        return "No se encontraron enfermedades que coincidan con los síntomas ingresados."
    
    # Crear un mensaje con los resultados de las enfermedades.
    results = ""
    for disease, match_count in possible_diseases:
        results += f"- {disease} (síntomas coincidentes: {match_count})\n"
    
    return results