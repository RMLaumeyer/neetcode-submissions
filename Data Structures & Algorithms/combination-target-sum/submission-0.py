class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []

        def back(start, path, total):
            if total == target:
                arr.append(path[:])
                return
            
            if total > target:
                return


            for i in range(start, len(nums)):
                path.append(nums[i])
                back(i, path, total + nums[i])
                path.pop()

        back(0, [], 0)
        return arr

