[![Build Status](https://travis-ci.org/UlmBlois/Aircraft-Registration.svg?branch=master)](https://travis-ci.org/UlmBlois/Aircraft-Registration)

# Aircraft-Registration

Simple international aircraft registration code validator.

## Usage

```python
from aircraft_registration.registration import RegistrationNumber

code = ResgistratonNumber('F-JABC')

code.is_valid()

```

## TODO

* extract aircraft type (microlight, glider, militarily, ...) when possible; ie: when they can be differentiate by a code pattern
