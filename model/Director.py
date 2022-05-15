
from model.Usuario import Usuario
from model.Criterio import Criterio
"""
La función ver_actas solo esta habilitada en el controlador, y se puede visualizar en la vista del Director, es decir
solo se incluira esta función de ver todas las actas para la vista asignada para el director
"""
class Director(Usuario):
    def __init__(self,nombre,contrasena,identificacion):
        Usuario.__init__(self,nombre,contrasena,identificacion)
    
    def ver_acta(self,diccionario_actas,numero):
        valor = diccionario_actas[numero]
        return valor # Retorna el acta en una clave del diccionario

    def modificar_criterio(self,criterio,new_ident,new_desc,new_pond):
        criterio.mod_criterio(new_ident,new_desc,new_pond)

    def agregar_criterio(self,identificador,descripcion,ponderacion):
        criterio = Criterio()
        criterio.mod_criterio(identificador,descripcion,ponderacion)
        return criterio
 
        

        
