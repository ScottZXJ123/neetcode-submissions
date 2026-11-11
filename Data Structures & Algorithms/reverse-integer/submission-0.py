class Solution:
    def reverse(self, x: int) -> int:
        MAX = 0x7FFFFFFF
        
        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10

            if res > (MAX - digit) // 10:
                return 0
            
            res = res * 10 + digit
        
        return sign * res