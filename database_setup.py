import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("symptoms_db.sqlite")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS diseases (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    symptoms TEXT NOT NULL)''')

# Eliminar el contenido existente en la tabla si esta existe
cursor.execute("DELETE FROM diseases")

# Insertar datos (esto es un ejemplo; puedes expandir la lista)
diseases = [
    ("Gripe", "Fiebre, Tos, Dolor de Cabeza, Congestión Nasal"),
    ("Covid-19", "Fiebre, Tos, Dificultad para Respirar, Pérdida de Olfato"),
    ("Migraña", "Dolor de Cabeza, Náuseas, Sensibilidad a la Luz, Vómitos"),
    ("Amigdalitis", "Dolor de Garganta, Fiebre, Dificultad para Tragar, Inflamación de Amígdalas")
]

# Insertar datos en la tabla
cursor.executemany("INSERT INTO diseases (name, symptoms) VALUES (?, ?)", diseases)

# Guardar y cerrar la conexión
conn.commit()
conn.close()
print("Base de datos creada y poblada con éxito.")
