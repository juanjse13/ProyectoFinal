
class Usuario():
    def __init__(self):
        self.nombre = ""
        self.identificacion = 0
        self.contrasena = ""
    def register(self,name,password,identificacion):
        lista_comprobante1 = ['0','1','2','3','4','5','6','7','8','9']
        lista_comprobante2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ñ']
        lista_comprobante3 = ['@','#','%','&','$','!','*','?','¿','+','-']
        for itr in name:
            try:
                self.nombre = name
            except name[itr] == lista_comprobante1[itr]:
                return "ERROR, INVALID CHARACTER(S) IN NAME, NUMBERS ARE NOT ALLOWED"
            try: 
                self.identificacion = identificacion
            except identificacion[itr] == lista_comprobante2[itr]:
                return "ERROR, INVALID CHARACTER(S) IN IDENTIFICATION, CHARACTER(S) ARE NOT ALLOWED"
            try:
                self.contrasena = password
            except password[itr] == lista_comprobante3[itr]:
                return "ERROR, INVALID CHARACTER(S) IN PASSWORD"
        try:
            self.contrasena = password
        except password == "" or password == " ":
            return "ERROR, INVALID PASSWORD"

    def __del__(self):
        return "DELETE USER"
    
    def change_password(self,password):
        self.contrasena = password

 
        
        
        


