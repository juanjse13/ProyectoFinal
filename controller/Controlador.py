from model.Criterio import Criterio
from model.Asistente import Asistente
from model.Jurado import Jurado
from model.Director import Director
from model.DetalleCriterio import DetalleCriterio

class Controlador:
    def __init__(self):
        self._criterios = []
        self._inicializar_criterios() #inicializa los criterios
        self._actas = {}
        self._asistentes = {1007827636 : Asistente("Juan", 1007827635, 123), 66825016 : Asistente("Juan", 66825016, 123), 93384031 : Asistente("Pepe", 93384031, 123)}
        self._jurados = {123 : Jurado("Martin", 123, 123), 321 : Jurado("Alex", 3215, 123), 543 : Jurado("Alex", 543, 123)}
        self._directores = {100786354 : Director("Francesco", 100786354, 123), 95485943 : Director("Luis", 95485943, 123)}



    def _inicializar_criterios(self):
        self._criterios.append(Criterio(0, "Desarrollo y profundidad en el tratamiento del tema", 0.2 ))
        self._criterios.append(Criterio(1, "Diseño académico y científico del tema", 0.15))
        self._criterios.append(Criterio(2, "Cumplimiento de los objetivos propuetos", 0.1))
        self._criterios.append(Criterio(3, "Creatividad e innovación de las soluciones y desarrollos propuestos", 0.1))
        self._criterios.append(Criterio(4, "Validez de los resultados y conclusiones", 0.2))
        self._criterios.append(Criterio(5, "Manejo y procesamiento de la información y bibliografía", 0.1))
        self._criterios.append(Criterio(6, "Calidad y presentación del documento escrito", 0.075))
        self._criterios.append(Criterio(7, "Presentación oral", 0.075))


    def get_criterios(self):
        return self._criterios

    def get_asistentes(self):
        return self._asistentes

    def get_jurados(self):
        return self._jurados

    def get_directores(self):
        return self._directores

    def agregar_acta(self, acta_obj): #Método que recibe una instancia de tipo Acta y lo agrega al diccionario de Actas
        detalles_criterios = self.agregar_detalles_criterios() ##Se inicializan los detalles criterios para cada instancia de tipo Acta
        acta_obj.set_detalles_criterios(detalles_criterios)
        self._actas[acta_obj.get_numero()] = acta_obj #Se agrega el acta al diccionario y se le asocia la llave

    def agregar_nuevo_criterio(self, identificador, descripcion, ponderacion): #Se añade el criterio a la lista Criterios
        nuevo_criterio = Director.agregar_criterio(identificador, descripcion, ponderacion)
        self._criterios.append(nuevo_criterio)

    def cambiar_criterio(self, identificador, descripcion, ponderacion):
        for posicion in range(0, len(self._criterios)):
            if self._criterios[posicion].get_identificador() == identificador: #Si corresponde al criterio deseado, cambie dicho criterio
                Director.modificar_criterio(self._criterios[posicion], descripcion, ponderacion, identificador)

    def ver_actas(self): #TODO: Implementar método
        pass

    def agregar_detalles_criterios(self): #Objeto de tipo controlador que contiene una lista con los criterios
        lista_criterios = self._criterios
        detalle_criterios = {}
        for posicion in range(0, len(lista_criterios) - 1):
            detalle_criterios[lista_criterios[posicion].get_identificador()] = DetalleCriterio(lista_criterios[posicion]) #Se asocia un detalleCriterio a un Criterio
        return detalle_criterios


