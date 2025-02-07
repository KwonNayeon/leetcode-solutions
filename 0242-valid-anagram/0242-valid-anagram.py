class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = s.replace(' ', '').lower()
        t = t.replace(' ', '').lower()

        if sorted(s) == sorted(t):
            return True
        else:
            return False
        