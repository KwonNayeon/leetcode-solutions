class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k]) # 1+12-5-6
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k] # nums[i-k] == nums[0]
            max_sum = max(current_sum, max_sum)

        return max_sum / k


        