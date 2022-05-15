from model.exepciones_criterio import CriteryAssignationError

class Criterio():
    def __init__(self, identificador, descripcion, ponderacion):
        self.identificador = identificador
        self.descripcion = descripcion
        self.ponderacion = ponderacion
        if isinstance(self.descripcion,str) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(STR) FOR NAME")
        if isinstance(self.identificador,int) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(INT) FOR IDENTIFY")
        if isinstance(self.ponderacion,float) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(INT) FOR PONDERATION")

    def set_identificador(self,identificacion):
        self.identificador = identificacion

    def set_descripcion(self,descripcion):
        self.descripcion = descripcion

    def set_ponderacion(self,ponderacion):
        self.ponderacion = ponderacion

    def get_identificador(self):
        return self.identificador
    
    def get_descripcion(self):
        return self.identificador
    
    def get_ponderacion(self):
        return self.ponderacion


    
    