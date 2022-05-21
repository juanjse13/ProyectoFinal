from model.exepciones_criterio import InvalidExportRecord, NotFoundUser


class Acta:
    def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2, detalles_criterios):
        self._numero = numero
        self._fecha = fecha
        self._periodo = periodo
        self._autor = autor
        self._nombre_trabajo = nombre_trabajo
        self._modalidad = modalidad
        self._estado_acta = "Vacio" #Puede ser: Vacio, En proceso o Terminado
        self._nombre_estudiante = nombre_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._director = director
        self._codirector = codirector
        self._jurado1 = jurado1
        self._jurado2 = jurado2
        self._observaciones_generales = ""
        self._detalles_criterios = detalles_criterios
        self._nota_jurado1 = 0
        self._nota_jurado2 = 0
        self._nota_final = 0
        self._reconocimiento = "" # Intervalo de la nota del acta
    
    def get_numero(self):
        return self._numero

    def get_fecha(self):
        return self._fecha

    def get_periodo(self):
        return self._periodo

    def get_autor(self):
        return self._autor

    def get_nombre_trabajo(self):
        return self._nombre_trabajo

    def get_modalidad(self):
        return self._modalidad

    def get_nombre_estudiante(self):
        return self._nombre_estudiante

    def get_identificacion_estudiante(self):
        return self._identificacion_estudiante

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

    def get_detalles_criterios(self):
        return self._detalles_criterios

    def get_estado_acta(self):
        return self._estado_acta

    def set_estado_acta(self, estado_acta):
        self._estado_acta = estado_acta

    def set_observaciones_generales(self, observaciones_generales):
        self._observaciones_generales = observaciones_generales

    def set_detalles_criterios(self, detalles_criterios):
        self._detalles_criterios = detalles_criterios

    def set_estado_acta(self, estado_acta):
        self._estado_acta = estado_acta

    def set_nota_jurado1(self, nota_jurado1):
        self._nota_jurado1 = nota_jurado1

    def set_nota_jurado2(self, nota_jurado2):
        self._nota_jurado2 = nota_jurado2

    def get_nota_jurado1(self):
        return self._nota_jurado1

    def get_nota_jurado2(self):
        return self._nota_jurado2

    def set_nota_final(self, nota_final):
        self._nota_final = nota_final

    def evaluar_acta(self):
        if self._estado_acta == "Vacio":
            raise InvalidExportRecord("IS NOT POSSIBLE EXPORT CAUSE IS EMTY")
        elif self._estado_acta == "Proceso":
            raise InvalidExportRecord("IS NOT POSSIBLE EXPORT CAUSE RECORD IS IN PROGRESS")
        elif self._estado_acta == "Terminado":
            self.exportar() # Añadir código para exportar a pdf

    def set_reconocimiento(self, nota_final):
        if 4.5 <= nota_final <=5:
            self._reconocimiento = "Alto"
        elif 4.0 <= nota_final < 4.5:
            self._reconocimiento = "Normal"
        elif 3.5 <= nota_final < 4:
            self._reconocimiento = "Basico"
        elif nota_final < 3.5:
            self._reconocimiento = "Rechazado"

    def get_reconocimiento(self):
        return self._reconocimiento
    
    def exportar(self):
        pass
            