# EX 3.11 Write a function to validate a given phone number.
# Write a function validate_phone(tmp_str) to validate a given phone number.
# Test data:
# Input: ab122
# Output: False
# Test data:
# Input: 0932095456
# Output: True
# Test data:
# Input: 02836229888
# Output: True
import re
a = input()
def validate_phone(tmp_str):
    return tmp_str.isnumeric()
print(validate_phone(a),end='')
