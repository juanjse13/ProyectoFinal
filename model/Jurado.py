import Usuario 
from DetalleCriterio import DetalleCriterio

"""
Debe haber un atributo en las actas que permita saber el estado del acta,
Estado sin exportar, Estado en proceso, Estado Exportado. Esto se hace mediante
dos atributos en cada clase acta, que tengan por nombre, exportacion1 y exportacion2
si las dos estan en False, el estado del acta es sin exportar, si una de las
exportaciones es True el acta esta en proceso, y si las dos exportaciones son True
el estado es exportado. Esto con el fin de poder exportar a PDF las actas que estan en
estado Exportado
"""
# def mod_criterio(self,new_identificador,new_descripcion,new_ponderacion
class Jurado(Usuario):
    def __init__(self,name,identificacion,password):
        Usuario.__init__(self,name,identificacion,password)

    def exportar_acta(self,acta):    
        acta.exportar() # Debe verificar estado del acta
        return acta

    def evaluar(self,calificacion):
        return calificacion




