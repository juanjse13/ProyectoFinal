

class DetalleCriterio:
    def __init__(self, calificacion1, calificacion2, observacion1, observacion2, criterio):
        self._calificacion1 = calificacion1
        self._calificacion2 = calificacion2
        self._observacion1 = observacion1
        self._observacion2 = observacion2
        self._criterio = criterio

    def calcular_nota_criterio(self):
        nota =  ((self._calificacion1 + self._calificacion2) / 2) * self._criterio.get_ponderacion()
        return nota