class LRUCache:

    def __init__(self, capacity: int):
        self.d = defaultdict(int)
        self.capacity = capacity
        self.size = 0
        self.lru = set()

    def get(self, key: int) -> int:
        return self.d.get(key,-1)
        self.lru.add(key)
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.lru.add(key)
            self.size = len(self.d)
        
        if self.size >= self.capacity:
            k = next(iter(self.lru)) 
            self.lru.remove(k)
            del self.d[k]

        else:
            self.size += 1

        self.d[key] = value
        self.lru.add(key)     
