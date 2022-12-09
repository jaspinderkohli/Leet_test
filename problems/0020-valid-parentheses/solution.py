class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # map the open brackets to their corresponding close brackets
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch in bracket_map:
                # if the character is an open bracket, push it onto the stack
                stack.append(ch)
            elif len(stack) == 0 or bracket_map[stack.pop()] != ch:
                # if the stack is empty or the popped element is not the corresponding open bracket for the current close bracket, then the string is not valid
                return False

        return len(stack) == 0

