import unittest
from aircraft_registration.registration import Validator, RegistrationNumber


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.valid_number = 'B-HZE'
        self.invalid_prefix = 'ZZ-H12'
        self.invalid_number = 'F-J111'

    def test_fromNumber(self):
        validator = Validator.fromNumber(self.valid_number)
        self.assertNotEqual(validator.prefix, '')
        self.assertNotEqual(validator.patterns, [])

        self.assertRaises(ValueError,
                          Validator.fromNumber, self.invalid_prefix)

    def test_validate_is_valid(self):
        validator = Validator.fromNumber(self.valid_number)
        self.assertTrue(validator.validate(self.valid_number))

    def test_validate_is_invalid(self):
        validator = Validator.fromNumber(self.invalid_number)
        self.assertFalse(validator.validate(self.invalid_number))


class RegistrationNumberTest(unittest.TestCase):

    def setUp(self):
        self.valid_number = 'B-HZE'
        self.invalid_prefix = 'ZZ-H12'
        self.invalid_number = 'F-J111'

    def test_constructor(self):
        try:
            RegistrationNumber(self.valid_number)
        except ValueError:
            self.fail("RegistrationNumber() raised ValueError unexpectedly!")
        self.assertRaises(ValueError, RegistrationNumber, '')

    def test_is_valid(self):
        reg_num = RegistrationNumber(self.valid_number)
        self.assertTrue(reg_num.is_valid())
        reg_num = RegistrationNumber(self.invalid_number)
        self.assertFalse(reg_num.is_valid())
