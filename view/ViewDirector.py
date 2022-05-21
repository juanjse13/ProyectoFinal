def validar_criterio(st, controller): #Método que va a permitir sacar un warning o no de ser el caso
    suma = controller.validar_criterios()
    if  1.0 >= suma >= 0.999:
        st.write("Criterio modificado exitosamente")
    else:
        st.error("Las ponderaciones no dan el 100%")
    st.write("Las ponderaciones dan", suma * 100, " %")


def modificar_criterio(st, controller):
    lista_criterios = controller.get_criterios() #Se trae la lista de criterios
    for criterio in lista_criterios:
        st.write("Criterio ", criterio.get_identificador())
        descripcion = st.text_input( value = criterio.get_descripcion() , key = str(criterio.get_identificador()), label = "" )
        criterio.set_descripcion(descripcion)
        ponderacion = st.text_input(value = criterio.get_ponderacion(), key = f'{str(criterio.get_ponderacion())} {str(criterio.get_identificador())}', label = "")
        criterio.set_ponderacion(float(ponderacion)) #Es necesario convertir el string a float

    enviado_btn = st.button("Modificar")

    if enviado_btn:
        validar_criterio(st, controller)


    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

#TODO: Falta adicionar criterio
def adicionar_criterio(st, controller):
    identificador = len(controller.get_criterios()) #Permite dar un identificador al nuevo criterio
    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")

    enviado_btn = st.button("Agregar")

    if enviado_btn:
        st.write(identificador)
        st.write(descripcion)
        st.write(ponderacion)
        controller.agregar_nuevo_criterio(identificador, descripcion, float(ponderacion))
        #Es necesario modificar las ponderaciones de los otros criterios después de haber creado el nuevo criterio
        modificar_criterio(st, controller)

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def observar_actas(st, controller):
    diccionario_directores = controller.get_directores() #Se traen a los directores
    box_director = st.selectbox(
        'Seleccione el director que desea ver las actas',
        diccionario_directores.keys()
    )
    director = diccionario_directores[box_director]
    #Para mostrar la información del jurado seleccionado
    st.write('Seleccionaste como director a:', director.get_nombre())

    diccionario_actas = controller.get_actas() #Se traen las actas
    for llave in diccionario_actas.keys():
        acta = diccionario_actas[llave]
        if acta.get_director().get_identificacion() == director.get_identificacion() and acta.get_estado_acta() == "Terminado": # Si el acta tiene como director al seleccionado...
            numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento = controller.ver_actas(acta, director)
            nota_final = controller.hallar_nota_final(acta)
            with st.expander("Actas creadas"):
                st.write("Acta número: ", numero_acta)
                st.write("Fecha: ", fecha)
                st.write("Nombre estudiante: ", nombre_estudiante)
                st.write("Nota final", nota_final)
                st.write("Nombre del jurado 1: ", jurado1.get_nombre())
                st.write("Nombre del jurado 2: ", jurado2.get_nombre())
                st.write("Nombre del director: ", director.get_nombre())
                st.write("Reconocimiento: ", acta.get_reconocimiento())
                st.write("Observaciones generales ", acta.get_observaciones_generales1())
                st.write("Observaciones generales ", acta.get_observaciones_generales2())










