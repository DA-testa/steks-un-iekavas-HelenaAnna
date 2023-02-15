# python3

from collections import namedtuple

import sys

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    else:
        return "Success"

def main():
    mode = input("Choose mode (F for file or I for input): ")
    if mode.upper() == "F":
        filename = input("Enter filename: ")
        try:
            with open(filename, "r") as file:
                text = file.read().strip()
        except FileNotFoundError:
            print("File not found.")
            sys.exit(1)
    elif mode.upper() == "I":
        text = input("Enter brackets: ")
    else:
        print("Invalid mode choice.")
        sys.exit(1)

    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()