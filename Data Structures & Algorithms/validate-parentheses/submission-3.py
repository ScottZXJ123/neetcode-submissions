class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {']':'[', ')': '(', '}': '{'}
        for c in s: 
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop() #对上后直接把左边对应的最后一个元素弹出
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False