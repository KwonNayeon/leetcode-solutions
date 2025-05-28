class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            current_sum = a ^ b
            next_carry = (a & b) << 1

            a = a ^ b
            b = (a & b) << 1

        return a
        