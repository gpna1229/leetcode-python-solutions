"""
Approach 1: Sliding Window with Slicing and Indexing.
Complexity:
- Time: O(n^2) due to slicing and .index() within the loop.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in s[start:i]:
                start += s[start:i].index(s[i]) + 1
            max_len = max(max_len, i - start + 1)
        return max_len

"""
Approach 2: Standard Sliding Window using a set.
Complexity:
- Time: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        start = end = max_len = 0
        window = set()
        while end < len(s):
            if s[end] in window:
                window.remove(s[start])
                start += 1
            else:
                window.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
        return max_len
