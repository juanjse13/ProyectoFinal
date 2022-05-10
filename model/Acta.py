class Acta:
    def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante, identificacion_estudiante,
                 director, codirector, jurado1, jurado2):
        self._numero = numero
        self._fecha = fecha
        self._periodo = periodo
        self._autor = autor
        self._nombre_trabajo = nombre_trabajo
        self._modalidad = modalidad
        self._nombre_estudiante = nombre_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._director = director
        self._codirector = codirector
        self._jurado1 = jurado1
        self._jurado2 = jurado2
        self._observaciones_generales = ""
        self._detalles_criterios = {}
        self._nota_final = 0

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

    def set_observaciones_generales(self, observaciones_generales):
        self._observaciones_generales = observaciones_generales

    def set_detalles_criterios(self, detalles_criterios):
        self._detalles_criterios = detalles_criterios




