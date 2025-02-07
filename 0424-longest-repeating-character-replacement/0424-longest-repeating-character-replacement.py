class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            curr_length = right - left + 1

            if curr_length - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length