import unittest
from add_function import add


class TestAddFunction(unittest.TestCase):
    """
    Testy jednostkowe dla funkcji add(numbers).

    Sprawdzają poprawność działania funkcji w różnych przypadkach,
    takich jak puste wejście, jednoelementowe wejście, wiele liczb
    oddzielonych przecinkami lub znakami nowej linii oraz nieprawidłowe wejścia.
    """

    def test_empty_string_returns_zero(self):
        """
        Testuje, że pusty string zwraca 0.

        Returns:
            None
        """
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        """
        Testuje, że pojedyncza liczba jest zwracana jako wynik.

        Returns:
            None
        """
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("0"), 0)
        self.assertEqual(add("999"), 999)

    def test_two_numbers(self):
        """
        Testuje sumowanie dwóch liczb oddzielonych przecinkiem.

        Returns:
            None
        """
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("10,20"), 30)
        self.assertEqual(add("100,200"), 300)

    def test_multiple_numbers(self):
        """
        Testuje sumowanie wielu liczb oddzielonych przecinkami.

        Returns:
            None
        """
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("4,5,6,7"), 22)
        self.assertEqual(add("10,20,30,40,50"), 150)
        self.assertEqual(add("0,0,0,0"), 0)
        self.assertEqual(add("1,0,2,0,3"), 6)

    def test_numbers_with_newlines(self):
        """
        Testuje sumowanie liczb oddzielonych znakami nowej linii.

        Returns:
            None
        """
        self.assertEqual(add("1\n2"), 3)
        self.assertEqual(add("10\n20\n30"), 60)
        self.assertEqual(add("0\n0\n0"), 0)

    def test_newline_and_comma_delimiters(self):
        """
        Testuje sumowanie liczb oddzielonych przecinkami i znakami nowej linii.

        Returns:
            None
        """
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("1\n2\n3,4"), 10)
        self.assertEqual(add("5,5\n5"), 15)

    def test_trailing_newline_or_comma_invalid(self):
        """
        Testuje, że funkcja rzuca wyjątek ValueError,
        gdy wejście kończy się przecinkiem lub znakiem nowej linii.

        Raises:
            ValueError: gdy wejście jest nieprawidłowe
        """
        with self.assertRaises(ValueError):
            add("1,\n")
        with self.assertRaises(ValueError):
            add("1,\n2,")
        with self.assertRaises(ValueError):
            add("1,\n2\n")

    def test_leading_or_double_delimiters_invalid(self):
        """
        Testuje, że funkcja rzuca wyjątek ValueError,
        gdy wejście zawiera nieprawidłowe lub podwójne separatory.

        Raises:
            ValueError: gdy wejście jest nieprawidłowe
        """
        with self.assertRaises(ValueError):
            add(",1,2")
        with self.assertRaises(ValueError):
            add("\n1,2")
        with self.assertRaises(ValueError):
            add("1,,2")
        with self.assertRaises(ValueError):
            add("1\n\n2")

    def test_large_numbers(self):
        """
        Testuje sumowanie bardzo dużych liczb.

        Returns:
            None
        """
        self.assertEqual(add("1000000,2000000,3000000"), 6000000)

    def test_mixed_zero_and_large_numbers(self):
        """
        Testuje sumowanie zer i bardzo dużych liczb razem.

        Returns:
            None
        """
        self.assertEqual(add("0,1000000,0,2000000,0,3000000,0"), 6000000)


if __name__ == "__main__":
    unittest.main()
