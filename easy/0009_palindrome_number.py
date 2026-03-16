class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        half_reverse = 0
        while (x > half_reverse):
            half_reverse = half_reverse * 10 + x % 10
            x //= 10
        if x == half_reverse or x == half_reverse // 10:
            return True
        return False
        
        
