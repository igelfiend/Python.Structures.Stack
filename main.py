#!/usr/bin/env python
# coding=utf8

from copy import deepcopy


class Stack:
    """
    Class represents stack container interface.
    Provides push, pop and peek functions.
    """
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


class StackReversed:
    """
    Class represents stack container interface,
    but all operations (push, pop, peek) executes in tail side.
    """
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.stack:
            return None
        else:
            value = deepcopy(self.stack[-1])
            del self.stack[-1]
            return value

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]
