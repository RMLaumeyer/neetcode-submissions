class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}

        for i in range(len(nums)):
            if nums[i] in dictt:
                return True
            else:
                dictt[nums[i]] = True

        return False