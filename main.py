from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import openai

# Configurar la clave API de OpenAI
openai.api_key = "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"

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

class DiagnosIAHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Servir el formulario HTML en respuesta a GET."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DiagnosIA</title>
        </head>
        <body>
            <h1>DiagnosIA - Diagnóstico Médico</h1>
            <form action="/" method="post">
                <label for="symptoms">Describe tus síntomas separados por comas:</label><br>
                <textarea id="symptoms" name="symptoms" rows="4" cols="50" placeholder="Ejemplo: fiebre, dolor de cabeza"></textarea><br>
                <button type="submit">Diagnosticar</button>
            </form>
            <br>
            <div id="diagnosis"></div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        """Procesar los datos del formulario enviados por POST."""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode("utf-8"))
        symptoms = parsed_data.get("symptoms", [""])[0]
        
        # Obtener el diagnóstico basado en los síntomas
        diagnosis = get_diagnosis(symptoms)

        # Responder con el diagnóstico
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DiagnosIA</title>
        </head>
        <body>
            <h1>DiagnosIA - Diagnóstico Médico</h1>
            <form action="/" method="post">
                <label for="symptoms">Describe tus síntomas separados por comas:</label><br>
                <textarea id="symptoms" name="symptoms" rows="4" cols="50" placeholder="Ejemplo: fiebre, dolor de cabeza"></textarea><br>
                <button type="submit">Diagnosticar</button>
            </form>
            <br>
            <div id="diagnosis">
                <h2>Posible Diagnóstico:</h2>
                <p>{diagnosis}</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(response_html.encode("utf-8"))

# Configurar y correr el servidor HTTP
def run(server_class=HTTPServer, handler_class=DiagnosIAHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

exit ()

