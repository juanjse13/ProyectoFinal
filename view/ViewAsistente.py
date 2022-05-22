from datetime import datetime


def crear_acta_nueva(st, controller):
    diccionario_asistentes = controller.get_asistentes()
    box_asistente = st.selectbox(
        'Seleccione el asistente que va a crear el acta',
        diccionario_asistentes.keys()
    )
    asistente = diccionario_asistentes[box_asistente]
    #Para mostrar la información del asistente seleccionado
    st.write('Seleccionaste como asistente a:', asistente.get_nombre())
    fecha = datetime.today().strftime('%Y-%m-%d')
    try:
        periodo = st.text_input("Cual Periodo: XXXX-1 o XXXX-2?")
        autor = st.text_input("Autor")
        nombre_estudiante = st.text_input("Nombre del estudiante")
        identificacion_estudiante = st.text_input("Cédula del estudiante")
        nombre_trabajo = st.text_input("Nombre del trabajo")
    except ValueError:
        st.error("No es posible asignar")
    modalidad = st.selectbox(
        '¿Cuál es su tipo de tesis?',
        ('Investigación', 'Aplicado'))

    diccionario_directores = controller.get_directores()  #Se trae el diccionario de directores
    diccionario_jurados = controller.get_jurados()  #Se trae el diccionario de directores

    box_jurado1 = st.selectbox(
        'Seleccione al primer de los jurados',
        diccionario_jurados.keys()
        )
    jurado1 = diccionario_jurados[box_jurado1]
    #Para mostrar la información del jurado seleccionado
    st.write('Seleccionaste como 1° jurado a:', jurado1.get_nombre())

    box_jurado2 = st.selectbox(
        'Seleccione al segundo de los jurados',
        diccionario_jurados.keys()
        )
    jurado2 = diccionario_jurados[box_jurado2]
    st.write('Seleccionaste como 2° jurado a:', jurado2.get_nombre())

    box_director = st.selectbox(
        'Seleccione al director',
        diccionario_directores.keys()
        )
    director = diccionario_directores[box_director]
    st.write('Seleccionaste como director a:', director.get_nombre())

    box_codirector = st.selectbox(
        label = 'Seleccione al codirector',
        options = diccionario_directores.keys()
        )
    codirector = diccionario_directores[box_codirector]
    st.write('Seleccionaste como codirector a:', codirector.get_nombre())


    enviado_btn2 = st.button("Crear Acta")

    if enviado_btn2:
        controller.agregar_acta(fecha, periodo, autor, nombre_trabajo, modalidad, nombre_estudiante,
                                 identificacion_estudiante,
                                 director, codirector, jurado1, jurado2, asistente) ##Debe indicarse cual fue el asistente que creo el acta
        st.write("Acta agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller