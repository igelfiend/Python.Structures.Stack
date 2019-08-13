import unittest

from brackets import check_brackets_in_string


class BracketsTester(unittest.TestCase):
    # -------------- VALID CASES --------------------------
    def test_valid_row1(self):
        data = "(((()())))"
        self.assertEqual(True, check_brackets_in_string(data),
                         "valid case 1. %{0} must be valid".format(data))

    def test_valid_row2(self):
        data = "()()()"
        self.assertEqual(True, check_brackets_in_string(data),
                         "valid case 2. %{0} must be valid".format(data))

    def test_valid_row3(self):
        data = "()()()(()())"
        self.assertEqual(True, check_brackets_in_string(data),
                         "valid case 3. %{0} must be valid".format(data))

    def test_valid_row4(self):
        data = "((((()))))"
        self.assertEqual(True, check_brackets_in_string(data),
                         "valid case 4. %{0} must be valid".format(data))

    # ------------- INVALID CASES ---------------------------

    def test_invalid_row1(self):
        data = "()(()"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 1. %{0} must be invalid".format(data))

    def test_invalid_row2(self):
        data = "((("
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 2. %{0} must be invalid".format(data))

    def test_invalid_row3(self):
        data = "))))"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 3. %{0} must be invalid".format(data))

    def test_invalid_row4(self):
        data = ")()()()()"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 4. %{0} must be invalid".format(data))

    def test_invalid_row5(self):
        data = ")()()()()"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 5. %{0} must be invalid".format(data))

    def test_invalid_row6(self):
        data = "((())()))"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 6. %{0} must be invalid".format(data))

    def test_invalid_row7(self):
        data = "(()()"
        self.assertEqual(False, check_brackets_in_string(data),
                         "invalid case 7. %{0} must be invalid".format(data))


if __name__ == '__main__':
    unittest.main()
