class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        indx = self._hash(key)
        bucket = self.buckets[indx]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        indx = self._hash(key)
        bucket = self.buckets[indx]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        indx = self._hash(key)
        bucket = self.buckets[indx]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del(bucket[i])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)