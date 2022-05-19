import streamlit as st
from pydataxm.pydataxm import ReadDB
from streamlit_option_menu import option_menu
from controller.Controlador import Controlador
from view.ViewAsistente import crear_acta_nueva
from view.ViewDirector import modificar_criterio,  adicionar_criterio, observar_actas
from view.ViewJurado import calificar_tesis


class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"
            # Inicialización de las variables necesarias

            # Conexión con el controlador
            self.controller = Controlador()

            st.session_state['main_view'] = self

        else:
            # Al exisir en la sesión entonces se actualizan los valores
            self.controller = st.session_state.main_view.controller
            self.menu_actual = st.session_state.main_view.menu_actual

        self._inicialializar_layout()

    def _inicialializar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Sistema de calificación de tesis", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["Inicio", 'Asistentes(Crear Acta)', 'Jurados', 'Directores(Ver actas)', "Directores(Modificar criterio)", "Directores(Agregar criterio)"],
                                           icons=['house', 'gear'], menu_icon="cast", default_index=1)


    def controlar_menu(self):
        if self.menu_actual == "Inicio":
            print("AAA")
        elif self.menu_actual == "Asistentes(Crear Acta)":
            crear_acta_nueva(st, self.controller)
        elif self.menu_actual == "Jurados":
            print("AAA")
            #agregar_evaluacion(st, self.controller)
        elif self.menu_actual == "Directores(Ver actas)":
            observar_actas(st, self.controller)
        elif self.menu_actual == "Directores(Modificar criterio)":
            modificar_criterio(st, self.controller)
        elif self.menu_actual == "Directores(Agregar criterio)":
            adicionar_criterio(st, self.controller)

# Main call
if __name__ == "__main__":
    gui = MainView()
    gui.controlar_menu()

