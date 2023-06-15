# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true
#

# Input: s = "(]"
# Output: false

def isValid(s):

    # Dictionary mapping opening brackets to their corresponding closing brackets
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []  # Initialize an empty stack to track opening brackets

    for char in s:  # Iterate through each character in the input string
        if char in pairs:  # If the character is an opening bracket
            stack.append(char)  # Push it onto the stack
        elif char in pairs.values():  # If the character is a closing bracket
            if not stack or pairs[
                stack.pop()] != char:  # Check if stack is empty or if the topmost opening bracket doesn't match the current closing bracket
                return False  # Return False if the brackets are not balanced

    return len(stack) == 0  # Return True if the stack is empty (all brackets are balanced), False otherwise


print(isValid("{[]}"))  # Output: True

print(isValid("(]"))