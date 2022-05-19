def calificar_tesis(st, controller):
    diccionario_jurados = controller.get_jurados() #Se trae el diccionario que contiene a los jurados
    diccionario_actas = controller.get_actas() #Se trae el diccionario que contiene a todas las actas
    box_jurado = st.selectbox(
        'Seleccione el jurado que va a calificar',
        diccionario_jurados.keys()
    )

    jurado = diccionario_jurados[box_jurado]
    #Para mostrar la información del jurado seleccionado
    st.write('Seleccionaste como jurado a:', jurado.get_nombre())

    for llave in diccionario_actas.keys():
        acta = diccionario_actas[llave]
        if acta.get_jurado1().get_identificacion() == jurado.get_identificacion(): #Se indica el número del jurado que es...
            acta_deseada = acta
            numero_jurado = 1 #Sirve para identificar en qué parte se guardaran las calificaciones y las observaciones
        elif acta.get_jurado2().get_identificacion() == jurado.get_identificacion(): #Se indica el número del jurado que es...
            acta_deseada = acta
            numero_jurado = 2 #Sirve para identificar en qué parte se guardaran las calificaciones y las observaciones
        else:
            st.error("No tiene asociada ninguna acta") ##TODO: Falta la parte de la excepción

    #Para mostrar la información en general
    st.write("Evaluación de acta número: ", acta_deseada.get_numero(), " con tema: ", acta_deseada.get_nombre_trabajo())
    st.write("Fecha: ", acta_deseada.get_fecha())
    st.write("Período:", acta_deseada.get_periodo())
    st.write("Autor: ", acta_deseada.get_autor())
    st.write("Modalidad: ", acta_deseada.get_modalidad())
    st.write("Trabajo presentado por: ", acta_deseada.get_nombre_estudiante())
    st.write("Identificación del estudiante: ", acta_deseada.get_identificacion_estudiante())
    st.write("Director asignado: ", acta_deseada.get_director().get_nombre())
    st.write("Codirector asignado: ", acta_deseada.get_codirector().get_nombre())
    st.write("Primer jurado asignado: ", acta_deseada.get_jurado1().get_nombre())
    st.write("Segundo jurado asignado: ", acta_deseada.get_jurado2().get_nombre())

    #Para la parte de evaluar los criterios
    diccionario_detalles_criterios = acta_deseada.get_detalles_criterios() #Se trae el diccioario de detalles criterios desde la instancia acta

    for llave in diccionario_detalles_criterios.keys():
        detalle_criterio = diccionario_detalles_criterios[llave] #Se va tomando cada instancia detalle_criterio
        st.write("Criterio: ", detalle_criterio.get_criterio().get_identificador()) #Cada detalle criterio tiene un atributo de tipo Criterio
        st.write("Descripción: ", detalle_criterio.get_criterio().get_descripcion())
        st.write("Ponderación: ", detalle_criterio.get_criterio().get_ponderacion())
        nota = st.number_input( key = str(detalle_criterio.get_criterio().get_identificador()), label = "Coloque aquí la nota del criterio" )
        observacion = st.text_input(key = str(detalle_criterio.get_criterio().get_identificador() + 100), label="Coloque aquí la observación     del criterio")
        if numero_jurado == 1:
            acta_deseada.get_detalles_criterios()[llave].set_calificacion1(float(nota))
            acta_deseada.get_detalles_criterios()[llave].set_observacion1(observacion)
        elif numero_jurado == 2:
            acta_deseada.get_detalles_criterios()[llave].set_calificacion2(float(nota))
            acta_deseada.get_detalles_criterios()[llave].set_observacion2(observacion)

    enviado_btn = st.button("Agregar evaluación")

    if enviado_btn:
        nota_parcial = controller.encontrar_nota_parcial_jurado(acta_deseada, numero_jurado)
        st.write("La calificación parcial es: ", nota_parcial)

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller