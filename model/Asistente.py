from model.Usuario import Usuario
from model.Acta import Acta


class Asistente(Usuario):
    def __init__(self, nombre, identificacion, contraseña):
        Usuario.__init__(nombre, identificacion, contraseña)

    def crear_nueva_acta(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2):
        acta = Acta(numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2) #Se crea la instancia de acta
        return acta