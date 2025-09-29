class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        results = []

        for num in nums:
            if num == 0:
                zeros.append(num)
            else:
                results.append(num)

        new_nums = results + zeros

        for i in range(len(nums)):
            nums[i] = new_nums[i]
        