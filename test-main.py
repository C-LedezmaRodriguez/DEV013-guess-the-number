"""test guess the number"""
import unittest
from main import secretNum, userGuess, compGuess, gameAttempts

class TestGuessGame(unittest.TestCase):

    def setUp(self):
        """Número de pruebas"""
        self.secret_number = 42
        
    def test_gameAttempts(self):
        """ Probamos que la función gameAttempts devuelva los resultados esperados"""
        self.assertEqual(gameAttempts(50, self.secret_number), (False, "Your number is higuer, keep trying"))
        self.assertEqual(gameAttempts(42, self.secret_number), (True, "Congratulations, you guessed the number!"))
        self.assertEqual(gameAttempts(30, self.secret_number), (False, "Your number is lower, keep trying"))

if __name__ == '__main__':
    unittest.main()
