class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False
        stack = []
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if c != d[a]:
                    return False
        return len(stack) == 0
