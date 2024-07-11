from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        open = deque()
        result = []

        for char_s in s:
            if char_s == '(':
                open.append(len(result))
            elif char_s == ')':
                start = open.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(char_s)
        return "".join(result)