from .menu_cursos import menuCursos

from .menu_profesor import menuProfesor

from .menu_estudiante import menuEstudiante

class menuAdministrador:
    
        
    def mostrarMenuAdministrador(self):
        while True:
            print("1. Cursos")
            print("2. Profesores")
            print("3. Estudiantes")
            print("0. Salir")
            opcion = int(input("Digite su opcion: "))
            if opcion == 1:
                objetoCurso = menuCursos()
                objetoCurso.mostrarMenuCursos()
            elif opcion == 2:
                objetoProfesor = menuProfesor()
                objetoProfesor.mostrarMenuProfesor()
            elif opcion == 3:
                objetoEstudiante = menuEstudiante()
                objetoEstudiante.mostrarMenuEstudiante()