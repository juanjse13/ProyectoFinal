def calificar_tesis(st, controller, jurado):
    diccionario_actas = controller.get_actas() #Se trae el diccionario que contiene a todas las actas
    for llave1 in diccionario_actas.keys():
        instancia_acta = diccionario_actas[llave1]  ##Va ir seleccionando cada uno de los valores del diccionario
        if jurado.get_identificacion() == instancia_acta.get_jurado1(): #Verificia si el jurado está asociado al acta
            acta_a_calificar = instancia_acta #Como en Python hay paso por referencia de las instancias...
            tipo_jurado= 1
        elif jurado.get_identificacion() == instancia_acta.get_jurado2(): #Verificia si el jurado está asociado al acta
            acta_a_calificar = instancia_acta
            tipo_jurado = 2

    diccionario_detalles_criterios = acta_a_calificar.get_detalles_criterios() #Se trae el diccionario de detalles criterios para la acta respectiva

    lista_calificaciones = []
    lista_observaciones = []

    for llave2 in diccionario_detalles_criterios.keys():
        instancia_detalle_criterio = diccionario_detalles_criterios[llave2]
        st.write("Criterio", llave2)
        st.write("Descripción", instancia_detalle_criterio.get_criterio().get_descripcion())
        st.write("Ponderación", instancia_detalle_criterio.get_criterio().get_ponderacion())
        observacion_criterio = st.text_input("Observación criterio")
        calificacion_criterio = st.number_input("Calificación parcial")
        if tipo_jurado == 1:
            instancia_detalle_criterio.set_calificacion1(calificacion_criterio)
            instancia_detalle_criterio.set_observacion1(observacion_criterio)
        elif tipo_jurado == 2:
            instancia_detalle_criterio.set_calificacion2(calificacion_criterio)
            instancia_detalle_criterio.set_observacion2(observacion_criterio)


    enviado_btn3 = st.button("Agregar calificación")

    if enviado_btn3:

        controller.evaluar_acta(lista_observaciones, lista_calificaciones, tipo_jurado, acta_a_calificar)

    return controller










##Esto de aquí es línea de código a revisar y ver si se debe poner y de ser el caso en que si, analizar dónde se debe poner
    if jurado == acta.get_jurado1():
        for llave, valor in self._detalles_criterios.items():  # Para recorrer el diccionario de detalles_criterios
            acta.get_detalles_criterios()
            self._detalles_criterios[i].get_criterio().get_descripcion()
            self._detalles_criterios[i].set_calificacion1()
    elif jurado == acta.get_jurado2():
        for i in self._detalles_criterios:
            self._detalles_criterios[i].get_criterio().get_descripcion()
            self._detalles_criterios[i].set_calificacion2()
    else:
        raise NotFoundUser("NO JURY FOUND FOR THIS RECORD")