# python3

from collections import namedtuple

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
                return i

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def main():
    text = input().strip()
    if not all(bracket in "([{)]}" for bracket in text):
        print("Invalid input format. Please enter a string containing only brackets.")
    else:
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch + 1)

if __name__ == "__main__":
    main()