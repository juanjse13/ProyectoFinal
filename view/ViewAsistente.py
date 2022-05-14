from datetime import datetime


def definir_layout_asistente(st, controller, asistente):
    crear_acta_nueva(st, controller, asistente)


def crear_acta_nueva(st, controller, asistente):
    fecha = datetime.today().strftime('%Y-%m-%d')
    periodo = st.text_input("Cual Periodo: XXXX-1 o XXXX-2?")
    autor = st.text_input("Autor")
    nombre_estudiante = st.text_input("Nombre del estudiante")
    identificacion_estudiante = st.text_input("Cédula del estudiante")
    nombre_trabajo = st.text_input("Nombre del trabajo")
    modalidad = st.selectbox(
        '¿Cuál es su tipo de tesis?',
        ('Investigación', 'Aplicado'))

    diccionario_directores = controller.get_directores()  #Se trae el diccionario de directores
    diccionario_jurados = controller.get_jurados()  #Se trae el diccionario de directores

    box_jurado1 = st.selectbox(
        'Seleccione al primer de los jurados',
        diccionario_jurados.keys()
        )
    box_jurado2 = st.selectbox(
        'Seleccione al segundo de los jurados',
        diccionario_jurados.keys()
        )
    box_director = st.selectbox(
        'Seleccione al director',
        diccionario_directores.keys()
        )

    #TODO: revisar cómo se puede poner la opción de que no haya codirector
    box_codirector = st.selectbox(
        'Seleccione al codirector',
        diccionario_directores.keys()
        )
    #Se busca en los diccionarios la instancia respectiva
    jurado1 = diccionario_jurados[box_jurado1]
    jurado2 = diccionario_jurados[box_jurado2]
    director = diccionario_directores[box_director]
    codirector = diccionario_directores[box_codirector]

    enviado_btn2 = st.button("Crear Acta")

    if enviado_btn2:
        controller.agregar_acta(fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante,
                                 identificacion_estudiante,
                                 director, codirector, jurado1, jurado2, asistente) ##Debe indicarse cual fue el asistente que creo el acta
        st.write("Acta agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

