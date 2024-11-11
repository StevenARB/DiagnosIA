from symptoms_data import find_possible_diseases

def diagnose(symptoms):
    """Recibe una lista de síntomas y devuelve posibles enfermedades."""
    possible_diseases = find_possible_diseases(symptoms)
    if not possible_diseases:
        return "No se encontraron enfermedades que coincidan con los síntomas ingresados."
    
    # Crear un mensaje con los resultados de las enfermedades
    results = "Posibles enfermedades:\n"
    for disease, match_count in possible_diseases:
        results += f"- {disease} (síntomas coincidentes: {match_count})\n"
    return results
