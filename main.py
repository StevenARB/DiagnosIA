from diagnosis_engine import diagnose

def main():
    print("Bienvenido a SymptoBot - Asistente de Diagnóstico de Enfermedades")
    print("Por favor, ingrese sus síntomas separados por coma (e.g., fiebre, tos):")
    user_input = input("Síntomas: ")
    symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]

    # Diagnóstico basado en los síntomas ingresados
    diagnosis = diagnose(symptoms)
    print(diagnosis)

if __name__ == "__main__":
    main()
