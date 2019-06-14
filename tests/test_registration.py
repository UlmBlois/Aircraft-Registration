import unittest
from aircraft_registration.registration import Validator


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
