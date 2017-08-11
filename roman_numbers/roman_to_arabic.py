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
MAP_ROMAN = dict(TUPLE_ROMAN)

DEBUG = False


def print_debug(*values):
    if DEBUG:
        print(*values)


def roman_to_arabic(roman):
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