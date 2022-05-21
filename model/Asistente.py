from model.Usuario import Usuario
from model.Acta import Acta


class Asistente(Usuario):
    def __init__(self, nombre, identificacion):
        self.actas_creadas = 0
        Usuario.__init__(self, nombre, identificacion)
    
    def crear_nueva_acta(self, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
        director, codirector, jurado1, jurado2, detalles_criterios):
        self.actas_creadas += 1
        numero = self.actas_creadas #Este es el número del acta que se va a crear
        acta = Acta(numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
        director, codirector, jurado1, jurado2, detalles_criterios)
        return acta
    
    def get_actas_creadas(self):
        return self.actas_creadas

