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


def check_brackets_in_string(check_str):
    # Creating stack for provide string validation
    stack = Stack()
    is_valid = True
    for element in check_str:
        if element == "(":
            stack.push(1)
        elif element == ")" and stack.size() > 0:
            stack.pop()
        else:
            is_valid = False
            break

    return is_valid and stack.size() == 0


