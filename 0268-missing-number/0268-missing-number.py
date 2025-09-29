class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums_set = set(nums)

        for i in range(0, max(nums) + 1):
            if i not in nums_set:
                return i

        return max(nums) + 1