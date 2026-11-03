class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if(len(s) % 2 != 0):
            return False

        for i in range(len(s)):
            if (s[i] == '{') or (s[i] == '[') or (s[i] == '('):
                stack.append(s[i])
            else:
                if not stack:
                    return False
                check = stack.pop()
                if (check == '(' and s[i] == ')') or (check == '[' and s[i] == ']') or (check == '{' and s[i] == '}'):
                    continue
                else:
                    return False

        return not stack