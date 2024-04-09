"""test guess the number"""
import unittest
from unittest.mock import patch
# import io
from main import secret_num, user_guess, comp_guess, game_attempts

class TestGuessGame(unittest.TestCase):
    """Clase de pruebas unitarias para guess the number"""
    def setUp(self):
        """Número de pruebas"""
        self.secret_number = 42
        self.valid_input = '50'
        self.invalid_input = ['abc','101','50']

    def test_secret_num(self):
        """Número secreto entre 1 y 100"""
        secret_number = secret_num()
        self.assertTrue(1 <= secret_number <= 100)

    # @patch('builtins.input', return_value='42')
    def test_user_guess_valid_input(self):
        """Prueba de la función userGuess con una entrada válida"""
        with patch('builtins.input', return_value=  self.valid_input):
            user_input = user_guess()
        self.assertEqual(user_input,int(self.valid_input))

    def test_user_guess_invalid_input(self):
        """Prueba de la función userGuess con entradas inválidas"""
        with patch('builtins.input', side_effect = self.invalid_input):
            with patch('builtins.print') as mock_print:
                user_input = user_guess()
                mock_print.assert_called_with("Please enter a number between 1 and 100")
        self.assertEqual(user_input, 50)

    def test_comp_guess(self):
        """Número secreto entre 1 y 100"""
        min_num = 1
        max_num = 100
        comp_guess_number = comp_guess(min_num, max_num)
        self.assertTrue(min_num <= comp_guess_number <= max_num)

    def test_game_attempts(self):
        """ Probamos que la función gameAttempts devuelva los resultados esperados"""
        self.assertEqual(game_attempts(50, self.secret_number),
                         (False, "Your number is higuer, keep trying"))
        self.assertEqual(game_attempts(42, self.secret_number),
                         (True, "Congratulations, you guessed the number!"))
        self.assertEqual(game_attempts(30, self.secret_number),
                         (False, "Your number is lower, keep trying"))

if __name__ == '__main__':
    unittest.main()
