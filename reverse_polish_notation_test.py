#!/usr/bin/env python
# coding=utf8

import unittest
from reverse_polish_notation import process_rpn


class TestRpn(unittest.TestCase):
    def test_case1(self):
        test_row = "2 2 +"
        test_result = process_rpn(test_row)
        check_result = 4
        self.assertEqual(test_result, check_result,
                         "Test case 1. Result mismatch")

    def test_case2(self):
        test_row = "2 2 + 3 *"
        test_result = process_rpn(test_row)
        check_result = 12
        self.assertEqual(test_result, check_result,
                         "Test case 2. Result mismatch")

    def test_case3(self):
        test_row = "8 2 + 5 * 9 + ="
        test_result = process_rpn(test_row)
        check_result = 59
        self.assertEqual(test_result, check_result,
                         "Test case 3. Result mismatch")


if __name__ == '__main__':
    unittest.main()
