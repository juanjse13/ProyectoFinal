import unittest
from model.Asistente import Asistente
from model.Jurado import Jurado
from model.Director import Director


class AsistenteTest(unittest.TestCase):

    #Se desea probar el funcionaminento que revise el que varíe el número de actas creadas para un asistente
    def test_get_actas_creadas(self):
        asistente = Asistente("Felipe", 177976968)
        acta = asistente.crear_nueva_acta("2022/10/1", "2022-1", "Juan", "Tesis en IA", "Investigación", "Juan Fernand0", 8945678,
                    Director("Pedro", "10079635"), Director("Andrés", "134325425"), Jurado("Felipe", "1423545"),
                    Jurado("Isabella", "155545"), {})

        self.assertEqual(1, asistente.get_actas_creadas())  # El número de actas creadas debe ser 1 para la instancia asistente creada
if __name__ == '__main__':
    unittest.main()
