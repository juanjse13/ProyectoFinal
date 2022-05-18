import streamlit as st
def definir_layout_director(st, controller, director):
    opcion1 = st.button("Modificar criterio")
    opcion2 = st.button("Agregar criterio")
    opcion3 = st.button("Ver actas")

    if opcion1:
        modificar_criterio(st, controller)

    if opcion2:
        adicionar_criterio(st, controller)

    if opcion3:
        observar_actas(st, controller, director)

def modificar_criterio(st, controller):
    lista_criterios = controller.get_criterios() #Se trae la lista de criterios
    lista_prueba = []
    suma = 0
    for criterio in lista_criterios:
        descripcion = st.text_input( value = criterio.get_descripcion() , key = str(criterio.get_identificador()), label = "" )
        criterio.set_descripcion(descripcion)
        ponderacion = st.text_input(value = criterio.get_ponderacion(), key = f'{str(criterio.get_ponderacion())} {str(criterio.get_identificador())}', label = "")
        criterio.set_ponderacion(ponderacion)




    '''identificador = st.selectbox(
        'Seleccione el criterio que desea modificar',
        for valor in lista_criterios:
            lista_criterios[valor]
    )

    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")'''


    enviado_btn = st.button("Modificar")

    if enviado_btn:
        suma = controller.validar_criterio()
        if suma == 1.0:
            st.write("Criterio modificado exitosamente")
        else:
            st.error("Las ponderaciones no dan el 100%")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

def adicionar_criterio(st, controller):
    identificador = len(controller.get_criterios()) #Permite dar un identificador al nuevo criterio
    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")

    enviado_btn = st.button("Agregar")

    if enviado_btn:
        #TODO:Se debe validar las ponderaciones también...para todos los criterios
        controller.agregar_nuevo_criterio(identificador, descripcion, ponderacion)
        st.write("Criterio creado exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def observar_actas(st, controller, director): ##TODO: Terminar observar_actas
    diccionario_actas = controller.get_actas()
    for llave in diccionario_actas.keys():
        acta = diccionario_actas[llave]
        numero_acta, fecha, nombre_estudiante, nota_final, jurado1, jurado2, director, reconocimiento = controller.ver_actas(acta, director)
        with st.expander("Actas creadas"):
            st.write("Acta número", numero_acta)
            st.write("Fecha", fecha)
            st.write("Nombre estudiante", nombre_estudiante)
            st.write("Nota final", nota_final)
            st.write("Jurado 1", jurado1.get_nombre())
            st.write("Jurado 2", jurado2.get_nombre())
            st.write("Director", director.get_nombre())
            st.write("Reconocimiento", reconocimiento)




