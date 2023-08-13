import unittest


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

for _ in range(10):
    print(next(fib))


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = fibonacci()

    def test_first_ten_numbers(self):
        expected_results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for expected in expected_results:
            result = next(self.fib)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
