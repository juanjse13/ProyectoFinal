from model.Usuario import  Usuario
from model.PDF_fpdf import PDF


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
    def __init__(self, nombre, identificacion):
        Usuario.__init__(self, nombre, identificacion)

    def exportar_acta_PDF(self, acta):
        file = open("Acta.txt", "w")
        file.write(f'Numero del acta : {acta.get_numero()}')
        file.write(f'Fecha : {acta.get_fecha()}')
        file.write(f'Periodo : {acta.get_periodo()}')
        file.write(f'Autor : {acta.get_autor()}')
        file.write(f'Nombre del Trabajo : {acta.get_nombre_trabajo()}')
        file.write(f'Modalidad : {acta.get_modalidad()}')
        file.write(f'Estado del acta : {acta.get_estado_acta()}')
        file.write(f'Nombre del Estudiante : {acta.get_nombre_estudiante()}')
        file.write(f'Identificación del Estudiante : {acta.get_identificacion_estudiante()}')
        file.write(f'Director : {acta.get_director().get_nombre()}')
        file.write(f'Codirector : {acta.get_codirector().get_nombre()}')
        file.write(f'Jurado : {acta.get_jurado1().get_nombre()}')
        file.write(f'Jurado : {acta.get_jurado2().get_nombre()}')
        file.write(f'Nota Final : {acta.get_nota_final()}')
        file.write(f'Reconocimiento : {acta.get_reconocimiento()}')
        file.write(f'Reconocimiento : {acta.get_reconocimiento()}')
        pdf = PDF()
        pdf.add_page()
        pdf.texts('Acta.txt')
        pdf.titles(f'ACTA IDENTIFICADA CON EL NÚMERO :  {acta.get_numero()}')
        pdf.set_author(acta.get_autor())
        pdf.output('Acta exportada.pdf', 'F')
        return acta







