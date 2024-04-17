class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            del self.cache[self.queue.pop(0)]
        self.cache[key] = value
        self.queue.append(key)


class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            del self.cache[self.queue.pop()]
        self.cache[key] = value
        self.queue.append(key)


# Page reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3
page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
page_frames = 4

# LRU page replacement algorithm
lru_cache = LRUCache(page_frames)
for page in page_reference_string:
    lru_cache.put(page, page)
    print(f"LRU Cache: {lru_cache.cache.keys()}")
print() 
# MRU page replacement algorithm
mru_cache = MRUCache(page_frames)
for page in page_reference_string:
    mru_cache.put(page, page)
    print(f"MRU Cache: {mru_cache.cache.keys()}")