class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        result = []

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            result.append(suffixes[i] * prefixes[i])
        
        print(prefixes)
        print(suffixes)
        return result
