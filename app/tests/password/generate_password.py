import unittest
import string
from unittest.mock import MagicMock

from app.internal.password.logic.generate_password import GeneratePassword
from app.internal.password.models.generate_password import GeneratePasswordModel

class TestGeneratePassword(unittest.TestCase):

    def setUp(self):
        self.generate_password = GeneratePassword()
        self.specifications = GeneratePasswordModel(
            low_case=True,
            upper_case=True,
            number=True,
            special_char=False,
            length=16
        )

    def test_generate_password_returns_string(self):
        password = self.generate_password.generate_password(self.specifications)
        self.assertIsInstance(password, str)

    def test_generate_password_returns_expected_length(self):
        password = self.generate_password.generate_password(self.specifications)
        self.assertEqual(len(password), self.specifications.length)

    def test_define_alphabet_returns_string(self):
        alphabet = self.generate_password._GeneratePassword__define_alphabet(self.specifications)
        self.assertIsInstance(alphabet, str)

    def test_define_alphabet_returns_expected_characters(self):
        mock_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.generate_password.switcher = {
            "low_case": string.ascii_lowercase,
            "upper_case": string.ascii_uppercase,
            "number": string.digits,
            "special_char": string.punctuation
        }
        self.specifications.special_char = True
        expected_alphabet = mock_alphabet + string.punctuation
        alphabet = self.generate_password._GeneratePassword__define_alphabet(self.specifications)
        self.assertEqual(alphabet, expected_alphabet)

if __name__ == '__main__':
    unittest.main()
