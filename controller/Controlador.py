from model.Criterio import Criterio
from model.Asistente import Asistente
from model.Jurado import Jurado
from model.Director import Director



class Controlador:
    def __init__(self):
        self._criterios = []
        self._inicializar_criterios() #inicializa los criterios
        self._actas = {}
        self._asistentes = {1007827635 : Asistente(), 66825016 : Asistente(), 93384031 : Asistente()} #TODO: Agregarle los parámetros a las instancias
        self._jurados = {123 : Jurado(), 321 : Jurado(), 543 : Jurado()}
        self._directores = {100786354 : Director(), 95485943 : Director()}



    def _inicializar_criterios(self):
        self._criterios.append(Criterio(0, "Desarrollo y profundidad en el tratamiento del tema", 0.2 ))
        self._criterios.append(Criterio(1, "Diseño académico y científico del tema", 0.15))
        self._criterios.append(Criterio(2, "Cumplimiento de los objetivos propuetos", 0.1))
        self._criterios.append(Criterio(3, "Creatividad e innovación de las soluciones y desarrollos propuestos", 0.1))
        self._criterios.append(Criterio(4, "Validez de los resultados y conclusiones", 0.2))
        self._criterios.append(Criterio(5, "Manejo y procesamiento de la información y bibliografía", 0.1))
        self._criterios.append(Criterio(6, "Calidad y presentación del documento escrito", 0.075))
        self._criterios.append(Criterio(7, "Presentación oral", 0.075))

    def agregar_acta(self, acta_obj):
        self._actas[acta_obj.get_numero()] = acta_obj #Se agrega el acta al diccionario y se le asocia la llave


