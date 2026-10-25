class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        sums = ( (len(nums)*(len(nums) + 1))//2  )
        for n in nums:
            total += n
            
        return sums - total
        