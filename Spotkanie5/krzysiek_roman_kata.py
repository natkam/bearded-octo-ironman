import pytest

CONVERSIONS = {
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

def conversion_factors_for(arabic_number):
    if arabic_number not in CONVERSIONS:
        return  conversion_factors_for(arabic_number - 1)
    return arabic_number, CONVERSIONS[arabic_number]

def convert(arabic_number):
    if arabic_number > 0:
        return conversion_factors_for(arabic_number)[1] + convert(arabic_number - conversion_factors_for(arabic_number)[0])
    return ''

def test_convert_with_zero():
    assert convert(0) == ''

NUMBERS = [
    (1, 'I'),
    (2, 'II'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (42, 'XLII'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (500, 'D'),
    (400, 'CD'),
    (900, 'CM'),
    (1000, 'M'),
    (1764, 'MDCCLXIV'),
]

@pytest.mark.parametrize('input, expected', NUMBERS)
def test_convert_with_numbers(input, expected):
    assert convert(input) == expected
