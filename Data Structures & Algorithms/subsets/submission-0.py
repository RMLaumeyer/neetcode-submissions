class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []

        def back(start, path):
            arr.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                back(i + 1, path)
                path.pop()

        back(0, [])
        return arr
