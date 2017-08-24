import unittest

from roman_to_arabic import roman_to_arabic


class RomanArabicTestCase(unittest.TestCase):

    def test_roman_to_arabic_simple(self):
        self.assertEqual(roman_to_arabic('I'), 1)
        self.assertEqual(roman_to_arabic('V'), 5)
        self.assertEqual(roman_to_arabic('X'), 10)
        self.assertEqual(roman_to_arabic('L'), 50)
        self.assertEqual(roman_to_arabic('C'), 100)
        self.assertEqual(roman_to_arabic('D'), 500)
        self.assertEqual(roman_to_arabic('M'), 1000)

    def test_roman_to_arabic_complex(self):
        self.assertEqual(roman_to_arabic('III'), 3)
        self.assertEqual(roman_to_arabic('IV'), 4)
        self.assertEqual(roman_to_arabic('VI'), 6)
        self.assertEqual(roman_to_arabic('IX'), 9)
        self.assertEqual(roman_to_arabic('XVIII'), 18)
        self.assertEqual(roman_to_arabic('XXXII'), 32)
        self.assertEqual(roman_to_arabic('LX'), 60)
        self.assertEqual(roman_to_arabic('LIX'), 59)
        self.assertEqual(roman_to_arabic('LXXXIX'), 89)
        self.assertEqual(roman_to_arabic('CCCXXIV'), 324)
        self.assertEqual(roman_to_arabic('DCVII'), 607)
        self.assertEqual(roman_to_arabic('DCXLVIII'), 648)
        self.assertEqual(roman_to_arabic('DCLI'), 651)
        self.assertEqual(roman_to_arabic('MMCDXI'), 2411)

    def test_roman_to_arabic_wrong(self):
        try:
            roman_to_arabic('XY')
        except ValueError:
            pass
        else:
            raise Exception('Wrong format of roman number was not detected /1')
        try:
            roman_to_arabic('IXIII')
        except ValueError:
            pass
        else:
            raise Exception('Wrong format of roman number was not detected /2')

        try:
            roman_to_arabic('XIIII')
        except ValueError:
            pass
        else:
            raise Exception('Wrong format of roman number was not detected /3')

        try:
            roman_to_arabic('XIIV')
        except ValueError:
            pass
        else:
            raise Exception('Wrong format of roman number was not detected /4')

if __name__ == '__main__':
    unittest.main()
