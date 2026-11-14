class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        ho = 0

        for c in s:
            if c == "(":
                lo += 1
                ho += 1
            elif c == ")":
                lo -= 1
                ho -= 1
            else:
                lo -= 1
                ho += 1
            
            if ho < 0:
                return False
            if lo < 0:
                lo = 0
                
        return lo == 0