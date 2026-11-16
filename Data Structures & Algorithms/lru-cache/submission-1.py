class LRUCache:

    def __init__(self, capacity: int):
        self.dictt = {}
        self.cap = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.dictt:
            val = self.dictt.pop(key)
            self.dictt[key] = val
            return val 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictt:
            self.dictt.pop(key)
            self.count -= 1  # FIX


        elif self.count == self.cap:
            oldest = next(iter(self.dictt))
            self.dictt.pop(oldest)
            self.count -= 1

        self.dictt[key] = value
        self.count += 1

        
