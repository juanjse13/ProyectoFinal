from model.PDF_fpdf import PDF

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

    contador_aux = 3 #Sirve para luego generar una llave única que identifique "observaciones_generales"
    for llave1 in diccionario_actas.keys():
        contador_aux += 1
        acta = diccionario_actas[llave1]
        if acta.get_jurado1() == jurado and acta.get_estado_acta != "Terminado":       #Se indica el número del jurado que es...
            acta_deseada = acta
            numero_jurado = 1 #Sirve para identificar en qué parte se guardaran las calificaciones y las observaciones
        elif acta.get_jurado2() == jurado and acta.get_estado_acta != "Terminado":  #Se indica el número del jurado que es...
            acta_deseada = acta
            numero_jurado = 2 #Sirve para identificar en qué parte se guardaran las calificaciones y las observaciones
        else:
            st.error("No tiene asociada ninguna acta") ##TODO: Falta la parte de la excepción

        with st.expander("Acta:"):
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
            contador = 1
            for llave in diccionario_detalles_criterios.keys():
                contador += 1
                detalle_criterio = diccionario_detalles_criterios[llave] #Se va tomando cada instancia detalle_criterio
                st.write("Criterio: ", detalle_criterio.get_criterio().get_identificador()) #Cada detalle criterio tiene un atributo de tipo Criterio
                st.write("Descripción: ", detalle_criterio.get_criterio().get_descripcion())
                st.write("Ponderación: ", detalle_criterio.get_criterio().get_ponderacion())
                nota = st.number_input( key = str(contador) + str(llave1) + "nota", label = "Coloque aquí la nota del criterio" )
                observacion = st.text_input( key = str(contador) + str(llave1) + "abs", label="Coloque aquí la observación     del criterio")
                if numero_jurado == 1:
                    acta_deseada.get_detalles_criterios()[llave].set_calificacion1(float(nota))
                    acta_deseada.get_detalles_criterios()[llave].set_observacion1(observacion)
                elif numero_jurado == 2:
                    acta_deseada.get_detalles_criterios()[llave].set_calificacion2(float(nota))
                    acta_deseada.get_detalles_criterios()[llave].set_observacion2(observacion)
            observaciones_generales = st.text_input(label = "Observaciones generales", key = str(llave + contador + contador_aux))

            if numero_jurado == 1:
                acta_deseada.set_observaciones_generales1(observaciones_generales)
            elif numero_jurado == 2:
                acta_deseada.set_observaciones_generales2(observaciones_generales)


            enviado_btn = st.button(label = "Agregar evaluación", key= str(llave1))

    if enviado_btn:
        nota_parcial = controller.encontrar_nota_parcial_jurado(acta_deseada, numero_jurado)
        estado = controller.cambiar_estado_acta(acta_deseada)
        acta_deseada.set_estado_acta(estado) #Para cambiar el valor del estado de la instancia
        st.write("La calificación parcial es: ", nota_parcial)

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def exportar_acta(st, controller):
    diccionario_jurados = controller.get_jurados()  # Se trae el diccionario que contiene a los jurados
    diccionario_actas = controller.get_actas()
    box_jurado = st.selectbox(
        'Seleccione el jurado que va a exportar',
        diccionario_jurados.keys()
    )

    jurado = diccionario_jurados[box_jurado]
    # Para mostrar la información del jurado seleccionado
    st.write('Seleccionaste como jurado a:', jurado.get_nombre())

    actas_disponibles = {}
    for llave1 in diccionario_actas.keys():
        acta_deseada = diccionario_actas[llave1]
        if (acta_deseada.get_jurado1().get_identificacion() == jurado.get_identificacion() or acta_deseada.get_jurado2().get_identificacion() == jurado.get_identificacion()) and acta_deseada.get_estado_acta != "Terminado":       #Se indica el número del jurado que es...
            actas_disponibles[acta_deseada.get_numero()] = acta_deseada ##Recorra todas las actas y vea cuáles podría exportar

    box_actas = st.selectbox(
        'Seleccione el acta que quiere exportar',
        actas_disponibles.keys()
    )

    acta_a_exportar = actas_disponibles[box_actas]
    # Para mostrar la información del jurado seleccionado
    st.write('Seleccionaste como acta a exportar la acta: ', acta_a_exportar.get_numero(), " con tema:", acta_a_exportar.get_nombre_trabajo())
    enviado_btn = st.button("Exportar acta")

    if enviado_btn:
        #TODO: Falta hacer la función que cree el pdf en controlador y que interactua con el modelo
        ##TODO: excepción que indique que si no hay ningún acta creada, no es posible exportar algo

        exportar_acta_PDF(acta_a_exportar)
        st.write("El acta fue exportada")

def exportar_acta_PDF(acta):
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
