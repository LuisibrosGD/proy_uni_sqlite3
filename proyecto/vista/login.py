from .menu_administrador import menuAdministrador
from .menu_estudiante import menuEstudiante
from .menu_profesor import menuProfesor

class Login:
    
    def __init__(self):
        self.objA = menuAdministrador()
        self.objE = menuEstudiante()
        self.objP = menuProfesor()
    
    def mostrarLogin(self):
        nombre = input("Ingrese su nombre: ")
        contrasenia = input("Ingrese su contraseña: ")
        rol = int(input("Ingrese el rol: ")) # Administrador (0), Estudiante (1), Profesor (2)
        
        self.comprobarLogin(nombre,contrasenia,rol)
        
        if rol == 0:
            self.objA.mostrarMenuAdministrador()
        elif rol == 1:
            self.objP.mostrarMenuProfesor()
        elif rol == 2:
            self.objE.mostrarMenuEstudiante()
    
    def comprobarLogin(self,nombre,contrasenia,rol):
        # Por implementar
        pass