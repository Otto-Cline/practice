class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1 
        
        top_k = heapq.nlargest(k, seen.keys(), key=seen.get)
        return top_k
