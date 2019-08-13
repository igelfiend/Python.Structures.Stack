#!/usr/bin/env python
# coding=utf8

import unittest
from main import Stack, StackReversed


class TestForStack(unittest.TestCase):
    # ---------- TEST PUSH -------------------------
    def test_push_single_element_in_empty_stack(self):
        stack = Stack()
        stack.push(1)

        result_list = stack.stack
        check_list = [1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Push'. Pushing single element. Stack lists not equal")

    def test_push_multiple_elements_in_empty_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        result_list = stack.stack
        check_list = [3, 2, 1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Push'. Pushing multiple elements. Stack lists not equal")

    # ----------- TEST POP ---------------------------
    def test_pop_single_element_from_normal_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value = stack.pop()
        check_value = 3

        result_list = stack.stack
        check_list = [2, 1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop single element from normal stack. Stack lists not equal")
        self.assertEqual(test_value, check_value,
                         "Testing 'Pop'. Pop single element from normal stack. Popped value not correct")

    def test_pop_multiple_elements_from_normal_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value1 = stack.pop()
        check_value1 = 3

        test_value2 = stack.pop()
        check_value2 = 2

        result_list = stack.stack
        check_list = [1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Stack lists not equal")
        self.assertEqual(test_value1, check_value1,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Popped value not correct")
        self.assertEqual(test_value2, check_value2,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Popped value not correct")

    def test_pop_single_element_from_empty_stack(self):
        stack = Stack()

        test_value = stack.pop()

        result_list = stack.stack
        check_list = []

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop single element from empty stack. Stack lists not equal")
        self.assertIsNone(test_value,
                          "Testing 'Pop'. Pop single element from empty stack. Popped value not correct")

    # ----------- TEST PEEK -----------------------------
    def test_peek_normal_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value = stack.peek()
        check_value = 3

        result_list = stack.stack
        check_list = [3, 2, 1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Peek'. Peek from normal stack. Stack lists not equal")
        self.assertEqual(test_value, check_value,
                         "Testing 'Peek'. Peek from normal stack. Peek value is incorrect")

    def test_peek_empty_stack(self):
        stack = Stack()

        test_value = stack.peek()

        result_list = stack.stack
        check_list = []

        self.assertEqual(result_list, check_list,
                         "Testing 'Peek'. Peek from empty stack. Stack lists not equal")
        self.assertIsNone(test_value,
                          "Testing 'Peek'. Peek from empty stack. Peek value is incorrect")


class TestForStackReversed(unittest.TestCase):
    # ---------- TEST PUSH -------------------------
    def test_push_single_element_in_empty_stack(self):
        stack = StackReversed()
        stack.push(1)

        result_list = stack.stack
        check_list = [1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Push'. Pushing single element. Stack lists not equal")

    def test_push_multiple_elements_in_empty_stack(self):
        stack = StackReversed()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        result_list = stack.stack
        check_list = [1, 2, 3]

        self.assertEqual(result_list, check_list,
                         "Testing 'Push'. Pushing multiple elements. Stack lists not equal")

    # ----------- TEST POP ---------------------------
    def test_pop_single_element_from_normal_stack(self):
        stack = StackReversed()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value = stack.pop()
        check_value = 3

        result_list = stack.stack
        check_list = [1, 2]

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop single element from normal stack. Stack lists not equal")
        self.assertEqual(test_value, check_value,
                         "Testing 'Pop'. Pop single element from normal stack. Popped value not correct")

    def test_pop_multiple_elements_from_normal_stack(self):
        stack = StackReversed()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value1 = stack.pop()
        check_value1 = 3

        test_value2 = stack.pop()
        check_value2 = 2

        result_list = stack.stack
        check_list = [1]

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Stack lists not equal")
        self.assertEqual(test_value1, check_value1,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Popped value not correct")
        self.assertEqual(test_value2, check_value2,
                         "Testing 'Pop'. Pop multiple elements from normal stack. Popped value not correct")

    def test_pop_single_element_from_empty_stack(self):
        stack = Stack()

        test_value = stack.pop()

        result_list = stack.stack
        check_list = []

        self.assertEqual(result_list, check_list,
                         "Testing 'Pop'. Pop single element from empty stack. Stack lists not equal")
        self.assertIsNone(test_value,
                          "Testing 'Pop'. Pop single element from empty stack. Popped value not correct")

    # ----------- TEST PEEK -----------------------------
    def test_peek_normal_stack(self):
        stack = StackReversed()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        test_value = stack.peek()
        check_value = 3

        result_list = stack.stack
        check_list = [1, 2, 3]

        self.assertEqual(result_list, check_list,
                         "Testing 'Peek'. Peek from normal stack. Stack lists not equal")
        self.assertEqual(test_value, check_value,
                         "Testing 'Peek'. Peek from normal stack. Peek value is incorrect")

    def test_peek_empty_stack(self):
        stack = Stack()

        test_value = stack.peek()

        result_list = stack.stack
        check_list = []

        self.assertEqual(result_list, check_list,
                         "Testing 'Peek'. Peek from empty stack. Stack lists not equal")
        self.assertIsNone(test_value,
                          "Testing 'Peek'. Peek from empty stack. Peek value is incorrect")


if __name__ == '__main__':
    unittest.main()
