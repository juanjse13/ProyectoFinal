import streamlit as st
def definir_layout_Asistente(st):
    pass
##TODO: Revisar todo el view
def modificar_criterio:
    lista_criterios = Controlador.get_criterios() #Se trae la lista de criterios
    # identificador = st.selectbox(
    #   'Seleccione el criterio que desea modificar',
    #    (for valor in lista_criterios.values(),)

    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")


    enviado_btn = st.button("Submit")

    if enviado_btn:
        Controlador.cambiar_criterio(identificador, descripcion, ponderacion)
        st.write("Criterio modificado exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

def adicionar_criterio:
    identificador = len(Controlador.get_criterios()) #Permite dar un identificador al nuevo criterio
    descripcion = st.text_input("Descripción")
    ponderacion = st.text_input("Ponderación")

    enviado_btn = st.button("Submit")

    if enviado_btn:
        Controlador.agregar_nuevo_criterio(identificador, descripcion, ponderacion)
        st.write("Criterio creado exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller





