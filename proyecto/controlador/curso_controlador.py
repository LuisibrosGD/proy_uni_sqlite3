from modelo.curso import cursoModelo

class cursoControlador:
    
    def __init__(self):
        self.objCurso = cursoModelo()
    #opcion1
    def registrarCurso(self):
        nombreCurso = input("Ingrese el nombre del curso: ").strip().upper()
        creditos = int(input("Numero de creditos: "))
        self.objCurso.agregarCurso(nombreCurso, creditos)
    #opcion2
    def leerCursos(self):
        pass
    #opcion3
    def verificarCurso(self):
        pass
    #opcion4
    def eliminarCurso(self):
        pass