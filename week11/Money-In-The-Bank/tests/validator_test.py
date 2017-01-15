import unittest
import sys
sys.path.append("..")
from helpers.validator import (has_capital_letter, has_special_character,
                               has_numeric, is_username_in_password,
                               validate_password)


class TestValidator(unittest.TestCase):

    def setUp(self):
        pass

    def test_has_uppercase_letter(self):
        self.assertTrue(has_capital_letter('Capital'))
        self.assertTrue(has_capital_letter('capiTal'))
        self.assertFalse(has_capital_letter('capital'))

    def test_if_username_is_in_password_as_substring(self):
        self.assertTrue(is_username_in_password('John', 'StrongJohn123'))
        self.assertFalse(is_username_in_password('John', 'NoUsernameHere'))

    def test_has_special_charecter(self):
        self.assertTrue(has_special_character('foo~'))
        self.assertTrue(has_special_character('*foo'))
        self.assertFalse(has_special_character('foo'))

    def test_has_numeric(self):
        self.assertTrue(has_numeric('foo12'))
        self.assertFalse(has_numeric('foo'))

    def test_validate_password(self):
        self.assertTrue(validate_password('John', 'StrongPass12*'))


if __name__ == '__main__':
    unittest.main()
