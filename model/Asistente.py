from model.Usuario import Usuario
from model.Acta import Acta


class Asistente(Usuario):
    def __init__(self):
        return self.generar_acta()

    def generar_acta(self, bool_value):
        if bool_value == True:
            return True
        else:
            return False

    def crear_nueva_acta(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2):
        acta = Acta(numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2) #Se crea la instancia de acta
        return acta