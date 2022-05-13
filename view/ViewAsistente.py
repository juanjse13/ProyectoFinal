from datetime import datetime
from controller.Controlador import Controlador
import json
def definir_layout_Asistente(st):
    pass


def crear_acta_nueva(st):
    fecha = datetime.today().strftime('%Y-%m-%d')
    autor = st.text_input("Autor")
    nombre = st.text_input("Nombre del estudiante")
    identificación_estudiante = st.text_input("Cédula del estudiante")
    modalidad = st.selectbox(
        '¿Cuál es su tipo de tesis?',
        ('Investigación', 'Aplicado'))

    diccionario_directores = Controlador.get_directores()  #Se trae el diccionario de directores
    diccionario_jurados = Controlador.get_jurados()  #Se trae el diccionario de directores


    ##TODO: Buscar cómo traer los valores y ponerlos en un selectbox
    #jurado1 = st.selectbox(
     #   'Seleccione al primer de los jurados',
    #    (for valor in diccionario_directores.values(),)
    #jurado2 = st.selectbox(
    #    'Seleccione al primer de los jurados',
    #    (for valor in diccionario_directores.values(),)
    #director = st.selectbox(
    #    'Seleccione al primer de los jurados',
    #    (for valor in diccionario_directores.values(),)

    #codirector = st.selectbox(
    #    'Seleccione al primer de los jurados',
    #    (for valor in diccionario_directores.values(),)

    enviado_btn = st.button("Submit")

    if enviado_btn:
        Controlador.agregar_acta(numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante,
                                 identificacion_estudiante,
                                 director, codirector, jurado1, jurado2)
        st.write("Acta agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller







    def __init__(self, numero, fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante,
                 identificacion_estudiante,
                 director, codirector, jurado1, jurado2):


