
from Criterio import Criterio
from Asistente import Asistente
from Jurado import Jurado
from Director import Director
from DetalleCriterio import DetalleCriterio
from Acta import Acta
from PDF_fpdf import PDF


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
        self._criterios.append(Criterio(0, "Desarrollo y profundidad en el tratamiento del tema", 0.2))
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
        director_temp = Director("",0,0)
        nuevo_criterio = director_temp.agregar_criterio(identificador, descripcion, ponderacion)
        self._criterios.append(nuevo_criterio)

    def validar_criterios(self):
        suma_ponderaciones = 0.0
        for criterio in self._criterios:
            suma_ponderaciones += float(criterio.get_ponderacion())
            print(" ", suma_ponderaciones, " ")
        return suma_ponderaciones


    def ver_actas(self,acta, director):
        numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento = director.ver_acta(acta)
        return numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento

    def agregar_detalles_criterios(self): #Objeto de tipo controlador que contiene una lista con los criterios
        detalle_criterios = {}
        for criterio in self._criterios:
            detalle_criterios[criterio.get_identificador()] = DetalleCriterio(criterio) #Se asocia un detalleCriterio a un Criterio
        return detalle_criterios

    def encontrar_nota_parcial_jurado(self, acta, numero_jurado):
        diccionario_detalles_criterios = acta.get_detalles_criterios()
        suma_notas = 0
        for llave in diccionario_detalles_criterios.keys():
            detalle_criterio = diccionario_detalles_criterios[llave]
            if numero_jurado ==1: #Tiene que revisarse cuál de los dos jurados es para calcular la nota parcial del jurado
                suma_notas += detalle_criterio.get_criterio().get_ponderacion() * detalle_criterio.get_calificacion1()
            elif numero_jurado == 2:
                suma_notas += detalle_criterio.get_criterio().get_ponderacion() * detalle_criterio.get_calificacion2()
        #Para agregar la nota parcial en el acta dependiendo del jurado
        if numero_jurado ==1:
            acta.set_nota_jurado1(suma_notas)
        elif numero_jurado == 2:
            acta.set_nota_jurado2(suma_notas)

        return suma_notas #Devuelve la nota parcial final para lo que está calificando el jurado

    def cambiar_estado_acta(self, acta):
        diccionario_detalles_criterios = acta.get_detalles_criterios()
        for llave in diccionario_detalles_criterios.keys():
            detalle_criterio = diccionario_detalles_criterios[llave]
            if detalle_criterio.get_calificacion1() == 0 or detalle_criterio.get_calificacion2() == 0: #En este caso falta que uno de los dos jurados califique"
                estado = "En proceso"
            elif detalle_criterio.get_calificacion1() != 0 and detalle_criterio.get_calificacion2() != 0: #En este caso...ya existen las dos notas...acta terminada
                estado = "Terminado"
        return estado

    def hallar_nota_final(self, acta):
        nota_final = (acta.get_nota_jurado1() + acta.get_nota_jurado2()) / 2
        acta.set_nota_final(nota_final)
        acta.set_reconocimiento(nota_final) #Establece la evaluación cualitativa de la tesis
        return nota_final

    def generar_txt(self,acta):
        file = open("acta.txt","w")
        file.write(f'Numero del acta : {acta.get_numero()}\n')
        file.write(f'Fecha : {acta.get_fecha()}\n')
        file.write(f'Periodo : {acta.get_periodo()}\n')
        file.write(f'Autor : {acta.get_autor()}\n')
        file.write(f'Nombre del Trabajo : {acta.get_nombre_trabajo()}\n')
        file.write(f'Modalidad : {acta.get_modalidad()}\n')
        file.write(f'Estado del acta : {acta.get_estado_acta()}\n')
        file.write(f'Nombre del Estudiante : {acta.get_nombre_estudiante()}\n')
        file.write(f'Identificación del Estudiante : {acta.get_identificacion_estudiante()}\n')
        file.write(f'Director : {acta.get_director().get_nombre()}\n')
        file.write(f'Codirector : {acta.get_codirector().get_nombre()}\n')
        file.write(f'Jurado : {acta.get_jurado1().get_nombre()}\n')
        file.write(f'Jurado : {acta.get_jurado2().get_nombre()}\n')
        file.write(f'Nota Final : {acta.get_nota_final()}\n')
        file.write(f'Reconocimiento : {acta.get_reconocimiento()}\n')
        
    def exportar_acta(self,acta):
        self.generar_txt(acta)
        pdf = PDF()
        pdf.add_page()
        pdf.texts('acta.txt')
        pdf.titles(f'ACTA IDENTIFICADA CON EL NÚMERO :  {acta.get_numero()}')
        pdf.set_author(acta.get_autor())
        pdf.output('test.pdf','F')


