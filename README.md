[![Build Status](https://travis-ci.org/UlmBlois/Aircraft-Registration.svg?branch=master)](https://travis-ci.org/UlmBlois/Aircraft-Registration)
[![Coverage Status](https://coveralls.io/repos/github/UlmBlois/Aircraft-Registration/badge.svg?branch=master)](https://coveralls.io/github/UlmBlois/Aircraft-Registration?branch=master)

# Aircraft-Registration

Simple international aircraft registration code validator.

## Usage

```python
from aircraft_registration.registration import RegistrationNumber

code = RegistrationNumber('F-JABC')

code.is_valid()

```

## TODO

* get country code from prefix
* extract aircraft type (microlight, glider, militarily, ...) when possible; ie: when they can be differentiate by a code pattern
