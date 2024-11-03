from controlador.curso_controlador import cursoControlador

class menuCursos:
    
    def __init__(self):
        self.objetoControladorCurso = cursoControlador()
    
    def mostrarMenuCursos(self):
        while True:
            print("1. Agregar curso")
            print("2. Ver cursos disponibles")
            print("3. Modificar curso")
            print("4. Eliminar curso")
            print("0. Volver")
            opcion = int(input("Ingrese opcion: "))
            
            if opcion == 1:
                self.objetoControladorCurso.registrarCurso()
            elif opcion == 2:
                self.objetoControladorCurso.leerCursos()
            elif opcion == 3:
                self.objetoControladorCurso.verificarCurso()
            elif opcion == 4:
                self.objetoControladorCurso.eliminarCurso()
            elif opcion == 0:
                print("Volviendo")
                break
            else:
                print("Opcion incorrecta")