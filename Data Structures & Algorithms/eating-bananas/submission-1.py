class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        slow = 1
        fast = max(piles)

        while slow <= fast:
            mid = (slow + fast) // 2

            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] + mid -1) // mid

            if hours > h:
                slow = mid +1              
            else:
                fast = mid - 1

        return slow
 