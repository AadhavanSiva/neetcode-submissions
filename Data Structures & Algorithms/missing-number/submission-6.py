class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        nums.sort()
        while index < len(nums):
            if nums[index] != index:
                return index
            index += 1
        return index
        