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
        if self.capacity != self.size:
            self.d[key] = value
            self.lru.add(key)
            self.size = len(self.d)
        else:
            k = self.lru.remove(0)
            del self.d[k]
            self.d[key] = value
            self.lru.add(key)  
            self.size = len(self.d)      
