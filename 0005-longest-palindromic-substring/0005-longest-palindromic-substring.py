class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        max_len = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]

                if substr == substr[::-1]:
                    if len(substr) > max_len:
                        max_len = len(substr)
                        longest_palindrome = substr

        return longest_palindrome


        