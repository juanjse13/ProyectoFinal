from model.exepciones_criterio import CriteryAssignationError

class Criterio():
    def __init__(self, identificador, descripcion, ponderacion):
        self._identificador = identificador
        self._descripcion = descripcion
        self._ponderacion = ponderacion
        if isinstance(self._descripcion,str) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(STR) FOR NAME")
        if isinstance(self._identificador,int) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(INT) FOR IDENTIFY")
        if isinstance(self._ponderacion,float) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(INT) FOR PONDERATION")

    def set_identificador(self,identificacion):
        self._identificador = identificacion

    def set_descripcion(self,descripcion):
        self._descripcion = descripcion

    def set_ponderacion(self,ponderacion):
        self._ponderacion = ponderacion

    def get_identificador(self):
        return self._identificador
    
    def get_descripcion(self):
        return self._descripcion
    
    def get_ponderacion(self):
        return self._ponderacion


    
    
    