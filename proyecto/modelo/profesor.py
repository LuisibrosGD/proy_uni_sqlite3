from base_de_datos.conexionBD import conexionBD,sqlite3

class profesorModelo:
    def __init__(self):
        self.conexionBaseDatos = conexionBD()
        
    def agregarProfesor(self,nombre,departamento):
        
        try:
            sql = "INSERT INTO Profesores(nombre,departamento) VALUES (?,?)"
            valores = (nombre,departamento)
            self.conexionBaseDatos.ejecutar_consulta(sql,valores)
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            self.conexionBaseDatos.cerrar_conexion()
        
        
    def verificarProfesor(self, nombre):
        
        sql = "SELECT nombre FROM Profesores WHERE nombre = ?"
        valores = (nombre,)
        resultado = self.conexionBaseDatos.ejecutar_consulta(sql,valores).fetchone()
        if resultado is None:
            print("No se encontró al profesor")
        else:
            print("Registro encontrado")
        
    def verProfesores(self):
        sql = "SELECT * FROM Profesores"
        resultado = self.conexionBaseDatos.ejecutar_consulta(sql).fetchall()
        
        for dato in resultado:
            print(f"ID: {dato[0]}, Nombre: {dato[1]}, Departamento: {dato[2]}")
            
        
    def modificarDatosProfesor(self):
        pass
    def eliminarProfesor(self):
        pass
    def verCursosAsignados(self):
        pass