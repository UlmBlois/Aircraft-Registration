import re

from .data import PATTERNS_DICT


class RegistrationNumber:
    """Given a registration code, extract the associate validator and validate it."""

    def __init__(self, number=''):
        self.number = number
        if len(number) > 0:
            self.validator = Validator.fromNumber(number)
        else:
            raise ValueError("Empty registration number.")

    def is_valid(self):
        """Test if the registration code is valid.

        ie: match one of the patterns of the prefix."""
        return self.validator.validate(self.number)


class Validator:
    """Helper class extrating the prefix of a registration code"""
    """and validate it against his associate patterns."""

    def __init__(self, prefix='', patterns=[]):
        self.prefix = prefix
        self.patterns = patterns

    @classmethod
    def fromNumber(cls, number):
        key_max_size = 0
        key_best_match = ''
        for key, patterns in PATTERNS_DICT.items():
            if number.startswith(key):
                if key_max_size < len(key):
                    key_max_size = len(key)
                    key_best_match = key
        if not key_best_match:
            raise ValueError(
                ('Cannot match registration number '
                 '"{}" with any know prefix.'.format(number)
                 ))
        return cls(key_best_match, PATTERNS_DICT[key_best_match])

    def validate(self, number):
        for p in self.patterns:
            if re.match(self.prefix+p, number):
                return True
        return False

    @staticmethod
    def pattern_to_str(pattern):
        """Convert the given regex pattern into a string representation.

        ex: 'J[A-Za-z][A-Za-z][A-Za-z]$' -> 'Jabc'"""
        alpha = re.compile(r'\[A-Za-z\]|\[a-zA-Z\]')
        num = '[0-9]'
        alpha_count = ord('a')
        num_count = 1
        has_alpha = True
        has_num = True
        pattern = pattern.replace('$', '')
        while has_num or has_alpha:
            if has_alpha:
                tmp_str = alpha.sub(chr(alpha_count), pattern,  1)
                if tmp_str == pattern:
                    has_alpha = False
                else:
                    alpha_count += 1
                    pattern = tmp_str
            if has_num:
                tmp_str = pattern.replace(num, str(num_count), 1)
                if tmp_str == pattern:
                    has_num = False
                else:
                    num_count += 1
                    pattern = tmp_str
        return pattern

    def __str__(self):
        str = [self.pattern_to_str(self.prefix + x)for x in self.patterns]
        return ', '.join(str)
