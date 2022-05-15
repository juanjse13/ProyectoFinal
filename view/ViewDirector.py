import streamlit as st
def definir_layout_director(st, controller, director):
    opcion1 = st.button("Modificar criterio")
    opcion2 = st.butto("Agregar criterio")
    opcion3 = st.button("Ver actas")

    if opcion1:
        modificar_criterio(st, controller)

    if opcion2:
        adicionar_criterio(st, controller)

    if opcion3:
        observar_actas(st, controller)

def modificar_criterio(st, controller):
    lista_criterios = controller.get_criterios() #Se trae la lista de criterios

    #TODO: Ver cómo traer los criterios que están en la lista_criterios
    # identificador = st.selectbox(
    #   'Seleccione el criterio que desea modificar',
    #    (for valor in lista_criterios.values(),)

    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")


    enviado_btn = st.button("Modificar")

    if enviado_btn:
        controller.cambiar_criterio(identificador, descripcion, ponderacion)
        st.write("Criterio modificado exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

def adicionar_criterio(st, controller):
    identificador = len(controller.get_criterios()) #Permite dar un identificador al nuevo criterio
    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")

    enviado_btn = st.button("Agregar")

    if enviado_btn:
        controller.agregar_nuevo_criterio(identificador, descripcion, ponderacion)
        st.write("Criterio creado exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def observar_actas(st, controller):
    pass



