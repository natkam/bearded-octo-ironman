# To run execute py.test roman_to_greek.py
import pytest

ARABIC_AND_ROMAN_NUMBERS = {
  1:'I',
  4:'IV',
  5:'V',
  9:'IX',
  10:'X',
  40:'XL',
  50:'L',
  90:'XC',
  100:'C',
  400:'CD',
  500:'D',
  900:'CM',
  1000:'M'
}

def conversion_factors(number, conversion_dict):
  return  max({item for item in conversion_dict.items() if item[0] <= number})

def arabic_to_roman(number):
  if number > 0:
    arabic, roman = conversion_factors(number,ARABIC_AND_ROMAN_NUMBERS)
    return roman + arabic_to_roman(number - arabic)
  else:
    return ''

TESTED_NUMBERS = {
  0:'',
  1:'I',
  2:'II',
  3:'III',
  4:'IV',
  5:'V',
  6:'VI',
  7:'VII',
  8:'VIII',
  9:'IX',
  10:'X',
  17:'XVII',
  40:'XL',
  50:'L',
  90:'XC',
  100:'C',
  222:'CCXXII',
  400:'CD',
  500:'D',
  900:'CM',
  1000:'M',
  3497:'MMMCDXCVII'
}

@pytest.mark.parametrize('arabic, roman', TESTED_NUMBERS.items())
def test_arabic_to_roman(arabic, roman):
    assert arabic_to_roman(arabic) == roman