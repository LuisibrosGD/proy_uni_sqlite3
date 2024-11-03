from controlador.profesor_controlador import profesorControlador

class menuProfesor:
    
    def __init__(self):
        self.objetoProfesorControlador = profesorControlador()
    
    def mostrarMenuProfesor(self):
        while(True):
            print("1. Agregar profesor")
            print("2. Ver profesores")
            print("3. Ver alumnos matriculados en X curso")
            print("4. Modificar datos de profesor")
            print("5. Eliminar datos de profesor")
            print("0. Salir")
            opcion = int(input("Digite su opcion: "))
            if opcion == 1:
                self.objetoProfesorControlador.registrarProfesor()
            elif opcion == 2:
                self.objetoProfesorControlador.mostrarProfesores()
            elif opcion == 3:
                self.objetoProfesorControlador.mostrarAlumnosMatriculados()
            elif opcion == 4:
                self.objetoProfesorControlador.modificarDatosProfesor()
            elif opcion == 5:
                self.objetoProfesorControlador.eliminarDatosProfesor()
            elif opcion == 0:
                print("Volviendo")
                break
            else:
                print("opcion incorrecta")