class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 將 key 移到 OrderedDict 的最後，表示最近被使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新值，並移動 key 到最後
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # 移除最久未使用的 key (OrderedDict 的第一個元素)
            self.cache.popitem(last=False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)