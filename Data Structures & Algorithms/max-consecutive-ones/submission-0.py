class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxTotal = 0
        maxtemp = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                maxtemp += 1
                maxTotal = max(maxTotal, maxtemp)
            else:
                maxtemp = 0

        return maxTotal