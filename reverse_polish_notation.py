#!/usr/bin/env python
# coding=utf8

from copy import deepcopy

"""
Important: Class was copy-pasted in cause of using it in study.
Normal use case suppose to import that class
"""


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.stack:
            return None
        else:
            value = deepcopy(self.stack[0])
            del self.stack[0]
            return value

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[0]


def use_operator(v1, v2, operator):
    if operator == "*":
        return v1 * v2
    elif operator == "+":
        return v1 + v2
    else:
        print("Error: incorrect operator was passed")
        raise Exception("Incorrect operator was passed")


def process_rpn(data_row):
    """
    :param data_row: string with reverse polish notation, each element must be splitted by space.
     Can be ended with '='
    :return: expression result (or None if any error was caused)
    """
    data_stack = Stack()
    process_stack = Stack()

    data_stack.stack = data_row.split(" ")

    try:
        while data_stack.size() != 0 and data_stack.peek() != "=":
            current_element = data_stack.pop()
            if str.isdigit(current_element):
                process_stack.push(int(current_element))
            elif current_element == "=":
                return process_stack.pop()
            else:
                if process_stack.size() != 2:
                    raise Exception("Data sequence corrupted")

                v1 = process_stack.pop()
                v2 = process_stack.pop()

                process_stack.push(use_operator(v1, v2, current_element))
        return process_stack.pop()
    except Exception as e:
        print("{0}".format(e))
        return None
