class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        max_length = 0
        max_count = 0
        start = 0
        char_count = defaultdict(int)

        for end in range(len(s)):
            char_count[s[end]] += 1
            max_count = max(max_count, char_count[s[end]])

            if (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)
            
        return max_length
        