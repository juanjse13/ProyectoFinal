
class DetalleCriterio:

    #Se aplica sobrecarga
    def __int__(self, criterio):
        self._calificacion1 = 0
        self._calificacion2 = 0
        self._observacion1 = 0
        self._observacion2 = 0
        self._criterio = criterio

    def calcular_nota_criterio(self):
        nota =  ((self._calificacion1 + self._calificacion2) / 2) * self._criterio.get_ponderacion()
        return nota

    def set_calificacion1(self, calificacion1):
        self._calificacion1 = calificacion1

    def set_calificacion2(self, calificacion2):
        self._calificacion2 = calificacion2

    def set_observacion1(self, observacion1):
        self._observacion1 = observacion1

    def set_calificacion1(self, observacion2):
        self._observacion2 = observacion2
    
    def get_criterio(self):
        return self._criterio