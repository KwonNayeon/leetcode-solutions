class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = sum(nums[:k]) / k
        max_avg = curr_avg

        # nums = [1,12,-5,-6,50,3]
        for i in range(k, len(nums)):
            curr_avg += (nums[i] - nums[i-k]) / k
            max_avg = max(curr_avg, max_avg)

        return max_avg