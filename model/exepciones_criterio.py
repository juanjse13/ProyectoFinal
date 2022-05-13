

class CriteryAssignationError(BaseException): # Valores invalidos en los atributos de los criterios

    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()
    
class UserRegisterError(BaseException): # Valor invalido al ingresar un usuario

    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()

class UserLoginError(BaseException): # Valor invalido al logear un usuario o usuario no encontrado
    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()

class InvalidPassword(BaseException): # Valor invalido al logear un usuario o usuario no encontrado
    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()
    
class InvalidExportRecord(BaseException): # No se puede exportar acta porque su estado no es finalizado
    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()

class NotFoundUser(BaseException): # Un usuario o sus clases hijas no fue encontrado en la lista de usuarios 
    def __init__(self,*args: object) -> None:
        super().__init__(*args)
        
    def __str__(self) -> str:
        return super().__str__()
    


    
        
    


    