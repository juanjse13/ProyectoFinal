from model import*

class Jurado(Usuario):
    def __init__(self):
        Usuario.__init__()

    def exportar_acta(self,acta):
        acta.exportar()
        return acta

    def evaluar_tesis(self,detalle_criterio):
        vista = detalle_criterio.criterio_access()
        vista.get_identificador()
        vista.get_descripcion()
        vista.get_ponderacion()
        try:
            nota = int(input())
            detalle_criterio.set_calificacion(nota)
        except nota > 5 or nota < 0.5:
            return "INVALID CALIFICATION"
        try:
            detalle_criterio.set_observacion()
        except detalle_criterio.get_observacion() == " ":
            return "INVALID OBSERVATION"
