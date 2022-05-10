from model.Usuario import Usuario
from model.Criterio import Criterio
from model.Acta import Acta


class Director(Usuario):
    def __init__(self, nombre, identificacion, contraseña):
        Usuario.__init__(self, nombre, identificacion, contraseña)

    def ver_acta(self, acta):
        numero_acta = acta.get_numero()
        fecha = acta.get_fecha()
        nombre_estudiante = acta.get_nombre_estudiante()
        nota_final = acta.get_nota_final()
        jurado1 = acta.get_jurado1()
        jurado2 = acta.get_jurado2()
        director = acta.get_director()
        return numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director



    def modificar_criterio(self, criterio, descripcion, ponderacion, identificador):
        criterio.set_descripcion(descripcion)
        criterio.set_identificador(identificador)
        criterio.set_ponderacion(ponderacion)

    def agregar_criterio(self, identificador, descripcion, ponderacion):
        criterio = Criterio(identificador, descripcion, ponderacion)
        return criterio
