class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left, right):
            cnt = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        total = 0

        for i in range(len(s)):
            # 홀수일 때
            total += expand_around_center(i, i)
            # 짝수일 때
            total += expand_around_center(i, i+1)
        
        return total

        