class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [None]
        self.kth = k

        for i in range(len(nums)):
            self.add(nums[i])
        

    def add(self, val: int) -> int:

        self.heap.append(val)

        i = len(self.heap) - 1

        while  i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp
            i = i // 2

        if len(self.heap) - 1 > self.kth:
            self.heap[1] = self.heap[-1]
            self.heap.pop()

            
            i = 1
            while 2 * i < len(self.heap):
                child = 2 * i

                if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                    child += 1

                if self.heap[i] <= self.heap[child]:
                    break

                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child

        return self.heap[1]
        
