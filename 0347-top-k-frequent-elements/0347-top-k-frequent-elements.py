class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        heap = []
        
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num, freq in frequency.items():
            heapq.heappush(heap, (-freq, num))
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        