from model.DetalleCriterio import DetalleCriterio
from controller.Controlador import Controlador

class Acta:
    def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2):
        self._numero = numero
        self._fecha = fecha
        self._periodo = periodo
        self._autor = autor
        self._nombre_trabajo = nombre_trabajo
        self._modalidad = modalidad
        self._nombre_estudiante = nombre_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._director = director
        self._codirector = codirector
        self._jurado1 = jurado1
        self._jurado2 = jurado2
        self._observaciones_generales = ""
        self._detalle_criterio = {}
        self._agregar_detalles_criterios()

    def get_numero(self):
        return self._numero

    def set_observaciones_generales(self, observaciones_generales):
        self._observaciones_generales = observaciones_generales

    def _agregar_detalles_criterios(self): #Objeto de tipo controlador que contiene un diccionario con los criterios
        controlador_obj = Controlador() #Se crea una instancia de tipo controlador
        lista_criterios = controlador_obj.get_criterios()
        for posicion in range(0, len(lista_criterios) - 1):
            self._detalle_criterio[lista_criterios [posicion].get_identificador()] = DetalleCriterio(lista_criterios [posicion]) #Se asocia un detalleCriterio a un Criterio
    def exportar():
        pass
    def criterio_access():
        pass
    def get_acta():
        pass



