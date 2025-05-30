class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if i > 1 and s[i-2] != '0':
                two_digit = int(s[i-2:i])
                if 1 <= two_digit <= 26:
                    dp[i] += dp[i-2]

        return dp[n]
