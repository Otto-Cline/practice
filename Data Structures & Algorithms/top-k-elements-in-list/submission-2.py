class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1 
        
        array = []
        for num, count in seen.items():
            array.append([count, num])
        array.sort()

        answer = []
        while len(answer) < k:
            answer.append(array.pop()[1])
        return answer
