# DiagnosIA: Asistente de Diagnóstico Médico
DiagnosIA es una aplicación de diagnóstico médico basada en inteligencia artificial, diseñada para ayudar a los doctores en la identificación de enfermedades.
Los usuarios ingresan los síntomas, y el sistema sugiere posibles enfermedades basadas en una base de datos médica.
Este proyecto es desarrollado por estudiantes de la Universidad Fidélitas.
----------------------------------------------------------------------
## Instalación
1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual:
    En Windows:
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
    En MacOS/Linux:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Instala las dependencias que están en el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. Inicializa la base de datos (solo se debe hacer la primera vez):
    ```bash
    python database_setup.py
    ```
----------------------------------------------------------------------
## Ejecución
1. Inicia la aplicación Flask:
    ```bash
    python app.py
    ```
2. Abre un navegador y accede a http://127.0.0.1:5000/ para usar la interfaz.

----------------------------------------------------------------------
## Herramientas utilizadas
- **Flask**: Para la interfaz web.
- **SQLite**: Como base de datos para almacenar información sobre síntomas y enfermedades.
- **Pandas**: Para manipulación de datos.
