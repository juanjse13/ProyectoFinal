class Criterio:

    def __init__(self, identificador, contexto, problema, ponderacion):
        self._identificador = identificador
        self._contexto = contexto
        self._problema = problema
        self._ponderacion = ponderacion
        self._calificaciones = [] #Se define inicialmente un arreglo que no tiene elementos(calificaciones) aún

    def get_identificador(self):
        return self._identificador

    def set_identificador(self, identificador):
        self._identificador = identificador

    def get_contexto(self):
        return self._contexto

    def set_contexto(self, contexto):
        self._contexto = contexto

    def get_problema(self):
        return self._problema

    def set_problema(self, problema):
        self._problema = problema

    def get_calificacion1(self):
        return self._calificacion1

    def set_calificacion1(self, calificacion1):
        self._calificacion1 = calificacion1

    def get_calificaciones(self):
        return self._calificaciones

    def calcular_nota_criterio(self):
        nota = sum(self._calificaciones) #Suma todos los elementos de la lista
        nota_final = nota / len(self._calificaciones)
        return nota_final




