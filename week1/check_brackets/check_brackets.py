# python2

from os import listdir
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def checker(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, start=1):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i
            
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                return i
            
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position
    
    return "Success"

    # Printing answer, write your code here

if __name__ == "__main__":
    text = sys.stdin.read()
    #text = "{"
    print(checker(text))
"""
tests = listdir("/Users/akashp1997/Documents/data-structures/data-structures/week1/check_brackets/tests")
for i in tests:
    print tests
    test_case = open(i, "r").readline().strip("\n")
    print test_case
"""
