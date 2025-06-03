class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]

        for i in range(len(nums)):

            if max_jump < i:
                return False

            max_jump = max(max_jump, i + nums[i])

            if max_jump >= len(nums) - 1:
                return True

        return True
        