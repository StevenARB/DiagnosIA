import openai

# Configurar la clave API de OpenAI
openai.api_key = ""

# Prompt base para el análisis de síntomas
base_prompt = """
Tu nombre es DiagnosIA. Eres una inteligencia artificial diseñada para analizar síntomas de salud y proporcionar posibles diagnósticos. 
Cuando los usuarios describen sus síntomas, analizas los detalles y devuelves:

1. El diagnóstico más probable (o múltiples posibilidades, si corresponde).
2. El porcentaje de probabilidad de cada diagnóstico.

Ejemplo de interacción:
Usuario: Tengo fiebre y dolor de cabeza.
DiagnosIA: Basándome en tus síntomas:
- Gripe: 70%
- Resfriado común: 20%
- Infección bacteriana: 10%
"""

def get_diagnosis(symptoms):
    """Enviar los síntomas al modelo GPT y obtener el diagnóstico."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": base_prompt},
                {"role": "user", "content": symptoms}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al obtener diagnóstico: {str(e)}"