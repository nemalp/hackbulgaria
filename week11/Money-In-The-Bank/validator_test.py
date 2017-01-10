import unittest
import validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        pass

    def test_has_uppercase_letter(self):
        self.assertTrue(validator.has_capital_letter('Capital'))
        self.assertTrue(validator.has_capital_letter('capiTal'))
        self.assertFalse(validator.has_capital_letter('capital'))

    def test_if_username_is_in_password_as_substring(self):
        self.assertTrue(validator.is_username_in_password('John',
                                                          'StrongJohn123'))
        self.assertFalse(validator.is_username_in_password('John',
                                                           'NoUsernameHere'))

    def test_has_special_charecter(self):
        self.assertTrue(validator.has_special_character('foo~'))
        self.assertTrue(validator.has_special_character('*foo'))
        self.assertFalse(validator.has_special_character('foo'))

    def test_has_numeric(self):
        self.assertTrue(validator.has_numeric('foo12'))
        self.assertFalse(validator.has_numeric('foo'))

    def test_validate_password(self):
        self.assertTrue(validator.validate_password('John', 'StrongPass12*'))


if __name__ == '__main__':
    unittest.main()
