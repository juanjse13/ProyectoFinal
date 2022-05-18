from model.Criterio import Criterio
from model.Asistente import Asistente
from model.Jurado import Jurado
from model.Director import Director
from model.DetalleCriterio import DetalleCriterio
from model.Acta import Acta



class Controlador:
    def __init__(self):
        self._criterios = []
        self._inicializar_criterios() #inicializa los criterios
        self._actas = {}
        self._asistentes = {1007827636 : Asistente("Juan", 1007827635, 123), 66825016 : Asistente("Juan", 66825016, 123), 93384031 : Asistente("Pepe", 93384031, 123)}
        self._jurados = {123 : Jurado("Martin", 123, 123), 321 : Jurado("Alex", 3215, 123), 543 : Jurado("Alex", 543, 123)}
        self._directores = {100786354 : Director("Francesco", 100786354, 123), 95485943 : Director("Luis", 95485943, 123)}
        self._lista_actas = []

    def _inicializar_criterios(self):
        self._criterios.append(Criterio(0, "Desarrollo y profundidad en el tratamiento del tema", 1.0))
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

    def get_actas(self):
        return self._actas

    def get_jurados(self):
        return self._jurados

    def get_directores(self):
        return self._directores

    def agregar_acta(self, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                    director, codirector, jurado1, jurado2, asistente): #recibe por parametros el asistente que crea el acta
        detalles_criterios = self.agregar_detalles_criterios()  # Se inicializan los detalles criterios para cada instancia de tipo Acta
        acta_obj = asistente.crear_nueva_acta(fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                    director, codirector, jurado1, jurado2, detalles_criterios)
        self._actas[acta_obj.get_numero()] = acta_obj  # Se agrega el acta al diccionario y se le asocia la llave


    def agregar_nuevo_criterio(self, identificador, descripcion, ponderacion): #Se añade el criterio a la lista Criterios
        nuevo_criterio = Director.agregar_criterio(identificador, descripcion, ponderacion)
        self._criterios.append(nuevo_criterio)

    def validar_criterios(self):
        suma_ponderaciones = 0
        for criterio in self._criterios:
            suma_ponderaciones = suma_ponderaciones + criterio.get_ponderacion()
        return suma_ponderaciones


    def ver_actas(self,acta, director): #TODO: Implementar método
        numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento = director.ver_acta(acta)
        return numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento

        
    def ver_promedios(self): # Solo para las actas con estados Terminado
        promedio = 0
        lista_notas =[]
        for i in self._actas:  ##TODO: Toca revisar esto...Acta no es una arreglo...es un diciconario...
            if self._actas[i].get_estado() == "Terminado":
                valores = self._actas[i].get_nota_final()
                lista_notas.append(valores)
                promedio = sum(lista_notas)/len(lista_notas)
        return promedio
    
    def generar_dataFrame_actas(self):
        df = pd.DataFrame(self._lista_actas,columns=["Numero de Acta","Fecha","Estudiante","Estado del Acta","Nota ponderada","Jurados","Director","Reconocimiento"])
        return df
    
    def graficar_notas_actas(self): ##TODO: Toca revisar esto...Acta no es una arreglo...es un diciconario...
        for i in self._actas:
            if self._actas[i].get_estado() == "Terminado":
                pass

    def agregar_detalles_criterios(self): #Objeto de tipo controlador que contiene una lista con los criterios
        detalle_criterios = {}
        for criterio in self._criterios:
            detalle_criterios[criterio.get_identificador()] = DetalleCriterio(criterio) #Se asocia un detalleCriterio a un Criterio
        return detalle_criterios

    ##TODO: Definir correctmente el método
    def evaluar_acta(self, lista_observaciones, lista_calificaciones, tipo_jurado, acta_a_calificar):
        for calificacion in range (0, len(lista_calificaciones) - 1):
            pass
