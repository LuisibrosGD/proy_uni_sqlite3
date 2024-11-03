from modelo.profesor import profesorModelo

class profesorControlador:
    
    def __init__(self):
        self.objetoProfesorModelo = profesorModelo()
    
    def registrarProfesor(self):
        pass
    def mostrarProfesores(self):
        self.objetoProfesorModelo.verProfesores()
    def mostrarAlumnosMatriculados(self):
        pass
    def modificarDatosProfesor(self):
        pass
    def eliminarDatosProfesor(self):
        pass