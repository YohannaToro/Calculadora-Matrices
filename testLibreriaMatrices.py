import libreriaMatrices
import unittest


class TestCalculadoraMatrices(unittest.TestCase):
    def test_suma_matrices(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = libreriaMatrices.suma_matrices([[[3,7],[5,-2]],[[1,8],[13,2]]],[[[-5,-6],[-9,2]],[[2,5],[-12,-9]]])
        self.assertEqual(result, [[(-2, 1), (-4, 0)], [(3, 13), (1, -7)]])
    def test_sMultiplicacionEscala_matrices(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = libreriaMatrices.multiplicacion_escalar_matrices((3,1),[[(13,2),(1,0),(4,8)]])
        self.assertEqual(result,[[(37, 19), (3, 1), (4, 28)]] )
   

if __name__ == '__main__':
    unittest.main()

