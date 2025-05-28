class Solution:
    def getSum(self, a: int, b: int) -> int:
        b = 0
        mask = 0xffffffff

        while b & mask != 0:
            a, b = a ^ b, (a & b) << 1

        return a & mask if b > mask else a
        