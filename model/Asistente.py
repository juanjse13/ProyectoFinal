from model import*

class Asistente(Usuario):
    def __init__(self):
        return self.generar_acta()

    def generar_acta(self,bool_value):
        if bool_value == True: return True
        else: return False
    
    def crear_nueva_acta(self):
        acta = Acta()
        return acta
