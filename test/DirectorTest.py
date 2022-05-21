import unittest
from model.Director import Director
from model.Criterio import Criterio


class DirectorTest(unittest.TestCase):

    # Se desea probar el funcionaminento que revise si se modifica un criterio
    def test_modificar_criterio(self):
        criterio = Criterio(0, "Prueba de criterio", 0.01)
        director = Director("Luis", 124058796)
        director.modificar_criterio(criterio, "Nuevo valor", 0.01, 100)



        self.assertEqual(100,criterio.get_identificador())  # 100 es el número identificador previamente cambiado

if __name__ == '__main__':
    unittest.main()
