class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        current_start = 0
        max_length = 0

        for i in range(len(s)):
            char = s[i]

            if char in seen and seen[char] >= current_start:
                current_start = seen[char] + 1

            seen[char] = i

            current_length = i - current_start + 1

            max_length = max(current_length, max_length)
        
        return max_length
