import sqlite3
'''
python- Base de datos incorporada sqlite
sin instalacion de software adicional
'''
conn = sqlite3.connect('estudiantes.db')

c = conn.cursor()

#crearemos recien una tabla y ejecutaremos
#sintaxis usadas en SQL
# 5 tipos de datos: text, integer,real, ..2 mas
'''
Recuerda siemple el comando c.execute( Dentro se pone la accion.)
1. PRIMER PASO CREAR DATABASE
2. INSERTAR VALORES
'''
#c.execute("""CREATE TABLE estudiantes (
#             nombre TEXT,
#             edad   INTEGER,
#             estatura REAL
#         )""")

'''
c.execute("INSERT INTO estudiantes VALUES ('Marck',27,1.9)")

todos_estudiantes = [
('Jhon',21,1.8),
('david',35,19),
('michael',19,1.73),
]
c.executemany("INSERT INTO estudiantes VALUES (?,?,?)",todos_estudiantes)

'''
c.execute("SELECT * FROM estudiantes")
print(c.fetchall)
x= c.fetchall()
for i in x:
    print(i)

conn.commit()

conn.close()

# Link para ver el visor de sql en web
# https://inloop.github.io/sqlite-viewer/