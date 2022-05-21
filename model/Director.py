
from Usuario import Usuario
from Criterio import Criterio
"""
La función ver_actas solo esta habilitada en el controlador, y se puede visualizar en la vista del Director, es decir
solo se incluira esta función de ver todas las actas para la vista asignada para el director
"""
class Director(Usuario):
    def __init__(self,nombre,contrasena,identificacion):
        Usuario.__init__(self,nombre,contrasena,identificacion)
    
    def ver_acta(self, acta):
        numero_acta = acta.get_numero()
        fecha = acta.get_fecha()
        nombre_estudiante = acta.get_nombre_estudiante()
        nota_final = acta.get_nota_final()
        jurado1 = acta.get_jurado1()
        jurado2 = acta.get_jurado2()
        director = acta.get_director()
        reconocimiento = acta.get_reconocimiento()
        return numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento

    def modificar_criterio(self, criterio, descripcion, ponderacion, identificador):
        criterio.set_descripcion(descripcion)
        criterio.set_identificador(identificador)
        criterio.set_ponderacion(ponderacion)

    def agregar_criterio(self, identificador, descripcion, ponderacion):
        criterio = Criterio(identificador, descripcion, ponderacion)
        return criterio
        

        
        

        
