class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_mapping.values():
                stack.append(char)
            elif char in bracket_mapping.keys():
                if not stack or stack.pop() != bracket_mapping[char]:
                    return False

        return not stack