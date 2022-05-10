#from Directorio.Directorio import Directorio
#from Detalle_Criterio.DetalleCriterio import DetalleCriterio
from Criterio import Criterio
from Usuario import Usuario 
import exepciones_criterio as exe

class Director(Usuario):
    def __init__(self,nombre,contrasena,identificacion):
        Usuario.__init__(self,nombre,contrasena,identificacion)
    
    def ver_actas(self,diccionario_actas):
        for valor in diccionario_actas.values():
            valor.get_acta() 
    
    def ver_actas_identificadas(self,diccionario_actas,numero):
        valor = diccionario_actas[numero]
        return valor.get_acta()

    def ver_promedios():
        pass

    def modificar_criterio(self,criterio,new_ident,new_desc,new_pond):
        try:
            criterio.mod_criterio(new_ident,new_desc,new_pond) # puede cambiar todos los atributos del criterio
        except new_ident == 0:
            new_ident = criterio.get_identificador()
        except new_desc == "":
            new_desc = criterio.get_descripcion()
        except new_pond == 0:
                new_pond = criterio.get_ponderacion()
        
    def agregar_criterio(self,identificador,descripcion,ponderacion):
        criterio = Criterio()
        try:
            criterio.mod_criterio(identificador,descripcion,ponderacion)
        except identificador == 0:
            print("ERROR")

        #except descripcion == "":
            #raise "ERROR"
        #except ponderacion == 0:
            #raise "ERROR"
        
 
        

        
