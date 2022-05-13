from exepciones_criterio import CriteryAssignationError

class Criterio():
    def __init__(self):
        self.identificador = 0
        self.descripcion = ""
        self.ponderacion = 0
        if isinstance(self.descripcion,str) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(STR) FOR NAME")
        if isinstance(self.identificador,int) == False:
            raise CriteryAssignationError("INVALID, NEED TYPE(INT) FOR IDENTIFY")
        if isinstance(self.ponderacion,int) == False:
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
    
    def mod_criterio(self,new_identificador,new_descripcion,new_ponderacion):
        self.set_identificador(new_identificador)
        self.set_descripcion(new_descripcion)
        self.set_ponderacion(new_ponderacion)
    

    
    