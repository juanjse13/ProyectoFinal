import streamlit as st
from pydataxm.pydataxm import ReadDB
from streamlit_option_menu import option_menu
from controller.Controlador import Controlador
from view.ViewAsistente import definir_layout_asistente



class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.usuario_actual = ""
            self.contraseña_actual = ""
            self.tipo_usuario_actual = ""
            # Inicialización de las variables necesarias

            # Conexión con el controlador
            self.controller = Controlador()

            st.session_state['main_view'] = self
        else:
            # Al exisir en la sesión entonces se actualizan los valores
            self.usuario_actual = st.session_state.main_view.usuario_actual
            self.contraseña_actual = st.session_state.main_view.contraseña_actual
            self.tipo_usuario_actual = st.session_state.main_view.tipo_usuario_actual
            self.controller = st.session_state.main_view.controller
             # Carga de las variables necesarias

        self._inicialializar_layout()

    def _inicialializar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Sistema de información para la evaluación de trabajos de grado de maestría", page_icon='', layout="wide")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        self.usuario_actual = st.number_input("Escriba su número de identificación")
        self.contraseña_actual = st.number_input("Escriba su contraseña")
        self.tipo_usuario_actual = st.selectbox(
            '¿Qué tipo de usuario eres?',
            ('Asistente', 'Jurado', 'Director'))

        enviado_btn = st.button("Submit")


        # Define lo que abrá en la barra de menu
        #with st.sidebar:
         #   self.menu_actual = option_menu("Menu", ["About", '[OtroMenu]Mi Menu'],
          #                                 icons=['house', 'gear'], menu_icon="cast", default_index=1)

        if enviado_btn:
            self.controlar_menu(self.controller)
        # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
        # entonces de esta manera se actualiza el controlador en la vista principal
        return self.controller


    def controlar_menu(self, controller):
        # Filtro opciones de menu
        if self.tipo_usuario_actual == "Asistente":
           diccionario_asistentes = self.controller.get_asistentes()
           if diccionario_asistentes.get(self.usuario_actual): # Si el número de identificación existe en el diccionario de asistentes
               if diccionario_asistentes[self.usuario_actual].get_contrasena() == self.contraseña_actual: #Si al clave que mete es la misma que está previamente guardada en el usuario
                ##Código que diriga al ViewAsistente
                asistente = diccionario_asistentes[self.usuario_actual] #Se trae la instancia particular de asistente donde la llave es el numero de id
                definir_layout_asistente(st, controller, asistente) #Aqui tiene que pasar tanto a la instancia controlador como a la instancia asistente
               else:
                   st.error("La contraseña no coincide")
           else:
               st.error("El usuario no se encuentra definido")

        elif self.tipo_usuario_actual == "Jurado":
            diccionario_jurados = self.controller.get_asistentes()
            if diccionario_jurados.get(self.usuario_actual):  # Si el número de identificación existe en el diccionario de jurados
                if diccionario_jurados[self.usuario_actual].get_contrasena() == self.contraseña_actual:  # Si al clave que mete es la misma que está previamente guardada en el usuario
                    ##Código que diriga al ViewJurados
                    jurado = diccionario_jurados[self.usuario_actual]  # Se trae la instancia particular de jurado donde la llave es el numero de id
                    st.write("Soy Jurado")
                else:
                    st.error("La contraseña no coincide")
            else:
                st.error("El usuario no se encuentra definido")

        elif self.tipo_usuario_actual == "Director":
            diccionario_directores = self.controller.get_asistentes()
            if diccionario_directores.get(self.usuario_actual):  # Si el número de identificación existe en el diccionario de directores
                if diccionario_directores[self.usuario_actual].get_contrasena() == self.contraseña_actual:  # Si al clave que mete es la misma que está previamente guardada en el usuario
                    ##Código que diriga al ViewDirectores
                    director = diccionario_directores[self.usuario_actual]  # Se trae la instancia particular de director donde la llave es el numero de id
                    st.write("Soy Director")
                else:
                    st.error("La contraseña no coincide")
            else:
                st.error("El usuario no se encuentra definido")



# Main call
if __name__ == "__main__":
    gui = MainView()

