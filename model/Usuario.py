from model.exepciones_criterio import InvalidPassword


class ErrorUserName(Exception): # string Name
    def __init__(self,messaje = "INVALID CHARACTER(S) IN NAME, NUMBERS ARE NOT ALLOWED"):
        super().__init__(messaje)

class ErrorUserPassword(Exception): # int Password
    def __init__(self,messaje = "INVALID CHARACTER(S) IN PASSWORD"):
        super().__init__(messaje)
    
class ErrorUserIdentification(Exception): # int Identification
    def __init__(self,messaje = "INVALID CHARACTER(S) IN IDENTIFICATION"):
        super().__init__(messaje)

class Usuario():
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion

    def get_nombre(self):
        return self._nombre
    
    def get_identificacion(self):
        return self._identificacion

    def __del__(self):
        return "DELETE USER"

        
        
        


 
        
        
        


        


