class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in dictt:
                return [dictt[temp], i]

            dictt[nums[i]] = i