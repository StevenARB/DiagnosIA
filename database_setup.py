import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("symptoms_db.sqlite")
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS diseases (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    symptoms TEXT NOT NULL)''')

# Insertar datos (esto es un ejemplo; puedes expandir la lista)
diseases = [
    ("Gripe", "fiebre, tos, dolor de cabeza, congestión nasal"),
    ("Covid-19", "fiebre, tos, dificultad para respirar, pérdida de olfato"),
    ("Migraña", "dolor de cabeza, náuseas, sensibilidad a la luz, vómitos"),
    ("Amigdalitis", "dolor de garganta, fiebre, dificultad para tragar, inflamación de amígdalas")
]

# Insertar datos en la tabla
cursor.executemany("INSERT INTO diseases (name, symptoms) VALUES (?, ?)", diseases)

# Guardar y cerrar la conexión
conn.commit()
conn.close()
print("Base de datos creada y poblada con éxito.")