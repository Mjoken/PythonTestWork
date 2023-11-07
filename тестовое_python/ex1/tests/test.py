from unittest import TestCase, main
from source.main import prime_numbers


class MyTestCase(TestCase):
    def testNumbers(self):
        self.assertEqual(prime_numbers(0, 10), [0, 1, 2, 3, 5, 7])  # add assertion here
        self.assertEqual(prime_numbers(3, 5), [3])
        self.assertEqual(prime_numbers(8, 11), [])
        self.assertEqual(prime_numbers(9950, 10001), [9967, 9973])

    def testError(self):
        self.assertEqual(prime_numbers(0, "a"), [])
        self.assertEqual(prime_numbers(0, 3.5), [])

    def testBadChoice(self):
        self.assertEqual(prime_numbers(-50, -10), [])
        self.assertEqual(prime_numbers(-10, 10), [])
        self.assertEqual(prime_numbers(0, 0), [])


if __name__ == '__main__':
    main()
