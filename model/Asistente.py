from Usuario import Usuario
from Acta import Acta

"""
def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
director, codirector, jurado1, jurado2):

"""

class Asistente(Usuario):
    def __init__(self,nombre,identificacion,contrasena):
        self.actas_creadas = 0
        Usuario.__init__(self,nombre,identificacion,contrasena)
    
    def crear_nueva_acta(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
        director, codirector, jurado1, jurado2):
        self.actas_creadas += 1
        acta = Acta(numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
        director, codirector, jurado1, jurado2)
        return acta
    
    def get_actas_creadas(self):
        return self.actas_creadas

