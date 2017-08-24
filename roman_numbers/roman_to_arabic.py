"""
Roman numbers to arabic converter.

LICENSE: MIT
Author: Ruslan Khalikov <khalikoff@gmail.com>
"""

# class RomanNumbers():
from collections import defaultdict

TUPLE_ROMAN = (
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
)
TUPLE_ADDITIONAL = (
    ('G', 4),
    ('J', 9),
    ('K', 40),
    ('Z', 90),
    ('B', 400),
    ('N', 900),
)
MAP_INITIAL = dict(TUPLE_ROMAN)
TUPLE_NEW = TUPLE_ROMAN + TUPLE_ADDITIONAL
MAP_ROMAN = dict(TUPLE_NEW)
REVERSED_MAP = dict([(y, x) for x, y in TUPLE_NEW])
DEBUG = False


def print_debug(*values):
    if DEBUG:
        print(*values)


def roman_to_arabic_previous(roman):
    """
    Converts Roman numbers to Arabic
    from 1 to 3999 including

    roman: string with Roman number
    returns: int (from 1 to 3999)
    """
    result = [0]
    previous_number = 4000
    p_previous_number = 4001
    # we store 2 previous numbers in order to check is
    # this number still correct
    for i, char in enumerate(roman):
        if char in MAP_ROMAN:
            number = MAP_ROMAN[char]
            # Chars in Roman numbers should decrease if not 3 same chars in line
            if p_previous_number <= number and previous_number != number:
                raise ValueError('Wrong Roman Number (...1)')
            if number > previous_number:
                # minus previous number if current > previous
                # IV: 5 - 1, IX: 10 - 1, XC: 100 - 10
                if number % previous_number < 5:
                    sign = -1
                else:
                    raise ValueError('Wrong Roman number (...2)')
            else:
                sign = 1

            print_debug(i, roman, char, number, previous_number, sign)

            result[-1] *= sign
            result.append(number)
            p_previous_number = previous_number
            previous_number = number
        else:
            raise ValueError('Unknown char "%s" in input roman number' % char)
    counts = defaultdict(int)

    # test for same multiple Roman numbers
    for number in result:
        num = abs(number)
        counts[num] += 1
        if counts[num] > 3:
            raise ValueError('Wrong Roman number (...3)')

    return sum(result)


def roman_to_arabic(roman):

    prev_char = ''
    prev_prev_char = ''
    for char in roman:
        # check if illegal characters in roman input
        if char not in MAP_INITIAL:
            raise ValueError('Unknown char "%s" in input roman number' % char)
        # check if roman input is like IXIII
        # excluding XIX (last condition)
        if prev_prev_char == char and char != prev_char and (
            MAP_ROMAN[char] < MAP_ROMAN[prev_char]
        ):
            raise ValueError(
                '"%s%s%s" is invalid' % (prev_prev_char, prev_char, char)
            )
        a = prev_char
        prev_char = char
        prev_prev_char = a


    # replacing additional numbers by unique characters
    new_roman = roman.replace('IV', 'G').replace('IX', 'J').replace(
        'XL', 'K'
    ).replace('XC', 'Z').replace('CD', 'B').replace('CM', 'N')


    previous = 4000
    counts = defaultdict(int)
    for char in new_roman:
        number = MAP_ROMAN[char]
        # given roman input with replaced 4, 9, 40, 90 ...
        # next number cannot be less than current
        if number > previous:
            raise ValueError('"%s" cannot follow "%s"' % (number, previous))
        counts[char] += 1
        previous = number
    # given counts for chars and with other previous conditions
    # count of character of new roman input cannot be more than 3
    for char, k in counts.items():
        if k > 3:
            raise ValueError(
                'character "%s" repeats more than 3 times in row' % char
            )
    result = 0
    for char in new_roman:
        result += MAP_ROMAN[char]
    return result
