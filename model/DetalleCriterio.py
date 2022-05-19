
class DetalleCriterio:

    def __init__(self, criterio):
        self._calificacion1 = 0
        self._calificacion2 = 0
        self._observacion1 = 0
        self._observacion2 = 0
        self._criterio = criterio

    def set_calificacion1(self, calificacion1):
        self._calificacion1 = calificacion1

    def get_calificacion1(self):
        return self._calificacion1

    def set_calificacion2(self, calificacion2):
        self._calificacion2 = calificacion2

    def get_calificacion2(self):
        return self._calificacion2

    def set_observacion1(self, observacion1):
        self._observacion1 = observacion1

    def get_observacion1(self):
        return self._observacion1

    def set_observacion2(self, observacion2):
        self._observacion2 = observacion2

    def get_observacion2(self):
        return self._observacion2

    def get_criterio(self):
        return self._criterio