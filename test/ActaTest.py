import unittest
from model.Acta import Acta
from model.Jurado import Jurado
from model.Director import Director



class ActaTest(unittest.TestCase):
    #Se desea probar el funcionaminento del método que define el reconocimiento dada una nota
    def test_set_reconocimiento(self):
        acta = Acta(0, "2022/10/1", "2022-1", "Juan", "Tesis en IA", "Investigación", "Juan Fernand0", 8945678,
                    Director("Pedro", "10079635"), Director("Andrés", "134325425"), Jurado("Felipe", "1423545"),
                    Jurado("Isabella", "155545"), {})
        acta.set_reconocimiento(5)
        self.assertEqual("Alto", acta.get_reconocimiento())  # add assertion here

if __name__ == '__main__':

    unittest.main()
