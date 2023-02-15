# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    else:
        return "Success"


def find_first_unmatched_closing_bracket(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))
        elif next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position + 1

    return None


def find_first_unmatched_opening_bracket(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))
        elif next in ")]}":
            # Process closing bracket
            top = opening_brackets_stack[-1]
            if not are_matching(top.char, next):
                return i + 1

            opening_brackets_stack.pop()

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position + 1

    return None


def find_error_location(text):
    unmatched_closing_bracket_location = find_first_unmatched_closing_bracket(text)
    if unmatched_closing_bracket_location is not None:
        return unmatched_closing_bracket_location

    unmatched_opening_bracket_location = find_first_unmatched_opening_bracket(text)
    if unmatched_opening_bracket_location is not None:
        return unmatched_opening_bracket_location

    return "Success"


def main():
    mode = input("Choose mode (F for file or I for input): ")
    if mode.upper() == "F":
        file_name = input("Enter file name: ")
        with open(file_name, "r") as f:
            text = f.read().strip()
    elif mode.upper() == "I":
        text = input("Enter the string: ")
    else:
        print("Invalid mode choice")
        return

    error_location = find_error_location(text)
    print(error_location)

if __name__ == "__main__":
    main()
