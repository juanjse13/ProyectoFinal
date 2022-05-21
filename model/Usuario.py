
from exepciones_criterio import InvalidPassword

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
    def __init__(self,name,identificacion,password):
        lista_comprobante1 = "0123456789"

        if isinstance(identificacion,int) == False:
            raise ErrorUserIdentification
        elif isinstance(identificacion,int) == True:
            self.identificacion =identificacion

        if isinstance(password,int) == False:
            raise ErrorUserPassword
        elif isinstance(password,int) == True:
            self.contrasena = password
        
        if password == "" or password == " ":
            raise ErrorUserPassword

        for itr in range(len(name)):
            for irt in range(len(lista_comprobante1)):
                if name[itr] == lista_comprobante1[irt]:
                    raise ErrorUserName
                else:
                    self.nombre = name
            
    def get_contrasena(self):
        return self.contrasena
    
    def get_nombre(self):
        return self.nombre
    
    def get_identificacion(self):
        return self.identificacion

    def __del__(self):
        return "DELETE USER"
    
    def change_password(self,anti_password,new_password):
        if anti_password == self.get_contrasena():
            self.contrasena = new_password
        else:
            raise InvalidPassword("IS NOT THE CORRECT PASSWORD")

 
        
        
        


 
        
        
        


        


