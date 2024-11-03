import sqlite3

class conexionBD:
    
    def __init__(self):
        self.conexion = sqlite3.connect('base_de_datos\\universidad.db')
        self.cursor = self.conexion.cursor()
        # Crear las tablas al inicializar si no existen
        self.crear_tabla_profesores()
        self.crear_tabla_cursos()
        self.crear_tabla_alumnos()
    
    def crear_tabla_cursos(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                profesor_id,
                FOREIGN KEY (profesor_id) REFERENCES Profesores (id)
            )
        ''')
        self.conexion.commit()
    
    def crear_tabla_profesores(self):
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Profesores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT UNIQUE NOT NULL
            )
        ''')
        self.conexion.commit()
    def crear_tabla_alumnos(self):
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            curso_id,
            FOREIGN KEY (curso_id) REFERENCES Cursos (id)
            )
        ''')
        self.conexion.commit()
    
    def ejecutar_consulta(self, consulta, parametros=()):
        """
        Metodo auxiliar para ejecutar una consulta SQL.
        """
        self.cursor.execute(consulta, parametros)
        # Ojito que ya se esta realizando el commit
        self.conexion.commit()
        return self.cursor
    # se usa asi:
    # resultado = conexion.ejecutar_consulta(sql, (nombre,)).fetchone()

    def cerrar_conexion(self):
        """
        Metodo para cerrar la conexión a la base de datos.
        """
        self.cursor.close()
        self.conexion.close()
        
    
    
# no hace falta crear un metodo para conectarse a una tabla en especifica
# ya que eso se hace en la consulta

# Pero si son bases de datos en diferentes archivos, ahi si se hace eso.