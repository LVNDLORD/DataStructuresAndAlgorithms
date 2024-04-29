"""
Write function to check the brackets balance
You have to write a function named "check_balance" that checks whether a string with different kind of bracket symbols
is balanced or not using stack. The stack class is already available with the name "Stack"

The function "check_balance" accepts a string and it will check if the different sets of brackets symbols in the text
are balanced, i.e. every kind of open bracket symbol is closed with the same kind of bracket symbol ('()', '[]' or '{}').
If everything checks, the function should return the text "Ok - C", being C the number of pairs found.
If not, it should return the text: "Match error at position X", being X the position of the character
relative to the beginning of the text.

Notice that texts should be exactly like shown and with the same capitalization.

The idea is simple, when you encounter an opening bracket symbol (`(` or a `{` or a `[`) you will push it to the stack.
When you encounter a closing bracket symbol (`)` or a `}` or a `]`), pop the one in the stack and check if they match.
If they don't match, you can return the error. If you get to the end of text without errors, return the "Ok" text
as told before.


Some cases you want to take into account are when you encounter a closing bracket symbol before any opening one,
and when the text leaves an unmatched opening bracket symbol.
"""

from q1_push_and_pop_for_stack_structure import Stack


def check_balance(text):
    stack = Stack()
    pairs = 0
    for i, c in enumerate(text):
        if c in '([{':
            stack.push(c)
        elif c in ')]}':
            open_char = stack.pop()
            if open_char and open_char+c in ('()', '[]', '{}'):
                pairs += 1
            else:
                return f"Match error at position {i}"
    if stack.pop() is None:
        return f"Ok - {pairs}"
    else:
        return f"Match error at position {i}"


check_balance("a(b)(((c[d]e{f}g)))")
