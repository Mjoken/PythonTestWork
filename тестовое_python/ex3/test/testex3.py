from unittest import TestCase, main
from source.main import roman_numerals_to_int


class MyTestCase(TestCase):
    def test(self):
        self.assertEqual(roman_numerals_to_int("VIII"), 8)
        self.assertEqual(roman_numerals_to_int("IV"), 4)
        self.assertEqual(roman_numerals_to_int("XXXVI"), 36)
        self.assertEqual(roman_numerals_to_int("CLXXXIX"), 189)
        self.assertEqual(roman_numerals_to_int(""), 0)

    def testErrors(self):
        self.assertEqual(roman_numerals_to_int("321"), None)
        self.assertEqual(roman_numerals_to_int(43), None)
        self.assertEqual(roman_numerals_to_int("   "), None)
        self.assertEqual(roman_numerals_to_int("vi"), None)
        self.assertEqual(roman_numerals_to_int("-CLXXXIX"), None)


if __name__ == '__main__':
    main()
