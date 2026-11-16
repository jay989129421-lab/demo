"""Assignment 5: PAN number validation using regular expression.
Format: AAAAA9999A  (5 capital letters, 4 digits, 1 capital letter)"""

import re

PAN_PATTERN = r"^[A-Z]{5}[0-9]{4}[A-Z]$"


def is_valid_pan(pan):
    return re.fullmatch(PAN_PATTERN, pan) is not None


pan = input("Enter PAN number: ").strip()

if is_valid_pan(pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
