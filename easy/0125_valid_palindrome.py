class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(filter(str.isalnum, s))
        return new_s.lower() == new_s[::-1].lower()
