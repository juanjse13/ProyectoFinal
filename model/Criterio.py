class Criterio:

    def __init__(self, identificador, descripcion, ponderacion):
        self._identificador = identificador
        self._descripcion = descripcion
        self._ponderacion = ponderacion

    def get_identificador(self):
        return self._identificador

    def set_identificador(self, identificador):
        self._identificador = identificador

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def get_ponderacion(self):
        return self._ponderacion

    def set_pónderacion(self, ponderacion):
        self._ponderacion = ponderacion







