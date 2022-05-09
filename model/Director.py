from model.Usuario import Usuario


class Director(Usuario):
    def __init__(self):
        Usuario.__init__()

    def ver_actas(self, diccionario_actas):
        for valor in diccionario_actas.values():
            valor.get_acta()

    def modificar_criterio(self, detalle_criterio):
        detalle_criterio.set_criterio()

    def agregar_criterio(self):
        pass
