from exepciones_criterio import InvalidExportRecord, NotFoundUser
class Acta:
    def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2):
        self._numero = numero
        self._fecha = fecha
        self._periodo = periodo
        self._autor = autor
        self._nombre_trabajo = nombre_trabajo
        self._modalidad = modalidad
        self._estado_acta = "" #Puede ser: Vacio, En proceso o Terminado
        self._nombre_estudiante = nombre_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._director = director
        self._codirector = codirector
        self._jurado1 = jurado1
        self._jurado2 = jurado2
        self._observaciones_generales = ""
        self._detalles_criterios = {}
        self._nota_final = 0
        self._reconocimiento = "" # Intervalo de la nota del acta

    def get_numero(self):
        return self._numero

    def get_fecha(self):
        return self._fecha

    def get_nombre_estudiante(self):
        return self._nombre_estudiante

    def get_nota_final(self):
        return self._nota_final

    def get_jurado1(self):
        return self._jurado1

    def get_jurado2(self):
        return self._jurado2

    def get_director(self):
        return self._director
    
    def get_codirector(self):
        return self._codirector
    
    def verificador_estado(self):
        conteo = 0
        for i in self._detalles_criterios:
            if self._detalles_criterios[i].calcular_nota_criterio() != 0:
                conteo += 1
        if conteo == len(self._detalles_criterios):
            self._estado_acta = "Terminado"
        elif 0 < conteo < len(self._detalles_criterios):
            self._estado_acta = "Proceso"
        elif conteo == 0:
            self._estado_acta = "Vacio"
    
    def get_estado(self):
        self.verificador_estado()
        return self._estado_acta

    def set_observaciones_generales(self, observaciones_generales):
        self._observaciones_generales = observaciones_generales

    def set_detalles_criterios(self, detalles_criterios):
        self._detalles_criterios = detalles_criterios
    
    def evaluar_acta(self):
        if self._estado_acta == "Vacio":
            raise InvalidExportRecord("IS NOT POSSIBLE EXPORT CAUSE IS EMTY")
        elif self._estado_acta == "Proceso":
            raise InvalidExportRecord("IS NOT POSSIBLE EXPORT CAUSE RECORD IS IN PROGRESS")
        elif self._estado_acta == "Terminado":
            self.exportar() # Añadir código para exportar a pdf
            
    def recorrido_actas(self):
        self.get_numero()
        self.get_fecha()
        self.get_nombre_estudiante()
        self.get_estado()
        self.get_nota_final()
        self.get_director()
        self.get_codirector()
        self.get_jurado1()
        self.get_jurado1()
        self.get_jurado2()
    
    def calcular_reconocimiento(self):
        if 4.5 <= self._nota_final <=5:
            self._reconocimiento = "Alto"
        elif 4.0 <= self._nota_final < 4.5:
            self._reconocimiento = "Normal"
        elif 3.5 <= self._nota_final < 4:
            self._reconocimiento = "Basico"
        elif self._nota_final < 3.5:
            self._reconocimiento = "Rechazado" 
        
    def evaluar_acta(self,jurado): # Evalua si es el jurado del acta y cual de los dos designados es 
        if jurado == self._jurado1:
            for i in self._detalles_criterios:
                self._detalles_criterios[i].get_criterio().get_descripcion()
                self._detalles_criterios[i].set_calificacion1()
        elif jurado == self._jurado2:
            for i in self._detalles_criterios:
                self._detalles_criterios[i].get_criterio().get_descripcion()
                self._detalles_criterios[i].set_calificacion2()
        else:
            raise NotFoundUser("NO JURY FOUND FOR THIS RECORD")
        
    def get_reconocimiento(self):
        self.calcular_reconocimiento()
        return self._reconocimiento
    
    def exportar(self):
        pass
            